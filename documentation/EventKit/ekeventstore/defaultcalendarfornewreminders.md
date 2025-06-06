# defaultCalendarForNewReminders()

**Framework**: EventKit  
**Kind**: method

Identifies the default calendar for adding reminders to, as specified by user settings.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func defaultCalendarForNewReminders() -> EKCalendar?
```

#### Return Value

The calendar that reminders are added to by default.

## See Also

- [var defaultCalendarForNewEvents: EKCalendar?](ekeventstore/defaultcalendarfornewevents.md)
  The calendar that events are added to by default, as specified by user settings.
- [func calendars(for: EKEntityType) -> [EKCalendar]](ekeventstore/calendars(for:).md)
  Identifies the calendars that support a given entity type, such as reminders or events.
- [func calendar(withIdentifier: String) -> EKCalendar?](ekeventstore/calendar(withidentifier:).md)
  Locates a calendar with the specified identifier.
- [func saveCalendar(EKCalendar, commit: Bool) throws](ekeventstore/savecalendar(_:commit:).md)
  Saves a calendar to the event store by either committing or batching the changes.
- [func removeCalendar(EKCalendar, commit: Bool) throws](ekeventstore/removecalendar(_:commit:).md)
  Removes a calendar from the event store by either committing or batching the changes.
- [var calendars: [EKCalendar]](ekeventstore/calendars.md)
  The calendars associated with the event store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/defaultcalendarfornewreminders())*