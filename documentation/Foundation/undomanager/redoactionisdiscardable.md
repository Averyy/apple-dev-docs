# redoActionIsDiscardable

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the next redo action is discardable.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var redoActionIsDiscardable: Bool { get }
```

```objc
@property (readonly) BOOL redoActionIsDiscardable;
```

#### Discussion

[`true`](../../Swift/true.md) if the action is discardable; [`false`](../../Swift/false.md) otherwise.

Specifies that the latest redo action may be safely discarded when a document can not be saved for any reason. These are typically actions that don’t affect persistent state.

An example might be an redo action that changes the viewable area of a document.

## See Also

### Using discardable undo and redo actions
- [func setActionIsDiscardable(Bool)](./setactionisdiscardable%28_%29.md)
  Sets whether the next undo or redo action is discardable.
- [var undoActionIsDiscardable: Bool](./undoactionisdiscardable.md)
  A Boolean value that indicates whether the next undo action is discardable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/redoactionisdiscardable)*