# editingDisabled

**Framework**: UIKit  
**Kind**: property

The document is busy and it isn’t currently safe for user edits.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
static var editingDisabled: UIDocument.State { get }
```

#### Discussion

This state is set just before [`UIDocument`](uidocument.md) calls the [`disableEditing()`](uidocument/disableediting().md) method. It calls [`enableEditing()`](uidocument/enableediting().md) when it becomes safe to edit again. [`UIDocument`](uidocument.md) also sets this state when an error prevents the reverting of a document.

## See Also

- [static var normal: UIDocument.State](uidocument/state/normal.md)
  The document is open, editing is enabled, and there are no conflicts or errors associated with it.
- [static var closed: UIDocument.State](uidocument/state/closed.md)
  There was an error in reading the document.
- [static var inConflict: UIDocument.State](uidocument/state/inconflict.md)
  Conflicts exist for the document file located at the file URL.
- [static var savingError: UIDocument.State](uidocument/state/savingerror.md)
  There was an error in saving or reverting the document.
- [static var progressAvailable: UIDocument.State](uidocument/state/progressavailable.md)
  The document is being downloaded or uploaded and progress information is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/state/editingdisabled)*