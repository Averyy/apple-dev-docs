# save(_:span:)

**Framework**: EventKit  
**Kind**: method  
**Role**: Instance Method

Saves changes to an event permanently.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
func save(_ event: EKEvent, span: EKSpan) throws
```

```objc
- (BOOL) saveEvent:(EKEvent *) event span:(EKSpan) span error:(NSError **) error;
```

#### Discussion

This method raises an exception if it’s passed an event from another event store.

When saving an event, it’s updated in the Calendar database. Any fields you didn’t modify are updated to reflect the most recent value in the database. If the event has been deleted from the database, it’s recreated as a new event.

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. Call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `event`: The event to save.
- `span`: The span that indicates whether to remove a single event or all future instances of the event in the case of a recurring event.

## See Also

### Accessing calendar events
- [func event(withIdentifier: String) -> EKEvent?](./event%28withidentifier%29.md)
  Locates the first occurrence of an event with a given identifier.
- [func calendarItem(withIdentifier: String) -> EKCalendarItem?](./calendaritem%28withidentifier%29.md)
  Locates a reminder or the first occurrence of an event with the specified identifier.
- [func calendarItems(withExternalIdentifier: String) -> [EKCalendarItem]](./calendaritems%28withexternalidentifier%29.md)
  Locates all reminders or the first occurrences of all events with the specified external identifier.
- [func remove(EKEvent, span: EKSpan) throws](./remove%28_,span%29.md)
  Removes an event from the event store.
- [func remove(EKEvent, span: EKSpan, commit: Bool) throws](./remove%28_,span,commit%29.md)
  Removes an event or recurring events from the event store by either committing or batching the changes.
- [func remove(EKReminder, commit: Bool) throws](./remove%28_,commit%29.md)
  Removes a reminder from the event store by either committing or batching the changes.
- [func save(EKEvent, span: EKSpan, commit: Bool) throws](./save%28_,span,commit%29.md)
  Saves an event or recurring events to the event store by either committing or batching the changes.
- [func save(EKReminder, commit: Bool) throws](./save%28_,commit%29.md)
  Saves changes to a reminder by either committing or batching the changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/save(_:span:))*