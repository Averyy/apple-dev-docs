# updateChangeCount(withToken:for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Updates the change count with reference to a change-count token passed in by UIKit.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func updateChangeCount(withToken changeCountToken: Any, for saveOperation: UIDocument.SaveOperation)
```

```objc
- (void) updateChangeCountWithToken:(id) changeCountToken forSaveOperation:(UIDocumentSaveOperation) saveOperation;
```

#### Discussion

To get autosaving capabilities for your documents, you must implement change tracking. Typically you do this by using an [`UndoManager`](../../Foundation/undomanager.md) object (assigned to [`undoManager`](./undomanager.md) property) to register changes or by calling the [`updateChangeCount(_:)`](./updatechangecount%28_%29.md) method every time the user makes a change; UIKit then automatically determines whether there are unsaved changes and returns the proper value from [`hasUnsavedChanges`](./hasunsavedchanges.md). If you take neither of these approaches (and you want the autosaving feature), you must implement this method as well as [`changeCountToken(for:)`](./changecounttoken%28for%29.md) and [`hasUnsavedChanges`](./hasunsavedchanges.md).

You implement the [`changeCountToken(for:)`](./changecounttoken%28for%29.md) method to return a change-count token that UIKit uses to encapsulate the history of document changes for a particular save operation. The token can be any object that represents the current change state of the document. This method is called at the start of the default implementation of the [`save(to:for:completionHandler:)`](./save%28to,for,completionhandler%29.md) method. At the end of this default implementation, [`UIDocument`](../uidocument.md) calls this method ([`updateChangeCount(withToken:for:)`](./updatechangecount%28withtoken,for%29.md)), passing in the change-count token. You implement this method to compare the token with the one returned earlier; by doing so, you can determine if the document has acquired new unsaved changes between the start and end of an asynchronous write operation. You can then return the proper value from your override of [`hasUnsavedChanges`](./hasunsavedchanges.md).

## Parameters

- `changeCountToken`: An object to use as a change-count token. `UIDocument` obtained this token earlier by calling [`changeCountToken(for:)`](./changecounttoken%28for%29.md).
- `saveOperation`: A constant that indicates whether the save operation is writing a new file or overwriting an existing one. See [`UIDocument.SaveOperation`](./saveoperation.md) for descriptions of these constants.

## See Also

### Tracking changes and autosaving
- [var hasUnsavedChanges: Bool](./hasunsavedchanges.md)
  A Boolean value that indicates whether the document has any unsaved changes.
- [func updateChangeCount(UIDocument.ChangeKind)](./updatechangecount%28_%29.md)
  Updates the change counter by indicating the kind of change.
- [var undoManager: UndoManager!](./undomanager.md)
  The undo manager for the document.
- [func changeCountToken(for: UIDocument.SaveOperation) -> Any](./changecounttoken%28for%29.md)
  Returns a change token for a specific save operation.
- [func autosave(completionHandler: ((Bool) -> Void)?)](./autosave%28completionhandler%29.md)
  Initiates automatic saving of documents with unsaved changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/updatechangecount(withtoken:for:))*