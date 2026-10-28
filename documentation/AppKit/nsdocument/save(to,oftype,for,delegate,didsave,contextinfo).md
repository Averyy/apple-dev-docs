# save(to:ofType:for:delegate:didSave:contextInfo:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Saves the contents of the document to a file or file package located by a URL, that is formatted to a specified type, for a particular kind of save operation.

**Availability**:
- macOS

## Declaration

```swift
func save(to url: URL, ofType typeName: String, for saveOperation: NSDocument.SaveOperationType, delegate: Any?, didSave didSaveSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)
```

```objc
- (void) saveToURL:(NSURL *) url ofType:(NSString *) typeName forSaveOperation:(NSSaveOperationType) saveOperation delegate:(id) delegate didSaveSelector:(SEL) didSaveSelector contextInfo:(void *) contextInfo;
```

## Discussion

When saving is completed, regardless of success or failure, the method sends the message selected by `didSaveSelector` to the `delegate`, with the `contextInfo` as the last argument. The method selected by `didSaveSelector` must have the same signature as:

```objc
- (void)document:(NSDocument *)document didSave:(BOOL)didSaveSuccessfully  contextInfo:(void  *)contextInfo;
```

The default implementation of this method invokes `[self saveToURL:absoluteURL ofType:typeName forSaveOperation:saveOperation error:&anError]` and, if [`false`](../../Swift/false.md) is returned, presents the error to the user in a document-modal panel before messaging the delegate.

## Parameters

- `url`: The location of the file or file package to which the document contents are saved.
- `typeName`: The string that identifies the document type.
- `saveOperation`: The type of save operation.
- `delegate`: The delegate to which the selector message is sent.
- `didSaveSelector`: The selector of the message sent to the delegate.
- `contextInfo`: Object passed with the callback to provide any additional context information.

## See Also

### Writing the Document’s Content
- [func canAsynchronouslyWrite(to: URL, ofType: String, for: NSDocument.SaveOperationType) -> Bool](./canasynchronouslywrite%28to,oftype,for%29.md)
  Returns whether the receiver can concurrently write to a file or file package located by a URL, that is formatted for a specific type, for a specific kind of save operation.
- [func unblockUserInteraction()](./unblockuserinteraction%28%29.md)
  Unblocks the main thread during asynchronous saving.
- [func write(to: URL, ofType: String) throws](./write%28to,oftype%29.md)
  Writes the contents of the document to a file or file package located by a URL, that is formatted to a specified type.
- [func writeSafely(to: URL, ofType: String, for: NSDocument.SaveOperationType) throws](./writesafely%28to,oftype,for%29.md)
  Writes the contents of the document to a file or file package located by a URL.
- [func fileWrapper(ofType: String) throws -> FileWrapper](./filewrapper%28oftype%29.md)
  Creates and returns a file wrapper that contains the contents of the document, formatted to the specified type.
- [func data(ofType: String) throws -> Data](./data%28oftype%29.md)
  Creates and returns a data object that contains the contents of the document, formatted to a specified type.
- [func write(to: URL, ofType: String, for: NSDocument.SaveOperationType, originalContentsURL: URL?) throws](./write%28to,oftype,for,originalcontentsurl%29.md)
  Writes the contents of the document to a file or file package located by a URL.
- [func save(to: URL, ofType: String, for: NSDocument.SaveOperationType, completionHandler: ((any Error)?) -> Void)](./save%28to,oftype,for,completionhandler%29.md)
  Saves the contents of the document to a file or file package located by a URL, that is formatted to a specified type, for a particular kind of save operation, and invokes the passed-in completion handler.
- [func fileAttributesToWrite(to: URL, ofType: String, for: NSDocument.SaveOperationType, originalContentsURL: URL?) throws -> [String : Any]](./fileattributestowrite%28to,oftype,for,originalcontentsurl%29.md)
  Returns the attributes to write to the file or file package at the specified URL, and targeting the specified type of save operation.
- [NSDocument.SaveOperationType](./saveoperationtype.md)
  Constants for specifying the type of document-save operation to perform.
### Related Documentation
- [- saveToURL:ofType:forSaveOperation:error:](./savetourl_oftype_forsaveoperation_error_.md)
  Saves the contents of the document to a file or file package located by a URL, formatted to a specified type, for a particular kind of save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/save(to:oftype:for:delegate:didsave:contextinfo:))*