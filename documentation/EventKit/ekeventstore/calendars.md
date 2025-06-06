# calendars

**Framework**: EventKit  
**Kind**: property

The calendars associated with the event store.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var calendars: [EKCalendar] { get }
```

## Mentions

- [Creating events and reminders](creating-events-and-reminders.md)

## See Also

- [var defaultCalendarForNewEvents: EKCalendar?](ekeventstore/defaultcalendarfornewevents.md)
  The calendar that events are added to by default, as specified by user settings.
- [func defaultCalendarForNewReminders() -> EKCalendar?](ekeventstore/defaultcalendarfornewreminders.md)
  Identifies the default calendar for adding reminders to, as specified by user settings.
- [func calendars(for: EKEntityType) -> [EKCalendar]](ekeventstore/calendars(for:).md)
  Identifies the calendars that support a given entity type, such as reminders or events.
- [func calendar(withIdentifier: String) -> EKCalendar?](ekeventstore/calendar(withidentifier:).md)
  Locates a calendar with the specified identifier.
- [func saveCalendar(EKCalendar, commit: Bool) throws](ekeventstore/savecalendar(_:commit:).md)
  Saves a calendar to the event store by either committing or batching the changes.
- [func removeCalendar(EKCalendar, commit: Bool) throws](ekeventstore/removecalendar(_:commit:).md)
  Removes a calendar from the event store by either committing or batching the changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/calendars)*