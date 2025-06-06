# remove(_:commit:)

**Framework**: Eventkit  
**Kind**: method

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

## Mentions

- [Creating events and reminders](creating-events-and-reminders.md)

#### Discussion

This method raises an exception if `reminder` belongs to another event store.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. Call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `reminder`: The reminder to remove.
- `commit`: A Boolean value that indicates whether to remove the reminder immediately or to batch the removals; passing   won’t commit the removal from the event store until the   method is invoked.

## See Also

- [func commit() throws](ekeventstore/commit.md)
  Commits all unsaved changes to the event store.
- [func event(withIdentifier: String) -> EKEvent?](ekeventstore/event(withidentifier:).md)
  Locates the first occurrence of an event with a given identifier.
- [func calendarItem(withIdentifier: String) -> EKCalendarItem?](ekeventstore/calendaritem(withidentifier:).md)
  Locates a reminder or the first occurrence of an event with the specified identifier.
- [func calendarItems(withExternalIdentifier: String) -> [EKCalendarItem]](ekeventstore/calendaritems(withexternalidentifier:).md)
  Locates all reminders or the first occurrences of all events with the specified external identifier.
- [func remove(EKEvent, span: EKSpan) throws](ekeventstore/remove(_:span:).md)
  Removes an event from the event store.
- [func remove(EKEvent, span: EKSpan, commit: Bool) throws](ekeventstore/remove(_:span:commit:).md)
  Removes an event or recurring events from the event store by either committing or batching the changes.
- [func save(EKEvent, span: EKSpan) throws](ekeventstore/save(_:span:).md)
  Saves changes to an event permanently.
- [func save(EKEvent, span: EKSpan, commit: Bool) throws](ekeventstore/save(_:span:commit:).md)
  Saves an event or recurring events to the event store by either committing or batching the changes.
- [func save(EKReminder, commit: Bool) throws](ekeventstore/save(_:commit:).md)
  Saves changes to a reminder by either committing or batching the changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/remove(_:commit:))*