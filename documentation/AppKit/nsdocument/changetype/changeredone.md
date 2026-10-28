# NSDocument.ChangeType.changeRedone

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

A single change has been redone.

**Availability**:
- macOS 10.5+

## Declaration

```swift
case changeRedone
```

```c
NSChangeRedone
```

## Discussion

For example, the built-in undo support of [`NSDocument`](../../nsdocument.md) passes this value whenever a document receives an [`NSUndoManagerDidRedoChange`](../../../Foundation/nsnotification/name-swift.struct/nsundomanagerdidredochange.md) from its own undo manager.

## See Also

### Constants
- [NSDocument.ChangeType.changeDone](./changedone.md)
  Increment change count.
- [NSDocument.ChangeType.changeUndone](./changeundone.md)
  Decrement change count.
- [NSDocument.ChangeType.changeCleared](./changecleared.md)
  Set change count to 0.
- [NSDocument.ChangeType.changeReadOtherContents](./changereadothercontents.md)
  The document has been initialized with the contents of a file or file package other than the one whose location is in the `fileURL` property, and therefore can’t possibly be synchronized with its persistent representation.
- [NSDocument.ChangeType.changeAutosaved](./changeautosaved.md)
  The document’s contents have been autosaved.
- [NSDocument.ChangeType.changeDiscardable](./changediscardable.md)
  A discardable change has been done.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/changetype/changeredone)*