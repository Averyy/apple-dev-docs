# undoNestedGroup()

**Framework**: Foundation  
**Kind**: method

Performs the undo operations in the last undo group (whether top-level or nested), recording the operations on the redo stack as a single group.

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
func undoNestedGroup()
```

#### Discussion

Raises an `NSInternalInconsistencyException` if any undo operations have been registered since the last [`enableUndoRegistration()`](undomanager/enableundoregistration().md) message.

This method posts an [`NSUndoManagerCheckpoint`](nsnotification/name-swift.struct/nsundomanagercheckpoint.md) and [`NSUndoManagerWillUndoChange`](nsnotification/name-swift.struct/nsundomanagerwillundochange.md) before it performs the undo operation, and it posts an [`NSUndoManagerDidUndoChange`](nsnotification/name-swift.struct/nsundomanagerdidundochange.md) after it performs the undo operation.

## See Also

- [func undo()](undomanager/undo.md)
  Closes the top-level undo group if necessary, and then performs undo operations on the group.
- [func redo()](undomanager/redo.md)
  Performs the operations in the last group on the redo stack, if there are any, recording them on the undo stack as a single group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/undonestedgroup())*