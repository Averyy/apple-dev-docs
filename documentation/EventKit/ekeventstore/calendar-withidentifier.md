# calendar(withIdentifier:)

**Framework**: EventKit  
**Kind**: method

Locates a calendar with the specified identifier.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func calendar(withIdentifier identifier: String) -> EKCalendar?
```

#### Return Value

A calendar with a [`calendarIdentifier`](ekcalendar/calendaridentifier.md) that matches the specified identifier.

## Parameters

- `identifier`: The calendar’s unique identifier.

## See Also

- [var defaultCalendarForNewEvents: EKCalendar?](ekeventstore/defaultcalendarfornewevents.md)
  The calendar that events are added to by default, as specified by user settings.
- [func defaultCalendarForNewReminders() -> EKCalendar?](ekeventstore/defaultcalendarfornewreminders.md)
  Identifies the default calendar for adding reminders to, as specified by user settings.
- [func calendars(for: EKEntityType) -> [EKCalendar]](ekeventstore/calendars(for:).md)
  Identifies the calendars that support a given entity type, such as reminders or events.
- [func saveCalendar(EKCalendar, commit: Bool) throws](ekeventstore/savecalendar(_:commit:).md)
  Saves a calendar to the event store by either committing or batching the changes.
- [func removeCalendar(EKCalendar, commit: Bool) throws](ekeventstore/removecalendar(_:commit:).md)
  Removes a calendar from the event store by either committing or batching the changes.
- [var calendars: [EKCalendar]](ekeventstore/calendars.md)
  The calendars associated with the event store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/calendar(withidentifier:))*