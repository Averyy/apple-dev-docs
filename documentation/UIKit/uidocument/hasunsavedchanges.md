# hasUnsavedChanges

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the document has any unsaved changes.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var hasUnsavedChanges: Bool { get }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the document has unsaved changes, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The default implementation of [`autosave(completionHandler:)`](uidocument/autosave(completionhandler:).md) initiates a save if this property returns [`true`](https://developer.apple.com/documentation/swift/true). Typical subclasses don’t need to override [`hasUnsavedChanges`](uidocument/hasunsavedchanges.md). To implement change tracking, they should instead use an [`UndoManager`](https://developer.apple.com/documentation/Foundation/UndoManager) object (assigned to [`undoManager`](uidocument/undomanager.md)) to register changes or call [`updateChangeCount(_:)`](uidocument/updatechangecount(_:).md) every time the user makes a change; UIKit then automatically determines whether there are unsaved changes.

## See Also

- [func updateChangeCount(UIDocument.ChangeKind)](uidocument/updatechangecount(_:).md)
  Updates the change counter by indicating the kind of change.
- [var undoManager: UndoManager!](uidocument/undomanager.md)
  The undo manager for the document.
- [func changeCountToken(for: UIDocument.SaveOperation) -> Any](uidocument/changecounttoken(for:).md)
  Returns a change token for a specific save operation.
- [func updateChangeCount(withToken: Any, for: UIDocument.SaveOperation)](uidocument/updatechangecount(withtoken:for:).md)
  Updates the change count with reference to a change-count token passed in by UIKit.
- [func autosave(completionHandler: ((Bool) -> Void)?)](uidocument/autosave(completionhandler:).md)
  Initiates automatic saving of documents with unsaved changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/hasunsavedchanges)*