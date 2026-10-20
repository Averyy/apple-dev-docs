# savingError

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

There was an error in saving or reverting the document.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
static var savingError: UIDocument.State { get }
```

```c
UIDocumentStateSavingError
```

## See Also

### Constants
- [static var normal: UIDocument.State](./normal.md)
  The document is open, editing is enabled, and there are no conflicts or errors associated with it.
- [static var closed: UIDocument.State](./closed.md)
  There was an error in reading the document.
- [static var inConflict: UIDocument.State](./inconflict.md)
  Conflicts exist for the document file located at the file URL.
- [static var editingDisabled: UIDocument.State](./editingdisabled.md)
  The document is busy and it isn’t currently safe for user edits.
- [static var progressAvailable: UIDocument.State](./progressavailable.md)
  The document is being downloaded or uploaded and progress information is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/state/savingerror)*