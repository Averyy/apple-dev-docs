# updateChangeCount(withToken:for:)

**Framework**: AppKit  
**Kind**: method

Updates the document’s change count settings after a successful save operation.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func updateChangeCount(withToken changeCountToken: Any, for saveOperation: NSDocument.SaveOperationType)
```

#### Discussion

This method updates the values in the [`isDocumentEdited`](nsdocument/isdocumentedited.md) and [`hasUnautosavedChanges`](nsdocument/hasunautosavedchanges.md) properties. For example, [`save(to:ofType:for:completionHandler:)`](nsdocument/save(to:oftype:for:completionhandler:).md) invokes this method, on the main thread, when it is done saving. The default implementation of this method also sends all of the document’s window controllers [`setDocumentEdited(_:)`](nswindowcontroller/setdocumentedited(_:).md) messages when appropriate.

## Parameters

- `changeCountToken`: An object encapsulating the document changes, returned from  .
- `saveOperation`: The type of save operation.

## See Also

- [func updateChangeCount(NSDocument.ChangeType)](nsdocument/updatechangecount(_:).md)
  Updates the receiver’s change count according to the given change type.
- [NSDocument.ChangeType](nsdocument/changetype.md)
  Values that indicate a document’s edit status.
- [func changeCountToken(for: NSDocument.SaveOperationType) -> Any](nsdocument/changecounttoken(for:).md)
  Returns an object that encapsulates the current record of document changes at the beginning of a save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/updatechangecount(withtoken:for:))*