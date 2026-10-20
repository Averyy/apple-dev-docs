# groupsByEvent

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property BOOL groupsByEvent;
```

#### Discussion

[`true`](../../Swift/true.md) if the manager automatically creates undo groups around each pass of the run loop, otherwise [`false`](../../Swift/false.md).

The default is [`true`](../../Swift/true.md). If you turn automatic grouping off, you must close groups explicitly before invoking either [`undo()`](./undo%28%29.md) or [`undoNestedGroup()`](./undonestedgroup%28%29.md).

## See Also

### Creating undo groups
- [func beginUndoGrouping()](./beginundogrouping%28%29.md)
  Marks the beginning of an undo group.
- [func endUndoGrouping()](./endundogrouping%28%29.md)
  Marks the end of an undo group.
- [var groupingLevel: Int](./groupinglevel.md)
  The number of nested undo groups (or redo groups, if redo is the most recent operation) in the current event loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/groupsbyevent)*