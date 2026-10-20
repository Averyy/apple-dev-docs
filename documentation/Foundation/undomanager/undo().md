# undo()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Closes the top-level undo group if necessary, and then performs undo operations on the group.

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
func undo()
```

```objc
- (void) undo;
```

#### Discussion

After closing the top-level undo group, this method invokes [`undoNestedGroup()`](./undonestedgroup%28%29.md).

This method also invokes [`endUndoGrouping()`](./endundogrouping%28%29.md) if the nesting level is 1. Raises an `NSInternalInconsistencyException` if more than one undo group is open (that is, if the last group isn’t at the top level).

This method posts an [`NSUndoManagerCheckpoint`](../nsnotification/name-swift.struct/nsundomanagercheckpoint.md).

## See Also

### Related Documentation
- [var groupingLevel: Int](./groupinglevel.md)
  The number of nested undo groups (or redo groups, if redo is the most recent operation) in the current event loop.
- [func enableUndoRegistration()](./enableundoregistration%28%29.md)
  Enables the recording of undo operations.
### Performing undo and redo
- [func undoNestedGroup()](./undonestedgroup%28%29.md)
  Performs the undo operations in the last undo group (whether top-level or nested), recording the operations on the redo stack as a single group.
- [func redo()](./redo%28%29.md)
  Performs the operations in the last group on the redo stack, if there are any, recording them on the undo stack as a single group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/undo())*