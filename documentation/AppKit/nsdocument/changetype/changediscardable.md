# NSDocument.ChangeType.changeDiscardable

**Framework**: AppKit  
**Kind**: case

A discardable change has been done.

**Availability**:
- macOS 10.7+

## Declaration

```swift
case changeDiscardable
```

#### Discussion

Discardable changes cause the document to be edited. In a locked document, for example, discardable changes may be thrown away instead of prompting the user to save them. Combine this value with the appropriate kind of change, [`NSDocument.ChangeType.changeDone`](nsdocument/changetype/changedone.md), [`NSDocument.ChangeType.changeUndone`](nsdocument/changetype/changeundone.md), or [`NSDocument.ChangeType.changeRedone`](nsdocument/changetype/changeredone.md), using the C bitwise OR operator. For example, a discardable change is `NSChangeDone | NSChangeDiscardable`.

## See Also

- [NSDocument.ChangeType.changeDone](nsdocument/changetype/changedone.md)
  Increment change count.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/changetype/changediscardable)*