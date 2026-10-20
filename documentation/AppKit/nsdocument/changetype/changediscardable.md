# NSDocument.ChangeType.changeDiscardable

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

A discardable change has been done.

**Availability**:
- macOS 10.7+

## Declaration

```swift
case changeDiscardable
```

```c
NSChangeDiscardable
```

#### Discussion

Discardable changes cause the document to be edited. In a locked document, for example, discardable changes may be thrown away instead of prompting the user to save them. Combine this value with the appropriate kind of change, [`NSDocument.ChangeType.changeDone`](./changedone.md), [`NSDocument.ChangeType.changeUndone`](./changeundone.md), or [`NSDocument.ChangeType.changeRedone`](./changeredone.md), using the C bitwise OR operator. For example, a discardable change is `NSChangeDone | NSChangeDiscardable`.

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
- [NSDocument.ChangeType.changeRedone](./changeredone.md)
  A single change has been redone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/changetype/changediscardable)*