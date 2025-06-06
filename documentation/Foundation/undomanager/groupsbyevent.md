# groupsByEvent

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the manager automatically creates undo groups around each pass of the run loop.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var groupsByEvent: Bool { get set }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if the manager automatically creates undo groups around each pass of the run loop, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

The default is [`true`](https://developer.apple.com/documentation/swift/true). If you turn automatic grouping off, you must close groups explicitly before invoking either [`undo()`](undomanager/undo().md) or [`undoNestedGroup()`](undomanager/undonestedgroup().md).

## See Also

- [func beginUndoGrouping()](undomanager/beginundogrouping.md)
  Marks the beginning of an undo group.
- [func endUndoGrouping()](undomanager/endundogrouping.md)
  Marks the end of an undo group.
- [var groupingLevel: Int](undomanager/groupinglevel.md)
  The number of nested undo groups (or redo groups, if redo is the most recent operation) in the current event loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/groupsbyevent)*