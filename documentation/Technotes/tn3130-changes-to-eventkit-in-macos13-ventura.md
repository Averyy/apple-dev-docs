# TN3130: Changes to EventKit in macOS Ventura 13

**Framework**: Technotes

Test your apps against EventKit API changes in macOS Ventura 13.

#### Overview

In macOS Ventura 13, the EventKit framework has seen significant changes. This document highlights some of the notable changes. To learn about related changes in iOS 16, see [`TN3132: Changes to EventKit and EventKitUI in iOS 16`](tn3132-changes-eventkit-and-eventkitui-in-ios16.md).

For apps running on systems prior to macOS Ventura 13, the legacy behavior remains in place when using EventKit. When you run your app on macOS Ventura 13, and have built it with Xcode 14 and linked against the macOS 13 SDK, you may see behavior that you are unfamiliar with when using EventKit. To identify these changes in behavior, thoroughly test your app for each major OS version it supports. Confirm that your implementation of EventKit behaves as you expect in each OS version and update your code where needed. If you notice an unexpected behavior in EventKit, report it using [`Feedback Assistant`](https://developer.apple.comhttps://developer.apple.com/bug-reporting/).

#### Ekcalendar

The inherited initializer `init()` throws an exception when attempting to create a new calendar. Use [`init(for:eventStore:)`](https://developer.apple.com/documentation/EventKit/EKCalendar/init(for:eventStore:)) instead.

```swift
let calendar = EKCalendar(for: .event, eventStore: eventStore)
```

In the legacy behavior, this inherited initializer returns an unusable `EKCalendar` object.

#### Ekcalendaritem

##### Fetching Recurence Rules

The [`recurrenceRules`](https://developer.apple.com/documentation/EventKit/EKCalendarItem/recurrenceRules) property returns an empty array if the calendar item doesn’t have any recurrence rules.

In the legacy behavior, `recurrenceRules` returns `nil` if the calendar item doesn’t have any recurrence rules.

##### Updating Time Zones

Changing the time zone of an event no longer changes the absolute time at which it occurs.

#### Ekevent

##### Creating Events

The inherited initializer `init()` throws an exception when attempting to create a new event. Use [`init(eventStore:)`](https://developer.apple.com/documentation/EventKit/EKEvent/init(eventStore:)) to create new events.

In the legacy behavior, this inherited initializer returns an unusable `EKEvent` object.

##### Event Identifiers

The [`eventIdentifier`](https://developer.apple.com/documentation/EventKit/EKEvent/eventIdentifier) property now returns identifiers in a new format. The previous identifier format will continue to work.

##### End Date of All Day Events

The [`endDate`](https://developer.apple.com/documentation/EventKit/EKEvent/endDate) property of all-day events returns a time of `11:59:59 PM` on the last day of this event.

```json
Event title: Marathon  
Start date: June 18, 2022 at 12:00:00 AM PDT
End date: June 18, 2022 at 11:59:59 PM PDT
```

In the legacy behavior, this property returns a time of `12:00:00 AM` on the day after the event.

```json
Event title: Marathon  
Start date: June 18, 2022 at 12:00:00 AM PDT
End date: June 19, 2022 at 12:00:00 AM PDT
```

#### Ekeventstore

##### Accessing Sources

The [`sources`](https://developer.apple.com/documentation/EventKit/EKEventStore/sources) property now contains delegate sources.

```swift
// Fetch all sources associated with the event store.
let sources = eventStore.sources

sources.forEach { source in
    // Let's check whether source is a delegate event source.
    let name = (source.isDelegate) ? "Delegate Source" : "Source"
    print("\(name): \(source.title)")
}
// Prints "Source: iCloud"
// Prints "Delegate Source: Calculus Office Hours"
```

##### Fetching Events

[`events(matching:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/events(matching:)) and [`enumerateEvents(matching:using:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/enumerateEvents(matching:using:)) no longer necessarily return events sorted by start date.

##### Accessing Calendar Events

The [`calendarItem(withIdentifier:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/calendarItem(withIdentifier:)), [`calendarItems(withExternalIdentifier:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/calendarItems(withExternalIdentifier:)), and [`event(withIdentifier:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/event(withIdentifier:)) methods may return different occurrences of an event or reminder with a given identifier in some cases. For instance, when the first occurrence of a recurring event was modified and the specified identifier refers to this occurrence. In this case, use the given identifier to fetch the unmodified version of the event’s first occurrence.

##### Committing Changes

When you call [`saveCalendar(_:commit:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/saveCalendar(_:commit:)), [`removeCalendar(_:commit:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/removeCalendar(_:commit:)), [`save(_:span:commit:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/save(_:span:commit:)), [`remove(_:span:commit:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/remove(_:span:commit:)), [`save(_:commit:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/save(_:commit:)), or [`remove(_:commit:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/remove(_:commit:)) methods with the `commit` parameter set to `true`, [`EKEventStore`](https://developer.apple.com/documentation/EventKit/EKEventStore) attempts to immediatedly save and commit your changes to the event store. If the commit fails, `EKEventStore` automatically rolls back all changes that been saved but aren’t yet committed to the event store.

In the legacy behavior, uncommitted objects remain saved in the event store.

#### Ekreminder

The inherited initializer `init()` throws an exception when attempting to create a new reminder. Use [`init(eventStore:)`](https://developer.apple.com/documentation/EventKit/EKReminder/init(eventStore:)) instead.

```swift
let reminder = EKReminder(eventStore: eventStore)
```

In the legacy behavior, this inherited initializer returns an unusable `EKReminder` object.

#### Eksource

The [`isDelegate`](https://developer.apple.com/documentation/EventKit/EKSource/isDelegate) property indicates whether the source is an event source delegated to the user.

#### Revision History

-  First published.

## See Also

- [TN3189: Managing Mail background traffic load](tn3189-managing-mail-background-traffic-load.md)
  Identify iOS Mail background traffic and manage its impact on your IMAP server.
- [TN3187: Migrating to the UIKit scene-based life cycle](tn3187-migrating-to-the-uikit-scene-based-life-cycle.md)
  Update your app to receive scene-based life-cycle events and manage your user interface using scene objects and methods.
- [TN3188: Troubleshooting In-App Purchases availability in the App Store](tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md)
  Verify your In-App Purchases are approved and available for sale in the App Store.
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.
- [TN3185: Troubleshooting In-App Purchases availability in Xcode](tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md)
  Inspect your active StoreKit configuration file for unexpected configurations.
- [TN3182: Adding privacy tracking keys to your privacy manifest](tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest.md)
  Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.
- [TN3183: Adding required reason API entries to your privacy manifest](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest.md)
  Declare the APIs that can potentially fingerprint devices in your app or third-party SDK in a privacy manifest.
- [TN3184: Adding data collection details to your privacy manifest](tn3184-adding-data-collection-details-to-your-privacy-manifest.md)
  Declare the data your app or third-party SDK collects in a privacy manifest.
- [TN3181: Debugging an invalid privacy manifest](tn3181-debugging-invalid-privacy-manifest.md)
  Identify common configurations that cause unsuccessful privacy manifest validation with the App Store.
- [TN3180: Reverting to App Store Server Notifications V1](tn3180-reverting-app-store-server-notifications-v1.md)
  Migrate from version 2 to version 1 of App Store Server Notifications using the Modify an App endpoint.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3178: Checking for and resolving build UUID problems](tn3178-checking-for-and-resolving-build-uuid-problems.md)
  Ensure that every Mach-O image has a UUID, and that every distinct Mach-O image has its own unique UUID.
- [TN3177: Understanding alternate audio track groups in movie files](tn3177-understanding-alternate-audio-track-groups-in-movie-files.md)
  Learn how alternate groups collect audio tracks, and how to choose which audio track to use in your app.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3176: Troubleshooting Apple Pay payment processing issues](tn3176-troubleshooting-apple-pay-payment-processing-issues.md)
  Diagnose errors that occur when processing Apple Pay payments, identify common causes, and explore potential solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3130-changes-to-eventkit-in-macos13-ventura)*