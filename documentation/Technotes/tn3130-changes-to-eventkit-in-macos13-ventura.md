# TN3130: Changes to EventKit in macOS Ventura 13

**Framework**: Technotes  
**Role**: Technote

Test your apps against EventKit API changes in macOS Ventura 13.

## Overview

In macOS Ventura 13, the EventKit framework has seen significant changes. This document highlights some of the notable changes. To learn about related changes in iOS 16, see [TN3132: Changes to EventKit and EventKitUI in iOS 16](./tn3132-changes-eventkit-and-eventkitui-in-ios16.md).

For apps running on systems prior to macOS Ventura 13, the legacy behavior remains in place when using EventKit. When you run your app on macOS Ventura 13, and have built it with Xcode 14 and linked against the macOS 13 SDK, you may see behavior that you are unfamiliar with when using EventKit. To identify these changes in behavior, thoroughly test your app for each major OS version it supports. Confirm that your implementation of EventKit behaves as you expect in each OS version and update your code where needed. If you notice an unexpected behavior in EventKit, report it using [Feedback Assistant](https://developer.apple.com/bug-reporting/).

## EKCalendar

The inherited initializer `init()` throws an exception when attempting to create a new calendar. Use [`init(for:eventStore:)`](../EventKit/ekcalendar/init%28for,eventstore%29.md) instead.

```swift
let calendar = EKCalendar(for: .event, eventStore: eventStore)
```

In the legacy behavior, this inherited initializer returns an unusable `EKCalendar` object.

## EKCalendarItem

### Fetching recurrence rules

The [`recurrenceRules`](../EventKit/ekcalendaritem/recurrencerules.md) property returns an empty array if the calendar item doesn’t have any recurrence rules.

In the legacy behavior, `recurrenceRules` returns `nil` if the calendar item doesn’t have any recurrence rules.

### Updating time zones

Changing the time zone of an event no longer changes the absolute time at which it occurs.

## EKEvent

### Creating events

The inherited initializer `init()` throws an exception when attempting to create a new event. Use [`init(eventStore:)`](../EventKit/ekevent/init%28eventstore%29.md) to create new events.

In the legacy behavior, this inherited initializer returns an unusable `EKEvent` object.

### Event identifiers

The [`eventIdentifier`](../EventKit/ekevent/eventidentifier.md) property now returns identifiers in a new format. The previous identifier format will continue to work.

### End date of all-day events

The [`endDate`](../EventKit/ekevent/enddate.md) property of all-day events returns a time of `11:59:59 PM` on the last day of this event.

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

## EKEventStore

### Accessing sources

The [`sources`](../EventKit/ekeventstore/sources.md) property now contains delegate sources.

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

### Fetching events

[`events(matching:)`](../EventKit/ekeventstore/events%28matching%29.md) and [`enumerateEvents(matching:using:)`](../EventKit/ekeventstore/enumerateevents%28matching,using%29.md) no longer necessarily return events sorted by start date.

### Accessing calendar events

The [`calendarItem(withIdentifier:)`](../EventKit/ekeventstore/calendaritem%28withidentifier%29.md), [`calendarItems(withExternalIdentifier:)`](../EventKit/ekeventstore/calendaritems%28withexternalidentifier%29.md), and [`event(withIdentifier:)`](../EventKit/ekeventstore/event%28withidentifier%29.md) methods may return different occurrences of an event or reminder with a given identifier in some cases. For instance, when the first occurrence of a recurring event was modified and the specified identifier refers to this occurrence. In this case, use the given identifier to fetch the unmodified version of the event’s first occurrence.

### Committing changes

When you call [`saveCalendar(_:commit:)`](../EventKit/ekeventstore/savecalendar%28_,commit%29.md), [`removeCalendar(_:commit:)`](../EventKit/ekeventstore/removecalendar%28_,commit%29.md), [`save(_:span:commit:)`](../EventKit/ekeventstore/save%28_,span,commit%29.md), [`remove(_:span:commit:)`](../EventKit/ekeventstore/remove%28_,span,commit%29.md), [`save(_:commit:)`](../EventKit/ekeventstore/save%28_,commit%29.md), or [`remove(_:commit:)`](../EventKit/ekeventstore/remove%28_,commit%29.md) methods with the `commit` parameter set to `true`, [`EKEventStore`](../EventKit/ekeventstore.md) attempts to immediately save and commit your changes to the event store. If the commit fails, `EKEventStore` automatically rolls back all changes that been saved but aren’t yet committed to the event store.

In the legacy behavior, uncommitted objects remain saved in the event store.

## EKReminder

The inherited initializer `init()` throws an exception when attempting to create a new reminder. Use [`init(eventStore:)`](../EventKit/ekreminder/init%28eventstore%29.md) instead.

```swift
let reminder = EKReminder(eventStore: eventStore)
```

In the legacy behavior, this inherited initializer returns an unusable `EKReminder` object.

## EKSource

The [isDelegate](../EventKit/eksource/isdelegate.md) property indicates whether the source is an event source delegated to the user.

## Revision History

- **2022-08-16** First published.

## See Also

### Related Documentation
- [TN3132: Changes to EventKit and EventKitUI in iOS 16](./tn3132-changes-eventkit-and-eventkitui-in-ios16.md)
  Test your apps against EventKit and EventKitUI API changes in iOS 16.
- [TN3153: Adopting API changes for EventKit in iOS 17, macOS 14, and watchOS 10](./tn3153-adopting-api-changes-for-eventkit-in-ios-macos-and-watchos.md)
  Test your existing apps against EventKit API latest changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3130-changes-to-eventkit-in-macos13-ventura)*