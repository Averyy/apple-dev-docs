# commit()

**Framework**: EventKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) commit:(NSError **) error;
```

## Mentions

- [Creating events and reminders](../creating-events-and-reminders.md)

#### Discussion

This method allows you to save batched changes to the event store. For example, if you pass [`false`](../../Swift/false.md) as the `commit` parameter to the [`saveCalendar(_:commit:)`](./savecalendar%28_,commit%29.md), [`removeCalendar(_:commit:)`](./removecalendar%28_,commit%29.md), [`save(_:span:commit:)`](./save%28_,span,commit%29.md), or [`remove(_:span:commit:)`](./remove%28_,span,commit%29.md) methods, the changes aren’t saved until [`commit()`](./commit%28%29.md) is invoked. Likewise, if you pass [`true`](../../Swift/true.md) as the `commit` parameter to the above methods, you don’t need to call [`commit()`](./commit%28%29.md).

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. Call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Saving and restoring state
- [func reset()](./reset%28%29.md)
  Reverts the event store to its saved state.
- [func refreshSourcesIfNecessary()](./refreshsourcesifnecessary%28%29.md)
  Pulls new data from remote sources, if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/commit())*