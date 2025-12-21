# updateChangeCount(_:)

**Framework**: UIKit  
**Kind**: method

Updates the change counter by indicating the kind of change.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func updateChangeCount(_ change: UIDocument.ChangeKind)
```

#### Discussion

Calling this method can affect the value returned by [`hasUnsavedChanges`](uidocument/hasunsavedchanges.md). You shouldn’t need to call method this if you access an [`UndoManager`](https://developer.apple.com/documentation/Foundation/UndoManager) object from the [`undoManager`](uidocument/undomanager.md) property (or assign a custom one to it) and register changes with the undo manager.

## Parameters

- `change`: A constant that indicates whether a change has been made, cleared, undone, or redone. See   for more information.

## See Also

- [var hasUnsavedChanges: Bool](uidocument/hasunsavedchanges.md)
  A Boolean value that indicates whether the document has any unsaved changes.
- [var undoManager: UndoManager!](uidocument/undomanager.md)
  The undo manager for the document.
- [func changeCountToken(for: UIDocument.SaveOperation) -> Any](uidocument/changecounttoken(for:).md)
  Returns a change token for a specific save operation.
- [func updateChangeCount(withToken: Any, for: UIDocument.SaveOperation)](uidocument/updatechangecount(withtoken:for:).md)
  Updates the change count with reference to a change-count token passed in by UIKit.
- [func autosave(completionHandler: ((Bool) -> Void)?)](uidocument/autosave(completionhandler:).md)
  Initiates automatic saving of documents with unsaved changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/updatechangecount(_:))*