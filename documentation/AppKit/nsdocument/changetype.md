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
  Increment change count. Pass this value to the [`updateChangeCount(_:)`](nsdocument/updatechangecount(_:).md) method to indicate that a single change has been done. For example, the built-in undo support in the [`NSDocument`](nsdocument.md) class passes this value whenever a document receives an [`NSUndoManagerDidCloseUndoGroup`](https://developer.apple.com/documentation/foundation/nsnotification/name/1408817-nsundomanagerdidcloseundogroup) notification from its own undo manager.
- [NSDocument.ChangeType.changeUndone](nsdocument/changetype/changeundone.md)
  Decrement change count. A single change has been undone. For example, the built-in undo support of `NSDocument` passes this value whenever a document receives an [`NSUndoManagerDidUndoChange`](https://developer.apple.com/documentation/foundation/nsnotification/name/1410142-nsundomanagerdidundochange) from its own undo manager.
- [NSDocument.ChangeType.changeCleared](nsdocument/changetype/changecleared.md)
  Set change count to 0. The document has been synchronized with its file or file package. For example, [`saveToURL:ofType:forSaveOperation:error:`](nsdocument/savetourl:oftype:forsaveoperation:error:.md) passes this value for a successful [`NSDocument.SaveOperationType.saveOperation`](nsdocument/saveoperationtype/saveoperation.md) or [`NSDocument.SaveOperationType.saveAsOperation`](nsdocument/saveoperationtype/saveasoperation.md). The [`revertToSaved(_:)`](nsdocument/reverttosaved(_:).md) method does too.
- [NSDocument.ChangeType.changeReadOtherContents](nsdocument/changetype/changereadothercontents.md)
  The document has been initialized with the contents of a file or file package other than the one whose location is in the [`fileURL`](nsdocument/fileurl.md) property, and therefore can’t possibly be synchronized with its persistent representation. For example, [`init(for:withContentsOf:ofType:)`](nsdocument/init(for:withcontentsof:oftype:).md) passes this value when the two passed-in URLs are not equal to indicate that an autosaved document is being reopened.
- [NSDocument.ChangeType.changeAutosaved](nsdocument/changetype/changeautosaved.md)
  The document’s contents have been autosaved. For example, [`saveToURL:ofType:forSaveOperation:error:`](nsdocument/savetourl:oftype:forsaveoperation:error:.md) passes this value for a successful [`NSAutosaveOperation`](nssaveoperationtype/nsautosaveoperation.md).
- [NSDocument.ChangeType.changeRedone](nsdocument/changetype/changeredone.md)
  A single change has been redone. For example, the built-in undo support of `NSDocument` passes this value whenever a document receives an [`NSUndoManagerDidRedoChange`](https://developer.apple.com/documentation/foundation/nsnotification/name/1413579-nsundomanagerdidredochange) from its own undo manager.
- [NSDocument.ChangeType.changeDiscardable](nsdocument/changetype/changediscardable.md)
### Initializers
- [init?(rawValue: UInt)](nsdocument/changetype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func updateChangeCount(withToken: Any, for: NSDocument.SaveOperationType)](nsdocument/updatechangecount(withtoken:for:).md)
  Updates the document’s change count settings after a successful save operation.
- [func updateChangeCount(NSDocument.ChangeType)](nsdocument/updatechangecount(_:).md)
  Updates the receiver’s change count according to the given change type.
- [func changeCountToken(for: NSDocument.SaveOperationType) -> Any](nsdocument/changecounttoken(for:).md)
  Returns an object that encapsulates the current record of document changes at the beginning of a save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/changetype)*