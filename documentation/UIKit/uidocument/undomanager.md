# undoManager

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (strong, null_resettable) NSUndoManager * undoManager;
```

## Discussion

This property holds the document’s undo manager (an [`UndoManager`](../../Foundation/undomanager.md) object). Accessing this property lazily creates a default undo manager if a custom undo manager hasn’t been set.

The undo manager for the document is registered as an observer of various [`UndoManager`](../../Foundation/undomanager.md) notifications so that it can call [`updateChangeCount(_:)`](./updatechangecount%28_%29.md) as the user makes undoable changes to the document. When a subclass sets this property and implements registers changes with it, it doesn’t need to call [`updateChangeCount(_:)`](./updatechangecount%28_%29.md) directly or (more rarely) override [`hasUnsavedChanges`](./hasunsavedchanges.md).

## See Also

### Tracking changes and autosaving
- [var hasUnsavedChanges: Bool](./hasunsavedchanges.md)
  A Boolean value that indicates whether the document has any unsaved changes.
- [func updateChangeCount(UIDocument.ChangeKind)](./updatechangecount%28_%29.md)
  Updates the change counter by indicating the kind of change.
- [func changeCountToken(for: UIDocument.SaveOperation) -> Any](./changecounttoken%28for%29.md)
  Returns a change token for a specific save operation.
- [func updateChangeCount(withToken: Any, for: UIDocument.SaveOperation)](./updatechangecount%28withtoken,for%29.md)
  Updates the change count with reference to a change-count token passed in by UIKit.
- [func autosave(completionHandler: ((Bool) -> Void)?)](./autosave%28completionhandler%29.md)
  Initiates automatic saving of documents with unsaved changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/undomanager)*