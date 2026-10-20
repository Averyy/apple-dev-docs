# NSDocument.ChangeType.changeCleared

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

Set change count to 0.

**Availability**:
- macOS

## Declaration

```swift
case changeCleared
```

```c
NSChangeCleared
```

#### Discussion

The document has been synchronized with its file or file package. For example, [`saveToURL:ofType:forSaveOperation:error:`](../savetourl_oftype_forsaveoperation_error_.md) passes this value for a successful [`NSDocument.SaveOperationType.saveOperation`](../saveoperationtype/saveoperation.md) or [`NSDocument.SaveOperationType.saveAsOperation`](../saveoperationtype/saveasoperation.md). The [`revertToSaved(_:)`](../reverttosaved%28_%29.md) method does too.

## See Also

### Constants
- [NSDocument.ChangeType.changeDone](./changedone.md)
  Increment change count.
- [NSDocument.ChangeType.changeUndone](./changeundone.md)
  Decrement change count.
- [NSDocument.ChangeType.changeReadOtherContents](./changereadothercontents.md)
  The document has been initialized with the contents of a file or file package other than the one whose location is in the `fileURL` property, and therefore can’t possibly be synchronized with its persistent representation.
- [NSDocument.ChangeType.changeAutosaved](./changeautosaved.md)
  The document’s contents have been autosaved.
- [NSDocument.ChangeType.changeRedone](./changeredone.md)
  A single change has been redone.
- [NSDocument.ChangeType.changeDiscardable](./changediscardable.md)
  A discardable change has been done.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/changetype/changecleared)*