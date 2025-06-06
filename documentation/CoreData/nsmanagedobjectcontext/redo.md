# redo()

**Framework**: Core Data  
**Kind**: method

Sends a redo message to the context’s undo manager, asking it to reverse the latest undo operation applied to objects in the object graph.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func redo()
```

## See Also

- [func processPendingChanges()](nsmanagedobjectcontext/processpendingchanges.md)
  Forces the context to process changes to the object graph.
- [var undoManager: UndoManager?](nsmanagedobjectcontext/undomanager.md)
  The object that provides undo support for the context.
- [func undo()](nsmanagedobjectcontext/undo.md)
  Sends an undo message to the context’s undo manager, asking it to reverse the latest uncommitted changes applied to objects in the object graph.
- [func reset()](nsmanagedobjectcontext/reset.md)
  Returns the context to its base state.
- [func rollback()](nsmanagedobjectcontext/rollback.md)
  Removes everything from the undo stack, discards all insertions and deletions, and restores updated objects to their last committed values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/redo())*