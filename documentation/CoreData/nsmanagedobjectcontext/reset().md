# reset()

**Framework**: Core Data  
**Kind**: method

Returns the context to its base state.

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
func reset()
```

## Mentions

- [Accessing data when the store changes](accessing-data-when-the-store-changes.md)

#### Discussion

All the receiver’s managed objects are “forgotten.” If you use this method, you should ensure that you also discard references to any managed objects fetched using the receiver, since they will be invalid afterwards.

## See Also

- [var stalenessInterval: TimeInterval](nsmanagedobjectcontext/stalenessinterval.md)
  The maximum length of time that may have elapsed since the store previously fetched data before fulfilling a fault issues a new fetch.
- [var undoManager: UndoManager?](nsmanagedobjectcontext/undomanager.md)
  The object that provides undo support for the context.
- [func undo()](nsmanagedobjectcontext/undo.md)
  Sends an undo message to the context’s undo manager, asking it to reverse the latest uncommitted changes applied to objects in the object graph.
- [func redo()](nsmanagedobjectcontext/redo.md)
  Sends a redo message to the context’s undo manager, asking it to reverse the latest undo operation applied to objects in the object graph.
- [func rollback()](nsmanagedobjectcontext/rollback.md)
  Removes everything from the undo stack, discards all insertions and deletions, and restores updated objects to their last committed values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/reset())*