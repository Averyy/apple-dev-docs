# NSDocument.ChangeType

**Framework**: AppKit  
**Kind**: enum

Values that indicate a document’s edit status.

**Availability**:
- macOS ?+

## Declaration

```swift
enum ChangeType
```

#### Overview

These constants indicate how a document should operate on its change count and are passed to the [`updateChangeCount(_:)`](nsdocument/updatechangecount(_:).md) method.

## Topics

### Constants
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
- [NSDocument.ChangeType.changeDiscardable](nsdocument/changetype/changediscardable.md)
  A discardable change has been done.
### Initializers
- [init?(rawValue: UInt)](nsdocument/changetype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func updateChangeCount(withToken: Any, for: NSDocument.SaveOperationType)](nsdocument/updatechangecount(withtoken:for:).md)
  Updates the document’s change count settings after a successful save operation.
- [func updateChangeCount(NSDocument.ChangeType)](nsdocument/updatechangecount(_:).md)
  Updates the receiver’s change count according to the given change type.
- [func changeCountToken(for: NSDocument.SaveOperationType) -> Any](nsdocument/changecounttoken(for:).md)
  Returns an object that encapsulates the current record of document changes at the beginning of a save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/changetype)*