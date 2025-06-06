# autosave(completionHandler:)

**Framework**: UIKit  
**Kind**: method

Initiates automatic saving of documents with unsaved changes.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func autosave() async -> Bool
```

#### Discussion

[`UIDocument`](uidocument.md) periodically invokes this method to initiate a save operation if there are unsaved changes. You shouldn’t call this method directly. Subclasses can override it if they want to do special things with autosaving. The default implementation of this method invokes the [`hasUnsavedChanges`](uidocument/hasunsavedchanges.md) method and, if that returns [`true`](https://developer.apple.com/documentation/swift/true), it invokes the [`save(to:for:completionHandler:)`](uidocument/save(to:for:completionhandler:).md) method.

This method should only be invoked for period-based saves. You may invoke it with the `success` parameter of the completion-handler parameter set to [`false`](https://developer.apple.com/documentation/swift/false) and return; this makes it safe to not actually save when [`autosave(completionHandler:)`](uidocument/autosave(completionhandler:).md) is invoked. However, if you call [`save(to:for:completionHandler:)`](uidocument/save(to:for:completionhandler:).md), saving of document data must occur.

## Parameters

- `completionHandler`: The block is invoked on the calling queue.

## See Also

- [var hasUnsavedChanges: Bool](uidocument/hasunsavedchanges.md)
  A Boolean value that indicates whether the document has any unsaved changes.
- [func updateChangeCount(UIDocument.ChangeKind)](uidocument/updatechangecount(_:).md)
  Updates the change counter by indicating the kind of change.
- [var undoManager: UndoManager!](uidocument/undomanager.md)
  The undo manager for the document.
- [func changeCountToken(for: UIDocument.SaveOperation) -> Any](uidocument/changecounttoken(for:).md)
  Returns a change token for a specific save operation.
- [func updateChangeCount(withToken: Any, for: UIDocument.SaveOperation)](uidocument/updatechangecount(withtoken:for:).md)
  Updates the change count with reference to a change-count token passed in by UIKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/autosave(completionhandler:))*