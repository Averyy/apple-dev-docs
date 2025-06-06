# calendars(for:)

**Framework**: EventKit  
**Kind**: method

Identifies the calendars that support a given entity type, such as reminders or events.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func calendars(for entityType: EKEntityType) -> [EKCalendar]
```

## Mentions

- [Retrieving events and reminders](retrieving-events-and-reminders.md)

#### Return Value

An array of calendars that support the specified entity type.

## Parameters

- `entityType`: The calendar’s entity type.

## See Also

- [var defaultCalendarForNewEvents: EKCalendar?](ekeventstore/defaultcalendarfornewevents.md)
  The calendar that events are added to by default, as specified by user settings.
- [func defaultCalendarForNewReminders() -> EKCalendar?](ekeventstore/defaultcalendarfornewreminders.md)
  Identifies the default calendar for adding reminders to, as specified by user settings.
- [func calendar(withIdentifier: String) -> EKCalendar?](ekeventstore/calendar(withidentifier:).md)
  Locates a calendar with the specified identifier.
- [func saveCalendar(EKCalendar, commit: Bool) throws](ekeventstore/savecalendar(_:commit:).md)
  Saves a calendar to the event store by either committing or batching the changes.
- [func removeCalendar(EKCalendar, commit: Bool) throws](ekeventstore/removecalendar(_:commit:).md)
  Removes a calendar from the event store by either committing or batching the changes.
- [var calendars: [EKCalendar]](ekeventstore/calendars.md)
  The calendars associated with the event store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/calendars(for:))*