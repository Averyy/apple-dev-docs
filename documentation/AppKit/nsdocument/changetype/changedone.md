# NSDocument.ChangeType.changeDone

**Framework**: AppKit  
**Kind**: case

Increment change count.

**Availability**:
- macOS ?+

## Declaration

```swift
case changeDone
```

#### Discussion

Pass this value to the [`updateChangeCount(_:)`](nsdocument/updatechangecount(_:).md) method to indicate that a single change has been done. For example, the built-in undo support in the [`NSDocument`](nsdocument.md) class passes this value whenever a document receives an [`NSUndoManagerDidCloseUndoGroup`](https://developer.apple.com/documentation/Foundation/NSNotification/Name-swift.struct/NSUndoManagerDidCloseUndoGroup) notification from its own undo manager.

## See Also

- [NSDocument.ChangeType.changeUndone](nsdocument/changetype/changeundone.md)
  Decrement change count.
- [NSDocument.ChangeType.changeCleared](nsdocument/changetype/changecleared.md)
  Set change count to 0.
- [NSDocument.ChangeType.changeReadOtherContents](nsdocument/changetype/changereadothercontents.md)
  The document has been initialized with the contents of a file or file package other than the one whose location is in the `fileURL` property, and therefore can’t possibly be synchronized with its persistent representation.
- [NSDocument.ChangeType.changeAutosaved](nsdocument/changetype/changeautosaved.md)
  The document’s contents have been autosaved.
- [NSDocument.ChangeType.changeRedone](nsdocument/changetype/changeredone.md)
  A single change has been redone.
- [NSDocument.ChangeType.changeDiscardable](nsdocument/changetype/changediscardable.md)
  A discardable change has been done.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/changetype/changedone)*