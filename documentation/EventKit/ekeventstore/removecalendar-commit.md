# removeCalendar(_:commit:)

**Framework**: EventKit  
**Kind**: method

Removes a calendar from the event store by either committing or batching the changes.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
func removeCalendar(_ calendar: EKCalendar, commit: Bool) throws
```

#### Discussion

This method raises an exception if `calendar` belongs to another event store.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. Call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

 In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. Call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `calendar`: The calendar to remove.
- `commit`:   to remove the calendar immediately; otherwise, the change is batched until the   method is invoked.

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
- [var calendars: [EKCalendar]](ekeventstore/calendars.md)
  The calendars associated with the event store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/removecalendar(_:commit:))*