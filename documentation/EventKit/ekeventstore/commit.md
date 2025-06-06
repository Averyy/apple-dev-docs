# commit()

**Framework**: EventKit  
**Kind**: method

Commits all unsaved changes to the event store.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
func commit() throws
```

## Mentions

- [Creating events and reminders](creating-events-and-reminders.md)

#### Discussion

This method allows you to save batched changes to the event store. For example, if you pass [`false`](https://developer.apple.com/documentation/swift/false) as the `commit` parameter to the [`saveCalendar(_:commit:)`](ekeventstore/savecalendar(_:commit:).md), [`removeCalendar(_:commit:)`](ekeventstore/removecalendar(_:commit:).md), [`save(_:span:commit:)`](ekeventstore/save(_:span:commit:).md), or [`remove(_:span:commit:)`](ekeventstore/remove(_:span:commit:).md) methods, the changes aren’t saved until [`commit()`](ekeventstore/commit().md) is invoked. Likewise, if you pass [`true`](https://developer.apple.com/documentation/swift/true) as the `commit` parameter to the above methods, you don’t need to call [`commit()`](ekeventstore/commit().md).

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. Call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

 In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. Call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

- [func reset()](ekeventstore/reset.md)
  Reverts the event store to its saved state.
- [func refreshSourcesIfNecessary()](ekeventstore/refreshsourcesifnecessary.md)
  Pulls new data from remote sources, if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/commit())*