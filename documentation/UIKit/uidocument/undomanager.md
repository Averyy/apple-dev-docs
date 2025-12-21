# undoManager

**Framework**: UIKit  
**Kind**: property

The undo manager for the document.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var undoManager: UndoManager! { get set }
```

#### Discussion

This property holds the document’s undo manager (an [`UndoManager`](https://developer.apple.com/documentation/Foundation/UndoManager) object). Accessing this property lazily creates a default undo manager if a custom undo manager hasn’t been set.

The undo manager for the document is registered as an observer of various [`UndoManager`](https://developer.apple.com/documentation/Foundation/UndoManager) notifications so that it can call [`updateChangeCount(_:)`](uidocument/updatechangecount(_:).md) as the user makes undoable changes to the document. When a subclass sets this property and implements registers changes with it, it doesn’t need to call [`updateChangeCount(_:)`](uidocument/updatechangecount(_:).md) directly or (more rarely) override [`hasUnsavedChanges`](uidocument/hasunsavedchanges.md).

## See Also

- [var hasUnsavedChanges: Bool](uidocument/hasunsavedchanges.md)
  A Boolean value that indicates whether the document has any unsaved changes.
- [func updateChangeCount(UIDocument.ChangeKind)](uidocument/updatechangecount(_:).md)
  Updates the change counter by indicating the kind of change.
- [func changeCountToken(for: UIDocument.SaveOperation) -> Any](uidocument/changecounttoken(for:).md)
  Returns a change token for a specific save operation.
- [func updateChangeCount(withToken: Any, for: UIDocument.SaveOperation)](uidocument/updatechangecount(withtoken:for:).md)
  Updates the change count with reference to a change-count token passed in by UIKit.
- [func autosave(completionHandler: ((Bool) -> Void)?)](uidocument/autosave(completionhandler:).md)
  Initiates automatic saving of documents with unsaved changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/undomanager)*