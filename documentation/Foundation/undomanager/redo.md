# redo()

**Framework**: Foundation  
**Kind**: method

Performs the operations in the last group on the redo stack, if there are any, recording them on the undo stack as a single group.

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
func redo()
```

#### Discussion

Raises an [`internalInconsistencyException`](nsexceptionname/internalinconsistencyexception.md) if the method is invoked during an undo operation.

This method posts an [`NSUndoManagerCheckpoint`](nsnotification/name-swift.struct/nsundomanagercheckpoint.md) and [`NSUndoManagerWillRedoChange`](nsnotification/name-swift.struct/nsundomanagerwillredochange.md) before it performs the redo operation, and it posts the [`NSUndoManagerDidRedoChange`](nsnotification/name-swift.struct/nsundomanagerdidredochange.md) after it performs the redo operation.

## See Also

- [func registerUndo(withTarget: Any, selector: Selector, object: Any?)](undomanager/registerundo(withtarget:selector:object:).md)
  Registers the selector of the specified target to implement a single undo operation that the target receives.
- [func undo()](undomanager/undo.md)
  Closes the top-level undo group if necessary, and then performs undo operations on the group.
- [func undoNestedGroup()](undomanager/undonestedgroup.md)
  Performs the undo operations in the last undo group (whether top-level or nested), recording the operations on the redo stack as a single group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/redo())*