# NSUndoManagerDidOpenUndoGroup

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Posted whenever an undo manager opens an undo group.

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
static let NSUndoManagerDidOpenUndoGroup: NSNotification.Name
```

```c
extern NSNotificationName const NSUndoManagerDidOpenUndoGroupNotification;
```

## Discussion

This notification originates in the implementation of the [`beginUndoGrouping()`](../../undomanager/beginundogrouping%28%29.md) method.

The notification object is the `NSUndoManager` object. This notification doesn’t contain a `userInfo` dictionary.

The system posts this notification on the actor, thread, or dispatch queue that calls [`beginUndoGrouping()`](../../undomanager/beginundogrouping%28%29.md).

## See Also

### Working with notifications
- [static let NSUndoManagerWillUndoChange: NSNotification.Name](./nsundomanagerwillundochange.md)
  Posted just before an undo manager performs an undo operation.
- [static let NSUndoManagerDidUndoChange: NSNotification.Name](./nsundomanagerdidundochange.md)
  Posted just after an undo manager performs an undo operation.
- [static let NSUndoManagerWillRedoChange: NSNotification.Name](./nsundomanagerwillredochange.md)
  Posted just before an undo manager performs a redo operation.
- [static let NSUndoManagerDidRedoChange: NSNotification.Name](./nsundomanagerdidredochange.md)
  Posted just after an undo manager performs a redo operation.
- [static let NSUndoManagerCheckpoint: NSNotification.Name](./nsundomanagercheckpoint.md)
  Posted whenever an undo manager opens or closes an undo group (except when it opens a top-level group) and when checking the redo stack.
- [static let NSUndoManagerWillCloseUndoGroup: NSNotification.Name](./nsundomanagerwillcloseundogroup.md)
  Posted before an undo manager closes an undo group.
- [static let NSUndoManagerDidCloseUndoGroup: NSNotification.Name](./nsundomanagerdidcloseundogroup.md)
  Posted after an undo manager closes an undo group.
- [let NSUndoManagerGroupIsDiscardableKey: String](../../nsundomanagergroupisdiscardablekey.md)
  A key, used in a notification’s user info, that indicates the undo group contains only discardable actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nsundomanagerdidopenundogroup)*