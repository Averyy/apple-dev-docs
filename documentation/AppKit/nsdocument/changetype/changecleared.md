# NSDocument.ChangeType.changeCleared

**Framework**: AppKit  
**Kind**: case

Set change count to 0.

**Availability**:
- macOS ?+

## Declaration

```swift
case changeCleared
```

#### Discussion

The document has been synchronized with its file or file package. For example, [`saveToURL:ofType:forSaveOperation:error:`](nsdocument/savetourl:oftype:forsaveoperation:error:.md) passes this value for a successful [`NSDocument.SaveOperationType.saveOperation`](nsdocument/saveoperationtype/saveoperation.md) or [`NSDocument.SaveOperationType.saveAsOperation`](nsdocument/saveoperationtype/saveasoperation.md). The [`revertToSaved(_:)`](nsdocument/reverttosaved(_:).md) method does too.

## See Also

- [NSDocument.ChangeType.changeDone](nsdocument/changetype/changedone.md)
  Increment change count.
- [NSDocument.ChangeType.changeUndone](nsdocument/changetype/changeundone.md)
  Decrement change count.
- [NSDocument.ChangeType.changeReadOtherContents](nsdocument/changetype/changereadothercontents.md)
  The document has been initialized with the contents of a file or file package other than the one whose location is in the `fileURL` property, and therefore can’t possibly be synchronized with its persistent representation.
- [NSDocument.ChangeType.changeAutosaved](nsdocument/changetype/changeautosaved.md)
  The document’s contents have been autosaved.
- [NSDocument.ChangeType.changeRedone](nsdocument/changetype/changeredone.md)
  A single change has been redone.
- [NSDocument.ChangeType.changeDiscardable](nsdocument/changetype/changediscardable.md)
  A discardable change has been done.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/changetype/changecleared)*