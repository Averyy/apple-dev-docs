# NSDocument.ChangeType.changeAutosaved

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

The document’s contents have been autosaved.

**Availability**:
- macOS

## Declaration

```swift
case changeAutosaved
```

```c
NSChangeAutosaved
```

#### Discussion

For example, [`saveToURL:ofType:forSaveOperation:error:`](../savetourl_oftype_forsaveoperation_error_.md) passes this value for a successful [`NSAutosaveOperation`](../../nssaveoperationtype/nsautosaveoperation.md).

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
- [NSDocument.ChangeType.changeRedone](./changeredone.md)
  A single change has been redone.
- [NSDocument.ChangeType.changeDiscardable](./changediscardable.md)
  A discardable change has been done.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/changetype/changeautosaved)*