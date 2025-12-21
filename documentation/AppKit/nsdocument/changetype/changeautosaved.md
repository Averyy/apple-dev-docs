# NSDocument.ChangeType.changeAutosaved

**Framework**: AppKit  
**Kind**: case

The document’s contents have been autosaved.

**Availability**:
- macOS ?+

## Declaration

```swift
case changeAutosaved
```

#### Discussion

For example, [`saveToURL:ofType:forSaveOperation:error:`](nsdocument/savetourl:oftype:forsaveoperation:error:.md) passes this value for a successful [`NSAutosaveOperation`](nssaveoperationtype/nsautosaveoperation.md).

## See Also

- [NSDocument.ChangeType.changeDone](nsdocument/changetype/changedone.md)
  Increment change count.
- [NSDocument.ChangeType.changeUndone](nsdocument/changetype/changeundone.md)
  Decrement change count.
- [NSDocument.ChangeType.changeCleared](nsdocument/changetype/changecleared.md)
  Set change count to 0.
- [NSDocument.ChangeType.changeReadOtherContents](nsdocument/changetype/changereadothercontents.md)
  The document has been initialized with the contents of a file or file package other than the one whose location is in the `fileURL` property, and therefore can’t possibly be synchronized with its persistent representation.
- [NSDocument.ChangeType.changeRedone](nsdocument/changetype/changeredone.md)
  A single change has been redone.
- [NSDocument.ChangeType.changeDiscardable](nsdocument/changetype/changediscardable.md)
  A discardable change has been done.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/changetype/changeautosaved)*