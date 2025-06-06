# EKReminder

**Framework**: EventKit  
**Kind**: class

A class that represents a reminder in a calendar.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class EKReminder
```

## Mentions

- [Creating events and reminders](creating-events-and-reminders.md)

#### Overview

Use the [`init(eventStore:)`](ekreminder/init(eventstore:).md) method to create a new reminder. Use the properties in the class to get and modify certain information about a reminder.

## Topics

### Creating a Reminder
- [init(eventStore: EKEventStore)](ekreminder/init(eventstore:).md)
  Creates and returns a new reminder in the given event store.
### Accessing Reminder Properties
- [enum EKReminderPriority](ekreminderpriority.md)
  The priority of the reminder.
- [var priority: Int](ekreminder/priority.md)
  The reminder’s priority.
- [var startDateComponents: DateComponents?](ekreminder/startdatecomponents.md)
  The start date of the task.
- [var dueDateComponents: DateComponents?](ekreminder/duedatecomponents.md)
  The date by which the reminder should be completed.
- [var isCompleted: Bool](ekreminder/iscompleted.md)
  A Boolean value determining whether or not the reminder is marked completed.
- [var completionDate: Date?](ekreminder/completiondate.md)
  The date on which the reminder was completed.

## Relationships

### Inherits From
- [EKCalendarItem](ekcalendaritem.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Creating events and reminders](creating-events-and-reminders.md)
  Create and modify events and reminders in a person’s database.
- [Retrieving events and reminders](retrieving-events-and-reminders.md)
  Fetch events and reminders from the Calendar database.
- [Updating with notifications](updating-with-notifications.md)
  Register for notifications about changes and keep your app up to date.
- [Managing Location-Based Reminders](managing-location-based-reminders.md)
  Add, fetch, complete, remove, and sort location-based reminders in your app.
- [class EKEvent](ekevent.md)
  A class that represents an event in a calendar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekreminder)*