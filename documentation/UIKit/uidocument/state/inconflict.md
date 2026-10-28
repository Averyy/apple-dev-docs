# inConflict

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

Conflicts exist for the document file located at the file URL.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
static var inConflict: UIDocument.State { get }
```

```c
UIDocumentStateInConflict
```

## Discussion

You can access these conflicting document versions by calling the [`otherVersionsOfItem(at:)`](../../../Foundation/nsfileversion/otherversionsofitem%28at%29.md) class method of the [`NSFileVersion`](../../../Foundation/nsfileversion.md) class. This method returns an array of [`NSFileVersion`](../../../Foundation/nsfileversion.md) objects. You can then resolve the conflicting versions — for example, programmatically attempt to merge the versions or present the document versions to a person and request them to pick one.

## See Also

### Constants
- [static var normal: UIDocument.State](./normal.md)
  The document is open, editing is enabled, and there are no conflicts or errors associated with it.
- [static var closed: UIDocument.State](./closed.md)
  There was an error in reading the document.
- [static var savingError: UIDocument.State](./savingerror.md)
  There was an error in saving or reverting the document.
- [static var editingDisabled: UIDocument.State](./editingdisabled.md)
  The document is busy and it isn’t currently safe for user edits.
- [static var progressAvailable: UIDocument.State](./progressavailable.md)
  The document is being downloaded or uploaded and progress information is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/state/inconflict)*