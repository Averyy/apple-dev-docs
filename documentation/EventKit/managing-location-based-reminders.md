# Managing Location-Based Reminders

**Framework**: EventKit

Add, fetch, complete, remove, and sort location-based reminders in your app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Xcode 12.0+

#### Overview

With the Reminders app, users can create reminders with attachments, and alarms based on time and location. When Location Services is turned on, users receive location-based reminders when entering or leaving a specified geographic area or geofence. This sample demonstrates how to add, fetch, complete, remove, and sort location-based reminders.

##### Provide a Purpose String

The sample first requests and receives authorization from the user before the app attempts to access their reminder data. It provides a purpose string or usage description that describes how the app intends to use the user’s reminder data. It then adds the [`NSRemindersUsageDescription`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/information_property_list/nsremindersusagedescription) key to the app’s `Info.plist`. The sample sets its value to a string that explains why the app needs access to reminder data. The system displays the string when prompting the user for authorization.

> ❗ **Important**: This `NSRemindersUsageDescription` key is required for apps that access the user’s reminder data. Apps crash when the key is absent.

This `NSRemindersUsageDescription` key is required for apps that access the user’s reminder data. Apps crash when the key is absent.

##### Request Authorization

Set up your app to instantiate and use a single instance of [`EKEventStore`](ekeventstore.md) that manages all reminder-related tasks. An `EKEventStore` object requires a significant amount of time to initialize and release. The user might add, remove, or update reminders while your app is running. Register for an [`EKEventStoreChanged`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/nsnotification/name/ekeventstorechanged) notification to be notified about changes to the Calendar database. When you receive this notification, refresh all your reminder data. It’s possible that your current data is stale or invalid. For more information on change notification, see [`Updating with Notifications`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/updating_with_notifications) for details.

The user grants or denies permission when apps request access to their reminder data. Because the user can change the app’s authorization status later in the Settings app ( Settings > Privacy > Reminders) on their device, the sample calls `EKEventStore`’s [`authorizationStatus(for:)`](ekeventstore/authorizationstatus(for:).md) with a [`EKEntityType.reminder`](ekentitytype/reminder.md) entity type before attempting to access their reminder data.

```swift
guard EKEventStore.authorizationStatus(for: .reminder) == .notDetermined else {
    // The user may have already granted, denied, or restricted access to Reminders.
    verifyAuthorizationStatus()
    return
}
```

If the authorization status is [`.notDetermined`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekauthorizationstatus/notDetermined), create an instance of `EKEventStore`, then store a strong reference to it.

```swift
private var store = EKEventStore()
```

Next, call its [`requestAccess(to:completion:)`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstore/requestaccess) method to prompt the user for access.

```swift
store.requestAccess(to: .reminder, completion: {(granted, error) in
    if granted { self.accessGranted() }
})
```

The system remembers the user’s answer, so that subsequent calls to `requestAccess(to:completion:)` don’t again prompt the user. For more information on user’s reminder data access, see [`Accessing the Event Store`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/accessing_the_event_store).

##### Map Annotations

The sample app uses the current user location and location-specific data saved in the `MapData.plist` file to create annotations for the map. It defines a `MapData` data type to represent each point of interest. `MapData.plist` contains three `MapData` entries. To test reminders around other locations, duplicate and update a `MapData` entry in `MapData.plist` with other data as needed.

