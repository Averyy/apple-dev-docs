# updateChangeCount(withToken:for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Updates the document’s change count settings after a successful save operation.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func updateChangeCount(withToken changeCountToken: Any, for saveOperation: NSDocument.SaveOperationType)
```

```objc
- (void) updateChangeCountWithToken:(id) changeCountToken forSaveOperation:(NSSaveOperationType) saveOperation;
```

#### Discussion

This method updates the values in the [`isDocumentEdited`](./isdocumentedited.md) and [`hasUnautosavedChanges`](./hasunautosavedchanges.md) properties. For example, [`save(to:ofType:for:completionHandler:)`](./save%28to,oftype,for,completionhandler%29.md) invokes this method, on the main thread, when it is done saving. The default implementation of this method also sends all of the document’s window controllers [`setDocumentEdited(_:)`](../nswindowcontroller/setdocumentedited%28_%29.md) messages when appropriate.

## Parameters

- `changeCountToken`: An object encapsulating the document changes, returned from [`changeCountToken(for:)`](./changecounttoken%28for%29.md).
- `saveOperation`: The type of save operation.

## See Also

### Updating the Document Change Count
- [func updateChangeCount(NSDocument.ChangeType)](./updatechangecount%28_%29.md)
  Updates the receiver’s change count according to the given change type.
- [NSDocument.ChangeType](./changetype.md)
  Values that indicate a document’s edit status.
- [func changeCountToken(for: NSDocument.SaveOperationType) -> Any](./changecounttoken%28for%29.md)
  Returns an object that encapsulates the current record of document changes at the beginning of a save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/updatechangecount(withtoken:for:))*