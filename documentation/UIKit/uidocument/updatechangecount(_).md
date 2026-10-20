# updateChangeCount(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) updateChangeCount:(UIDocumentChangeKind) change;
```

#### Discussion

Calling this method can affect the value returned by [`hasUnsavedChanges`](./hasunsavedchanges.md). You shouldn’t need to call method this if you access an [`UndoManager`](../../Foundation/undomanager.md) object from the [`undoManager`](./undomanager.md) property (or assign a custom one to it) and register changes with the undo manager.

## Parameters

- `change`: A constant that indicates whether a change has been made, cleared, undone, or redone. See [`UIDocument.ChangeKind`](./changekind.md) for more information.

## See Also

### Tracking changes and autosaving
- [var hasUnsavedChanges: Bool](./hasunsavedchanges.md)
  A Boolean value that indicates whether the document has any unsaved changes.
- [var undoManager: UndoManager!](./undomanager.md)
  The undo manager for the document.
- [func changeCountToken(for: UIDocument.SaveOperation) -> Any](./changecounttoken%28for%29.md)
  Returns a change token for a specific save operation.
- [func updateChangeCount(withToken: Any, for: UIDocument.SaveOperation)](./updatechangecount%28withtoken,for%29.md)
  Updates the change count with reference to a change-count token passed in by UIKit.
- [func autosave(completionHandler: ((Bool) -> Void)?)](./autosave%28completionhandler%29.md)
  Initiates automatic saving of documents with unsaved changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/updatechangecount(_:))*