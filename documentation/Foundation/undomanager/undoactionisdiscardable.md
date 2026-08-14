# undoActionIsDiscardable

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the next undo action is discardable.

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
var undoActionIsDiscardable: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if the action is discardable; [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

Specifies that the latest undo action may be safely discarded when a document can not be saved for any reason. These are typically actions that don’t affect persistent state.

An example might be an undo action that changes the viewable area of a document.

## See Also

- [func setActionIsDiscardable(Bool)](undomanager/setactionisdiscardable(_:).md)
  Sets whether the next undo or redo action is discardable.
- [var redoActionIsDiscardable: Bool](undomanager/redoactionisdiscardable.md)
  A Boolean value that indicates whether the next redo action is discardable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/undoactionisdiscardable)*