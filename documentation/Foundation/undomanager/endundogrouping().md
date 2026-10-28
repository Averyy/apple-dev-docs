# endUndoGrouping()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Marks the end of an undo group.

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
func endUndoGrouping()
```

```objc
- (void) endUndoGrouping;
```

## Discussion

All individual undo operations back to the matching [`beginUndoGrouping()`](./beginundogrouping%28%29.md) message are grouped together and reversed by a later [`undo()`](./undo%28%29.md) or [`undoNestedGroup()`](./undonestedgroup%28%29.md) message. Undo groups can be nested, thus providing functionality similar to nested transactions. Raises an `NSInternalInconsistencyException` if there’s no [`beginUndoGrouping()`](./beginundogrouping%28%29.md) message in effect.

This method posts an [`NSUndoManagerCheckpoint`](../nsnotification/name-swift.struct/nsundomanagercheckpoint.md) and an [`NSUndoManagerDidCloseUndoGroup`](../nsnotification/name-swift.struct/nsundomanagerdidcloseundogroup.md) just before the group is closed.

## See Also

### Related Documentation
- [var levelsOfUndo: Int](./levelsofundo.md)
  The maximum number of top-level undo groups the undo manager holds.
### Creating undo groups
- [func beginUndoGrouping()](./beginundogrouping%28%29.md)
  Marks the beginning of an undo group.
- [var groupsByEvent: Bool](./groupsbyevent.md)
  A Boolean value that indicates whether the manager automatically creates undo groups around each pass of the run loop.
- [var groupingLevel: Int](./groupinglevel.md)
  The number of nested undo groups (or redo groups, if redo is the most recent operation) in the current event loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/endundogrouping())*