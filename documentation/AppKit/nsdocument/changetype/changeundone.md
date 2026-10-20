# NSDocument.ChangeType.changeUndone

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

Decrement change count.

**Availability**:
- macOS

## Declaration

```swift
case changeUndone
```

```c
NSChangeUndone
```

#### Discussion

A single change has been undone. For example, the built-in undo support of [`NSDocument`](../../nsdocument.md) passes this value whenever a document receives an [`NSUndoManagerDidUndoChange`](../../../Foundation/nsnotification/name-swift.struct/nsundomanagerdidundochange.md) from its own undo manager.

## See Also

### Constants
- [NSDocument.ChangeType.changeDone](./changedone.md)
  Increment change count.
- [NSDocument.ChangeType.changeCleared](./changecleared.md)
  Set change count to 0.
- [NSDocument.ChangeType.changeReadOtherContents](./changereadothercontents.md)
  The document has been initialized with the contents of a file or file package other than the one whose location is in the `fileURL` property, and therefore can’t possibly be synchronized with its persistent representation.
- [NSDocument.ChangeType.changeAutosaved](./changeautosaved.md)
  The document’s contents have been autosaved.
- [NSDocument.ChangeType.changeRedone](./changeredone.md)
  A single change has been redone.
- [NSDocument.ChangeType.changeDiscardable](./changediscardable.md)
  A discardable change has been done.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/changetype/changeundone)*