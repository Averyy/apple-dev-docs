# NSDocument.ChangeType.changeReadOtherContents

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

The document has been initialized with the contents of a file or file package other than the one whose location is in the `fileURL` property, and therefore can’t possibly be synchronized with its persistent representation.

**Availability**:
- macOS

## Declaration

```swift
case changeReadOtherContents
```

```c
NSChangeReadOtherContents
```

#### Discussion

For example, [`init(for:withContentsOf:ofType:)`](../init%28for,withcontentsof,oftype%29.md) passes this value when the two passed-in URLs are not equal to indicate that an autosaved document is being reopened.

## See Also

### Constants
- [NSDocument.ChangeType.changeDone](./changedone.md)
  Increment change count.
- [NSDocument.ChangeType.changeUndone](./changeundone.md)
  Decrement change count.
- [NSDocument.ChangeType.changeCleared](./changecleared.md)
  Set change count to 0.
- [NSDocument.ChangeType.changeAutosaved](./changeautosaved.md)
  The document’s contents have been autosaved.
- [NSDocument.ChangeType.changeRedone](./changeredone.md)
  A single change has been redone.
- [NSDocument.ChangeType.changeDiscardable](./changediscardable.md)
  A discardable change has been done.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/changetype/changereadothercontents)*