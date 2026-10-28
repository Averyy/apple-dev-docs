# NSDocument.ChangeType

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Values that indicate a document’s edit status.

**Availability**:
- macOS

## Declaration

```swift
enum ChangeType
```

```c
enum NSDocumentChangeType : NSUInteger;
```

## Overview

These constants indicate how a document should operate on its change count and are passed to the [`updateChangeCount(_:)`](./updatechangecount%28_%29.md) method.

## Topics

### Constants
- [NSDocument.ChangeType.changeDone](./changetype/changedone.md)
  Increment change count.
- [NSDocument.ChangeType.changeUndone](./changetype/changeundone.md)
  Decrement change count.
- [NSDocument.ChangeType.changeCleared](./changetype/changecleared.md)
  Set change count to 0.
- [NSDocument.ChangeType.changeReadOtherContents](./changetype/changereadothercontents.md)
  The document has been initialized with the contents of a file or file package other than the one whose location is in the `fileURL` property, and therefore can’t possibly be synchronized with its persistent representation.
- [NSDocument.ChangeType.changeAutosaved](./changetype/changeautosaved.md)
  The document’s contents have been autosaved.
- [NSDocument.ChangeType.changeRedone](./changetype/changeredone.md)
  A single change has been redone.
- [NSDocument.ChangeType.changeDiscardable](./changetype/changediscardable.md)
  A discardable change has been done.
### Initializers
- [init?(rawValue: UInt)](./changetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Updating the Document Change Count
- [func updateChangeCount(withToken: Any, for: NSDocument.SaveOperationType)](./updatechangecount%28withtoken,for%29.md)
  Updates the document’s change count settings after a successful save operation.
- [func updateChangeCount(NSDocument.ChangeType)](./updatechangecount%28_%29.md)
  Updates the receiver’s change count according to the given change type.
- [func changeCountToken(for: NSDocument.SaveOperationType) -> Any](./changecounttoken%28for%29.md)
  Returns an object that encapsulates the current record of document changes at the beginning of a save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/changetype)*