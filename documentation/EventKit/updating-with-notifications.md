# Updating with notifications

**Framework**: EventKit

Register for notifications about changes and keep your app up to date.

#### Overview

It’s possible for another process or app to modify the Calendar database while your app is running. If your app fetches calendar events or reminders, register to be notified about changes to the Calendar database to ensure the calendar and reminder information you display to the user is current.

##### Register for Notifications

An [`EKEventStore`](ekeventstore.md) object posts an [`EKEventStoreChangedNotification`](ekeventstorechangednotification.md) notification whenever it detects changes to the Calendar database. Register for this notification if your app handles event or reminder data.

The code listing below registers for the [`EKEventStoreChangedNotification`](ekeventstorechangednotification.md) notification.

```swift
NotificationCenter.default.addObserver(self, selector: Selector("storeChanged:"), name: .EKEventStoreChanged, object: eventStore)
```

##### Respond to Notifications

When you receive an [`EKEventStoreChangedNotification`](ekeventstorechangednotification.md) notification, it’s possible the objects you’ve fetched—such as an [`EKEvent`](ekevent.md), [`EKReminder`](ekreminder.md), or [`EKCalendar`](ekcalendar.md)—have changed. The effect of the changes depends on whether an event was added, modified, or deleted:

- If an event was added, it does not affect any of your previously fetched events or reminders, but the added event may fall within the date range of events you are displaying to the user.
- If an event was modified or deleted, properties of [`EKEvent`](ekevent.md) and [`EKReminder`](ekreminder.md) objects representing that event may become out of date.

Because your local data is often invalidated or incomplete when a change occurs in the Calendar database, you should refetch your current date range of events whenever you receive an [`EKEventStoreChangedNotification`](ekeventstorechangednotification.md) notification. If you are modifying an event and do not want to refetch it unless it is absolutely necessary, call the [`refreshSourcesIfNecessary()`](ekeventstore/refreshsourcesifnecessary().md) method on the event. If the method returns `YES`, you can continue to use the event; otherwise, you must refetch it. 

> **Note**:  Events being modified in an event view controller with EventKitUI for iOS are updated automatically when a change occurs in the Calendar database. See [`EventKit UI`](https://developer.apple.com/documentation/EventKitUI) for more.

## See Also

- [Creating events and reminders](creating-events-and-reminders.md)
  Create and modify events and reminders in a person’s database.
- [Retrieving events and reminders](retrieving-events-and-reminders.md)
  Fetch events and reminders from the Calendar database.
- [Managing location-based reminders](managing-location-based-reminders.md)
  Access reminders set up with geofence-enabled alarms on a person’s calendars.
- [class EKEvent](ekevent.md)
  A class that represents an event in a calendar.
- [class EKReminder](ekreminder.md)
  A class that represents a reminder in a calendar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/updating-with-notifications)*