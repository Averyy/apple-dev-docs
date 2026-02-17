# beginUndoGrouping()

**Framework**: Foundation  
**Kind**: method

Marks the beginning of an undo group.

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
func beginUndoGrouping()
```

#### Discussion

All individual undo operations before a subsequent [`endUndoGrouping()`](undomanager/endundogrouping().md) message are grouped together and reversed by a later [`undo()`](undomanager/undo().md) message. By default undo groups are begun automatically at the start of the event loop, but you can begin your own undo groups with this method, and nest them within other groups.

This method posts an [`NSUndoManagerCheckpoint`](nsnotification/name-swift.struct/nsundomanagercheckpoint.md) unless a top-level undo is in progress. It posts an [`NSUndoManagerDidOpenUndoGroup`](nsnotification/name-swift.struct/nsundomanagerdidopenundogroup.md) if a new group was successfully created.

## See Also

- [func endUndoGrouping()](undomanager/endundogrouping.md)
  Marks the end of an undo group.
- [var groupsByEvent: Bool](undomanager/groupsbyevent.md)
  A Boolean value that indicates whether the manager automatically creates undo groups around each pass of the run loop.
- [var groupingLevel: Int](undomanager/groupinglevel.md)
  The number of nested undo groups (or redo groups, if redo is the most recent operation) in the current event loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/beginundogrouping())*