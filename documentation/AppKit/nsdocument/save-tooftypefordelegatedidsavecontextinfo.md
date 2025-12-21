# save(to:ofType:for:delegate:didSave:contextInfo:)

**Framework**: AppKit  
**Kind**: method

Saves the contents of the document to a file or file package located by a URL, that is formatted to a specified type, for a particular kind of save operation.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func save(to url: URL, ofType typeName: String, for saveOperation: NSDocument.SaveOperationType, delegate: Any?, didSave didSaveSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)
```

#### Discussion

When saving is completed, regardless of success or failure, the method sends the message selected by `didSaveSelector` to the `delegate`, with the `contextInfo` as the last argument. The method selected by `didSaveSelector` must have the same signature as:

```objc
- (void)document:(NSDocument *)document didSave:(BOOL)didSaveSuccessfully  contextInfo:(void  *)contextInfo;
```

The default implementation of this method invokes `[self saveToURL:absoluteURL ofType:typeName forSaveOperation:saveOperation error:&anError]` and, if [`false`](https://developer.apple.com/documentation/Swift/false) is returned, presents the error to the user in a document-modal panel before messaging the delegate.

## Parameters

- `url`: The location of the file or file package to which the document contents are saved.
- `typeName`: The string that identifies the document type.
- `saveOperation`: The type of save operation.
- `delegate`: The delegate to which the selector message is sent.
- `didSaveSelector`: The selector of the message sent to the delegate.
- `contextInfo`: Object passed with the callback to provide any additional context information.

## See Also

- [func canAsynchronouslyWrite(to: URL, ofType: String, for: NSDocument.SaveOperationType) -> Bool](nsdocument/canasynchronouslywrite(to:oftype:for:).md)
  Returns whether the receiver can concurrently write to a file or file package located by a URL, that is formatted for a specific type, for a specific kind of save operation.
- [func unblockUserInteraction()](nsdocument/unblockuserinteraction.md)
  Unblocks the main thread during asynchronous saving.
- [func write(to: URL, ofType: String) throws](nsdocument/write(to:oftype:).md)
  Writes the contents of the document to a file or file package located by a URL, that is formatted to a specified type.
- [func writeSafely(to: URL, ofType: String, for: NSDocument.SaveOperationType) throws](nsdocument/writesafely(to:oftype:for:).md)
  Writes the contents of the document to a file or file package located by a URL.
- [func fileWrapper(ofType: String) throws -> FileWrapper](nsdocument/filewrapper(oftype:).md)
  Creates and returns a file wrapper that contains the contents of the document, formatted to the specified type.
- [func data(ofType: String) throws -> Data](nsdocument/data(oftype:).md)
  Creates and returns a data object that contains the contents of the document, formatted to a specified type.
- [func write(to: URL, ofType: String, for: NSDocument.SaveOperationType, originalContentsURL: URL?) throws](nsdocument/write(to:oftype:for:originalcontentsurl:).md)
  Writes the contents of the document to a file or file package located by a URL.
- [func save(to: URL, ofType: String, for: NSDocument.SaveOperationType, completionHandler: ((any Error)?) -> Void)](nsdocument/save(to:oftype:for:completionhandler:).md)
  Saves the contents of the document to a file or file package located by a URL, that is formatted to a specified type, for a particular kind of save operation, and invokes the passed-in completion handler.
- [func fileAttributesToWrite(to: URL, ofType: String, for: NSDocument.SaveOperationType, originalContentsURL: URL?) throws -> [String : Any]](nsdocument/fileattributestowrite(to:oftype:for:originalcontentsurl:).md)
  Returns the attributes to write to the file or file package at the specified URL, and targeting the specified type of save operation.
- [NSDocument.SaveOperationType](nsdocument/saveoperationtype.md)
  Constants for specifying the type of document-save operation to perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/save(to:oftype:for:delegate:didsave:contextinfo:))*