# NSUndoManagerGroupIsDiscardableKey

**Framework**: Foundation  
**Kind**: var

A key, used in a notification’s user info, that indicates the undo group contains only discardable actions.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let NSUndoManagerGroupIsDiscardableKey: String
```

#### Discussion

The key has a corresponding value of [`true`](https://developer.apple.com/documentation/swift/true), wrapped as a Boolean [`NSNumber`](nsnumber.md) object, if the undo group as a whole is discardable.

## See Also

- [static let NSUndoManagerCheckpoint: NSNotification.Name](nsnotification/name-swift.struct/nsundomanagercheckpoint.md)
  Posted whenever an undo manager opens or closes an undo group (except when it opens a top-level group) and when checking the redo stack.
- [static let NSUndoManagerDidOpenUndoGroup: NSNotification.Name](nsnotification/name-swift.struct/nsundomanagerdidopenundogroup.md)
  Posted whenever an undo manager opens an undo group.
- [static let NSUndoManagerDidRedoChange: NSNotification.Name](nsnotification/name-swift.struct/nsundomanagerdidredochange.md)
  Posted just after an undo manager performs a redo operation.
- [static let NSUndoManagerDidUndoChange: NSNotification.Name](nsnotification/name-swift.struct/nsundomanagerdidundochange.md)
  Posted just after an undo manager performs an undo operation.
- [static let NSUndoManagerWillCloseUndoGroup: NSNotification.Name](nsnotification/name-swift.struct/nsundomanagerwillcloseundogroup.md)
  Posted before an undo manager closes an undo group.
- [static let NSUndoManagerDidCloseUndoGroup: NSNotification.Name](nsnotification/name-swift.struct/nsundomanagerdidcloseundogroup.md)
  Posted after an undo manager closes an undo group.
- [static let NSUndoManagerWillRedoChange: NSNotification.Name](nsnotification/name-swift.struct/nsundomanagerwillredochange.md)
  Posted just before an undo manager performs a redo operation.
- [static let NSUndoManagerWillUndoChange: NSNotification.Name](nsnotification/name-swift.struct/nsundomanagerwillundochange.md)
  Posted just before an undo manager performs an undo operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsundomanagergroupisdiscardablekey)*