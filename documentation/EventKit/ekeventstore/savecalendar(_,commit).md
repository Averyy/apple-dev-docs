# saveCalendar(_:commit:)

**Framework**: EventKit  
**Kind**: method  
**Role**: Instance Method

Saves a calendar to the event store by either committing or batching the changes.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
func saveCalendar(_ calendar: EKCalendar, commit: Bool) throws
```

```objc
- (BOOL) saveCalendar:(EKCalendar *) calendar commit:(BOOL) commit error:(NSError **) error;
```

## Discussion

This method raises an exception if `calendar` belongs to another event store.

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. Call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `calendar`: The calendar to save.
- `commit`: [`true`](../../Swift/true.md) to save the calendar immediately; otherwise, the change is batched until the [`commit()`](./commit%28%29.md) method is invoked.

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
- [func removeCalendar(EKCalendar, commit: Bool) throws](./removecalendar%28_,commit%29.md)
  Removes a calendar from the event store by either committing or batching the changes.
- [var calendars: [EKCalendar]](./calendars.md)
  The calendars associated with the event store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/savecalendar(_:commit:))*