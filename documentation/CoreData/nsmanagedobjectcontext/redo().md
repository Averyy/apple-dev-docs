# redo()

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Sends a redo message to the context’s undo manager, asking it to reverse the latest undo operation applied to objects in the object graph.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func redo()
```

```objc
- (void) redo;
```

## See Also

### Related Documentation
- [func processPendingChanges()](./processpendingchanges%28%29.md)
  Forces the context to process changes to the object graph.
### Undoing changes
- [var undoManager: UndoManager?](./undomanager.md)
  The object that provides undo support for the context.
- [func undo()](./undo%28%29.md)
  Sends an undo message to the context’s undo manager, asking it to reverse the latest uncommitted changes applied to objects in the object graph.
- [func reset()](./reset%28%29.md)
  Returns the context to its base state.
- [func rollback()](./rollback%28%29.md)
  Removes everything from the undo stack, discards all insertions and deletions, and restores updated objects to their last committed values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/redo())*