# changeCountToken(for:)

**Framework**: UIKit  
**Kind**: method

Returns a change token for a specific save operation.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func changeCountToken(for saveOperation: UIDocument.SaveOperation) -> Any
```

#### Return Value

An object to use as a change-count token.

#### Discussion

To get autosaving capabilities for your documents, you must implement change tracking. Typically you do this by using an [`UndoManager`](https://developer.apple.com/documentation/Foundation/UndoManager) object (assigned to [`undoManager`](uidocument/undomanager.md) property) to register changes or by calling the [`updateChangeCount(_:)`](uidocument/updatechangecount(_:).md) method every time the user makes a change; UIKit then automatically determines whether there are unsaved changes and returns the proper value from [`hasUnsavedChanges`](uidocument/hasunsavedchanges.md). If you take neither of these approaches (and you want the autosaving feature), you must implement this method as well as [`updateChangeCount(withToken:for:)`](uidocument/updatechangecount(withtoken:for:).md) and [`hasUnsavedChanges`](uidocument/hasunsavedchanges.md).

You implement this particular method to return a change-count token that UIKit uses to encapsulate the history of document changes for a particular save operation. The token can be any object that represents the current change state of the document. This method is called at the start of the default implementation of the [`save(to:for:completionHandler:)`](uidocument/save(to:for:completionhandler:).md) method. At the end of this default implementation, it calls the [`updateChangeCount(withToken:for:)`](uidocument/updatechangecount(withtoken:for:).md) method, passing in the change-count token. You implement the latter method to compare the token with the one returned earlier; by doing so, you can determine if the document has acquired new unsaved changes between the start and end of an asynchronous write operation. You can then return the proper value from your override of [`hasUnsavedChanges`](uidocument/hasunsavedchanges.md).

## Parameters

- `saveOperation`: A constant that indicates whether the save operation is writing a new file or overwriting an existing one. See   for descriptions of these constants.

## See Also

- [var hasUnsavedChanges: Bool](uidocument/hasunsavedchanges.md)
  A Boolean value that indicates whether the document has any unsaved changes.
- [func updateChangeCount(UIDocument.ChangeKind)](uidocument/updatechangecount(_:).md)
  Updates the change counter by indicating the kind of change.
- [var undoManager: UndoManager!](uidocument/undomanager.md)
  The undo manager for the document.
- [func updateChangeCount(withToken: Any, for: UIDocument.SaveOperation)](uidocument/updatechangecount(withtoken:for:).md)
  Updates the change count with reference to a change-count token passed in by UIKit.
- [func autosave(completionHandler: ((Bool) -> Void)?)](uidocument/autosave(completionhandler:).md)
  Initiates automatic saving of documents with unsaved changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/changecounttoken(for:))*