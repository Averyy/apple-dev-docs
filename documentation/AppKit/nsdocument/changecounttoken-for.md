# changeCountToken(for:)

**Framework**: AppKit  
**Kind**: method

Returns an object that encapsulates the current record of document changes at the beginning of a save operation.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func changeCountToken(for saveOperation: NSDocument.SaveOperationType) -> Any
```

#### Return Value

An object encapsulating the document changes.

#### Discussion

The returned object is meant to be passed to [`updateChangeCount(withToken:for:)`](nsdocument/updatechangecount(withtoken:for:).md) at the end of the save operation. For example, [`save(to:ofType:for:completionHandler:)`](nsdocument/save(to:oftype:for:completionhandler:).md) invokes this method, on the main thread, before it does any actual saving. This method facilitates asynchronous saving, during which a user can change a document while it is being saved.

## Parameters

- `saveOperation`: The type of save operation.

## See Also

- [func updateChangeCount(withToken: Any, for: NSDocument.SaveOperationType)](nsdocument/updatechangecount(withtoken:for:).md)
  Updates the document’s change count settings after a successful save operation.
- [func updateChangeCount(NSDocument.ChangeType)](nsdocument/updatechangecount(_:).md)
  Updates the receiver’s change count according to the given change type.
- [NSDocument.ChangeType](nsdocument/changetype.md)
  Values that indicate a document’s edit status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/changecounttoken(for:))*