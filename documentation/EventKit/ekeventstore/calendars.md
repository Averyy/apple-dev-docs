# calendars

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

The calendars associated with the event store.

**Availability**:
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use [`calendars(for:)`](./calendars%28for%29.md) instead.

## Declaration

```swift
var calendars: [EKCalendar] { get }
```

```objc
@property (nonatomic, readonly) NSArray<EKCalendar *> * calendars;
```

## Mentions

- [Creating events and reminders](../creating-events-and-reminders.md)

## See Also

### Accessing calendars
- [var defaultCalendarForNewEvents: EKCalendar?](./defaultcalendarfornewevents.md)
  The calendar that events are added to by default, as specified by user settings.
- [func defaultCalendarForNewReminders() -> EKCalendar?](./defaultcalendarfornewreminders%28%29.md)
  Identifies the default calendar for adding reminders to, as specified by user settings.
- [func calendars(for: EKEntityType) -> [EKCalendar]](./calendars%28for%29.md)
  Identifies the calendars that support a given entity type, such as reminders or events.
- [func calendar(withIdentifier: String) -> EKCalendar?](./calendar%28withidentifier%29.md)
  Locates a calendar with the specified identifier.
- [func saveCalendar(EKCalendar, commit: Bool) throws](./savecalendar%28_,commit%29.md)
  Saves a calendar to the event store by either committing or batching the changes.
- [func removeCalendar(EKCalendar, commit: Bool) throws](./removecalendar%28_,commit%29.md)
  Removes a calendar from the event store by either committing or batching the changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/calendars)*