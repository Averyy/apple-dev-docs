# remove(_:commit:)

**Framework**: EventKit  
**Kind**: method  
**Role**: Instance Method

Removes a reminder from the event store by either committing or batching the changes.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
func remove(_ reminder: EKReminder, commit: Bool) throws
```

```objc
- (BOOL) removeReminder:(EKReminder *) reminder commit:(BOOL) commit error:(NSError **) error;
```

## Mentions

- [Creating events and reminders](../creating-events-and-reminders.md)

## Discussion

This method raises an exception if `reminder` belongs to another event store.

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. Call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `reminder`: The reminder to remove.
- `commit`: A Boolean value that indicates whether to remove the reminder immediately or to batch the removals; passing [`false`](../../Swift/false.md) won’t commit the removal from the event store until the [`commit()`](./commit%28%29.md) method is invoked.

## See Also

### Related Documentation
- [func commit() throws](./commit%28%29.md)
  Commits all unsaved changes to the event store.
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
- [func save(EKEvent, span: EKSpan) throws](./save%28_,span%29.md)
  Saves changes to an event permanently.
- [func save(EKEvent, span: EKSpan, commit: Bool) throws](./save%28_,span,commit%29.md)
  Saves an event or recurring events to the event store by either committing or batching the changes.
- [func save(EKReminder, commit: Bool) throws](./save%28_,commit%29.md)
  Saves changes to a reminder by either committing or batching the changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/remove(_:commit:))*