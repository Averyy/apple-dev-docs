# canAsynchronouslyWrite(to:ofType:for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns whether the receiver can concurrently write to a file or file package located by a URL, that is formatted for a specific type, for a specific kind of save operation.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func canAsynchronouslyWrite(to url: URL, ofType typeName: String, for saveOperation: NSDocument.SaveOperationType) -> Bool
```

```objc
- (BOOL) canAsynchronouslyWriteToURL:(NSURL *) url ofType:(NSString *) typeName forSaveOperation:(NSSaveOperationType) saveOperation;
```

## Return Value

[`false`](../../Swift/false.md) by default; subclasses can override to return [`true`](../../Swift/true.md), thereby enabling asynchronous writing.

## Discussion

The default implementation of this method returns [`false`](../../Swift/false.md). You are strongly encouraged to override it and make it return [`true`](../../Swift/true.md), after making sure your overrides of document writing methods can be safely invoked on a non-main thread, and making sure that the [`unblockUserInteraction()`](./unblockuserinteraction%28%29.md) method is invoked at some appropriate time during writing.

## Parameters

- `url`: The location of the file or package to which the document is written.
- `typeName`: The string that identifies the document type.
- `saveOperation`: The type of save operation.

## See Also

### Writing the Document’s Content
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
- [func save(to: URL, ofType: String, for: NSDocument.SaveOperationType, delegate: Any?, didSave: Selector?, contextInfo: UnsafeMutableRawPointer?)](./save%28to,oftype,for,delegate,didsave,contextinfo%29.md)
  Saves the contents of the document to a file or file package located by a URL, that is formatted to a specified type, for a particular kind of save operation.
- [func save(to: URL, ofType: String, for: NSDocument.SaveOperationType, completionHandler: ((any Error)?) -> Void)](./save%28to,oftype,for,completionhandler%29.md)
  Saves the contents of the document to a file or file package located by a URL, that is formatted to a specified type, for a particular kind of save operation, and invokes the passed-in completion handler.
- [func fileAttributesToWrite(to: URL, ofType: String, for: NSDocument.SaveOperationType, originalContentsURL: URL?) throws -> [String : Any]](./fileattributestowrite%28to,oftype,for,originalcontentsurl%29.md)
  Returns the attributes to write to the file or file package at the specified URL, and targeting the specified type of save operation.
- [NSDocument.SaveOperationType](./saveoperationtype.md)
  Constants for specifying the type of document-save operation to perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/canasynchronouslywrite(to:oftype:for:))*