# defaultCalendarForNewEvents

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

The calendar that events are added to by default, as specified by user settings.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var defaultCalendarForNewEvents: EKCalendar? { get }
```

```objc
@property (nonatomic, readonly, nullable) EKCalendar * defaultCalendarForNewEvents;
```

## See Also

### Accessing calendars
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
- [var calendars: [EKCalendar]](./calendars.md)
  The calendars associated with the event store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/defaultcalendarfornewevents)*