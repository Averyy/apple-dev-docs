# EKCalendarItem

**Framework**: EventKit  
**Kind**: class

An abstract superclass for calendar events and reminders.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class EKCalendarItem
```

## Mentions

- [Creating events and reminders](creating-events-and-reminders.md)
- [Creating a recurring event](creating-a-recurring-event.md)

#### Overview

The `EKCalendarItem` is a an abstract superclass for calendar events and reminders. This class provides common properties and methods for accessing properties of calendar items such as the ability to set the calendar, title, and location, as well as support for attaching notes, displaying attendees, setting multiple alarms, and specifying recurrence rules.

## Topics

### Accessing Calendar Items
- [var calendarItemIdentifier: String](ekcalendaritem/calendaritemidentifier.md)
  The calendar item’s unique identifier.
- [var calendarItemExternalIdentifier: String!](ekcalendaritem/calendaritemexternalidentifier.md)
  The calendar item’s external identifier as provided by the calendar server.
- [var uuid: String](ekcalendaritem/uuid.md)
  The calendar item’s unique identifier.
### Accessing Calendar Item Properties
- [var calendar: EKCalendar!](ekcalendaritem/calendar.md)
  The calendar for the calendar item.
- [var title: String!](ekcalendaritem/title.md)
  The title for the calendar item.
- [var location: String?](ekcalendaritem/location.md)
  The location associated with the calendar item.
- [var creationDate: Date?](ekcalendaritem/creationdate.md)
  The date that this calendar item was created.
- [var lastModifiedDate: Date?](ekcalendaritem/lastmodifieddate.md)
  The date that the calendar item was last modified.
- [var timeZone: TimeZone?](ekcalendaritem/timezone.md)
  The time zone for the calendar item.
- [var url: URL?](ekcalendaritem/url.md)
  The URL for the calendar item.
### Attaching Notes
- [var hasNotes: Bool](ekcalendaritem/hasnotes.md)
  A Boolean value that indicates whether the calendar item has notes.
- [var notes: String?](ekcalendaritem/notes.md)
  The notes associated with the calendar item.
### Displaying Attendees
- [var hasAttendees: Bool](ekcalendaritem/hasattendees.md)
  A Boolean value that indicates whether the calendar item has attendees.
- [var attendees: [EKParticipant]?](ekcalendaritem/attendees.md)
  The attendees associated with the calendar item, as an array of [`EKParticipant`](ekparticipant.md) objects.
### Adding and Removing Alarms
- [var hasAlarms: Bool](ekcalendaritem/hasalarms.md)
  A Boolean value that indicates whether the calendar item has alarms.
- [func addAlarm(EKAlarm)](ekcalendaritem/addalarm(_:).md)
  Adds an alarm to the receiver.
- [func removeAlarm(EKAlarm)](ekcalendaritem/removealarm(_:).md)
  Removes an alarm from the calendar item.
- [var alarms: [EKAlarm]?](ekcalendaritem/alarms.md)
  The alarms associated with the calendar item, as an array of [`EKAlarm`](ekalarm.md) objects.
### Setting Recurrence Rules
- [var hasRecurrenceRules: Bool](ekcalendaritem/hasrecurrencerules.md)
  A Boolean value that indicates whether the calendar item has recurrence rules.
- [func addRecurrenceRule(EKRecurrenceRule)](ekcalendaritem/addrecurrencerule(_:).md)
  Adds a recurrence rule to the recurrence rule array.
- [func removeRecurrenceRule(EKRecurrenceRule)](ekcalendaritem/removerecurrencerule(_:).md)
  Removes a recurrence rule from the recurrence rule array.
- [var recurrenceRules: [EKRecurrenceRule]?](ekcalendaritem/recurrencerules.md)
  The recurrence rules for the calendar item.

## Relationships

### Inherits From
- [EKObject](ekobject.md)
### Inherited By
- [EKEvent](ekevent.md)
- [EKReminder](ekreminder.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class EKObject](ekobject.md)
  An abstract superclass for all EventKit classes that have persistent instances.
- [class EKSource](eksource.md)
  An abstract superclass that represents the account a calendar belongs to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekcalendaritem)*