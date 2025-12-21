# NSDocument.ChangeType.changeReadOtherContents

**Framework**: AppKit  
**Kind**: case

The document has been initialized with the contents of a file or file package other than the one whose location is in the `fileURL` property, and therefore can’t possibly be synchronized with its persistent representation.

**Availability**:
- macOS ?+

## Declaration

```swift
case changeReadOtherContents
```

#### Discussion

For example, [`init(for:withContentsOf:ofType:)`](nsdocument/init(for:withcontentsof:oftype:).md) passes this value when the two passed-in URLs are not equal to indicate that an autosaved document is being reopened.

## See Also

- [NSDocument.ChangeType.changeDone](nsdocument/changetype/changedone.md)
  Increment change count.
- [NSDocument.ChangeType.changeUndone](nsdocument/changetype/changeundone.md)
  Decrement change count.
- [NSDocument.ChangeType.changeCleared](nsdocument/changetype/changecleared.md)
  Set change count to 0.
- [NSDocument.ChangeType.changeAutosaved](nsdocument/changetype/changeautosaved.md)
  The document’s contents have been autosaved.
- [NSDocument.ChangeType.changeRedone](nsdocument/changetype/changeredone.md)
  A single change has been redone.
- [NSDocument.ChangeType.changeDiscardable](nsdocument/changetype/changediscardable.md)
  A discardable change has been done.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/changetype/changereadothercontents)*