> ❗ **Important**: Creating location-based reminders doesn’t require location services. The sample app uses location services to display the user’s current location on the map. As such, it includes and configures the [`NSLocationWhenInUseUsageDescription`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/information_property_list/nslocationwheninuseusagedescription) key in its `Info.plist`. This key is required for apps that access the user’s location services. For more information on user’s location services access, see [`Requesting Authorization for Location Services`](https://developer.apple.comhttps://developer.apple.com/documentation/corelocation/requesting_authorization_for_location_services).

Creating location-based reminders doesn’t require location services. The sample app uses location services to display the user’s current location on the map. As such, it includes and configures the [`NSLocationWhenInUseUsageDescription`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/information_property_list/nslocationwheninuseusagedescription) key in its `Info.plist`. This key is required for apps that access the user’s location services. For more information on user’s location services access, see [`Requesting Authorization for Location Services`](https://developer.apple.comhttps://developer.apple.com/documentation/corelocation/requesting_authorization_for_location_services).

##### Check for the Existence of a Default List

Creating a reminder requires a list, which is a calendar for these items. Use `EKEventStore`’s [`defaultCalendarForNewReminders()`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstore/defaultcalendarfornewreminders) to check whether the user has specified a default list for reminders. If `defaultCalendarForNewReminders()` returns no value, prompt the user to create a list in the Reminders app or provide a mechanism that lets them create it from within the app. The app provides an `Add List` button that allows users to create a new list.

##### Create Location Based Reminders

A location-based reminder is a reminder created with a geofence-enabled alarm. A geofence-enabled alarm has a structured location and proximity configured. The structured location consists of a location object and radius. The [`radius`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekstructuredlocation/radius) is defined in meters and uses the system’s default radius when its value is 0. When the user provides a value for `radius` in a unit other than meters such as miles, convert this value before using it. The sample uses the following steps to create a location-based reminder.

First, it creates an [`EKReminder`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekreminder) object using [`init(eventStore:)`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekreminder/init), then it sets its [`title`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekcalendaritem/title) and [`calendar`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekcalendaritem/calendar) properties:

```swift
guard let calendar = store.defaultCalendarForNewReminders() else { throw LocationBasedRemindersError.missingDefaultRemindersList }
let reminder = EKReminder(eventStore: store)
reminder.calendar = calendar
reminder.title = title
```

> ❗ **Important**: The `title` and `calendar` properties are required and must be set before saving the reminder.

The `title` and `calendar` properties are required and must be set before saving the reminder.

Next, it creates a structured location by using either [`EKStructuredLocation`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekstructuredlocation)’s [`init(title:)`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekstructuredlocation/init) or [`init(title:)`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekstructuredlocation/init). When the location object has latitude and longitude coordinates, it uses `init(title:)` to create the structured location. The sample initializes an [`CLLocation`](https://developer.apple.comhttps://developer.apple.com/documentation/corelocation/cllocation) object with the specified latitude and longitude, then assigns it to the created structured location’s [`geoLocation`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekstructuredlocation/geolocation) property:

```swift
let structuredLocation = EKStructuredLocation(title: geofence.title)
structuredLocation.geoLocation = CLLocation(latitude: coordinate.latitude, longitude: coordinate.longitude)
```

When the location object is an [`MKMapItem`](https://developer.apple.comhttps://developer.apple.com/documentation/mapkit/mkmapitem) object, the sample uses `init(mapItem:)` to create the structured

```swift
let structuredLocation = EKStructuredLocation(mapItem: mapItem)
```

Then, it sets the structured location’s `radius` property to a value in meters:

```swift
// The app displays the radius's value in miles. Let's convert it from miles to meters before assigning it to the radius property.
structuredLocation.radius = 1609.344 * geofence.radius
```

After that, it creates an [`EKAlarm`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekalarm) object, then sets its [`structuredLocation`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekalarm/structuredlocation) property to the created structured location object. The sample then sets the [`proximity`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekalarm/proximity) property to a value to finish configuring the alarm’s geofence:

```swift
let alarm = EKAlarm()
alarm.structuredLocation = structuredLocation
alarm.proximity = geofence.proximity
```

The sample adds the created alarm to the reminder. For more information on adding alarms, see [`Setting an Alarm`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/setting_an_alarm).

```swift
reminder.addAlarm(alarm)
```

Finally, it saves the reminder to the user’s Calendar database:

```swift
do {
    try store.save(reminder, commit: true)
} catch {
    handleError(error, with: reminder.title)
}
```

##### Fetch Location Based Reminders

The [`fetchReminders(matching:completion:)`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstore/fetchreminders) method asynchronously fetches all reminders matching a given predicate. When successful, `fetchReminders(matching:completion:)` returns an array that contains both time-based and location-based reminders.

```swift
// Predicate that fetches all reminders in all of the user's calendars.
let predicate = store.predicateForReminders(in: nil)
var result = [EKReminder]()
store.fetchReminders(matching: predicate, completion: {(reminders: [Any]?) in
    if let reminders = reminders as? [EKReminder] {
        // Filter reminders for the location ones.
        result = reminders.filter({ (item: EKReminder) in item.isLocation })
    }
    
    DispatchQueue.main.async {
        completion(result)
    }
})
```

To retrieve location-based reminders, the sample parses this array for reminders defined with an existing alarm that has a `structuredlocation` and `proximity` value.

```swift
/// Indicates whether a reminder is a location-based one.
var isLocation: Bool {
    guard let alarms = self.alarms else { return false }
    
    return !alarms.filter({(alarm: EKAlarm) in
        return (alarm.structuredLocation != nil) && ((alarm.proximity == .enter) || (alarm.proximity == .leave))
    }).isEmpty
}
```

##### Sort Reminders

Retrieving reminders from the Calendar database returns reminders sorted by creation date. To sort an array of `EKReminder` objects by title, or any other property, the sample implements [`sorted(by:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swift/array/sorted) on the array with a predicate that uses the property.

```swift
 /// - Returns: An array of reminders sorted by title in an ascending order.
func sortedByTitle() -> [EKReminder] {
    return self.sorted(by: { (first: EKReminder, second: EKReminder) in
        first.title.localizedCaseInsensitiveCompare(second.title) == .orderedAscending
    })
}
```

## See Also

- [Creating events and reminders](creating-events-and-reminders.md)
  Create and modify events and reminders in a person’s database.
- [Retrieving events and reminders](retrieving-events-and-reminders.md)
  Fetch events and reminders from the Calendar database.
- [Updating with notifications](updating-with-notifications.md)
  Register for notifications about changes and keep your app up to date.
- [class EKEvent](ekevent.md)
  A class that represents an event in a calendar.
- [class EKReminder](ekreminder.md)
  A class that represents a reminder in a calendar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/managing-location-based-reminders)*