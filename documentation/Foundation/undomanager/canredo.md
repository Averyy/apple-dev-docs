# canRedo

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the manager has any actions to redo.

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
@MainActor
var canRedo: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/Swift/true) if the manager has any actions to redo, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

Because any undo operation registered clears the redo stack, this method posts an [`NSUndoManagerCheckpoint`](nsnotification/name-swift.struct/nsundomanagercheckpoint.md) to allow clients to apply their pending operations before testing the redo stack.

## See Also

- [func redo()](undomanager/redo.md)
  Performs the operations in the last group on the redo stack, if there are any, recording them on the undo stack as a single group.
- [var canUndo: Bool](undomanager/canundo.md)
  A Boolean value that indicates whether the manager has any actions to undo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/canredo)*