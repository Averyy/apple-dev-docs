# editingDisabled

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The document is busy and it isn’t currently safe for user edits.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
static var editingDisabled: UIDocument.State { get }
```

```c
UIDocumentStateEditingDisabled
```

#### Discussion

This state is set just before [`UIDocument`](../../uidocument.md) calls the [`disableEditing()`](../disableediting%28%29.md) method. It calls [`enableEditing()`](../enableediting%28%29.md) when it becomes safe to edit again. [`UIDocument`](../../uidocument.md) also sets this state when an error prevents the reverting of a document.

## See Also

### Constants
- [static var normal: UIDocument.State](./normal.md)
  The document is open, editing is enabled, and there are no conflicts or errors associated with it.
- [static var closed: UIDocument.State](./closed.md)
  There was an error in reading the document.
- [static var inConflict: UIDocument.State](./inconflict.md)
  Conflicts exist for the document file located at the file URL.
- [static var savingError: UIDocument.State](./savingerror.md)
  There was an error in saving or reverting the document.
- [static var progressAvailable: UIDocument.State](./progressavailable.md)
  The document is being downloaded or uploaded and progress information is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/state/editingdisabled)*