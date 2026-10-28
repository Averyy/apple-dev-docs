# save(to:ofType:for:completionHandler:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Saves the contents of the document to a file or file package located by a URL, that is formatted to a specified type, for a particular kind of save operation, and invokes the passed-in completion handler.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func save(to url: URL, ofType typeName: String, for saveOperation: NSDocument.SaveOperationType, completionHandler: @escaping ((any Error)?) -> Void)
```

```swift
func save(to url: URL, ofType typeName: String, for saveOperation: NSDocument.SaveOperationType) async throws
```

```objc
- (void) saveToURL:(NSURL *) url ofType:(NSString *) typeName forSaveOperation:(NSSaveOperationType) saveOperation completionHandler:(void (^)(NSError *errorOrNil)) completionHandler;
```

## Discussion

The default implementation of this method invokes [`canAsynchronouslyWrite(to:ofType:for:)`](./canasynchronouslywrite%28to,oftype,for%29.md). If writing can’t be done concurrently, it invokes [`writeSafely(to:ofType:for:)`](./writesafely%28to,oftype,for%29.md) on the main thread thread. If writing can be done concurrently, it invokes that method on a different thread, but blocks the main thread until something invokes [`unblockUserInteraction()`](./unblockuserinteraction%28%29.md). Either way, if [`writeSafely(to:ofType:for:)`](./writesafely%28to,oftype,for%29.md) returns [`true`](../../Swift/true.md), it updates the values in the [`fileModificationDate`](./filemodificationdate.md), [`fileType`](./filetype.md), [`fileURL`](./fileurl.md), and [`autosavedContentsFileURL`](./autosavedcontentsfileurl.md) properties and calls the [`updateChangeCount(_:)`](./updatechangecount%28_%29.md) method as appropriate on the main thread. It also updates information that [`save(withDelegate:didSave:contextInfo:)`](./save%28withdelegate,didsave,contextinfo%29.md) uses to check for modification, renaming, moving, deleting, and trashing of open documents, and deletes autosaved contents files when they have become obsolete. You can override this method to do things that need to be done before or after any save operation but be sure to invoke `super`.

For backward binary compatibility with OS X v10.6 and earlier, the default implementation of this method instead invokes [`saveToURL:ofType:forSaveOperation:error:`](./savetourl_oftype_forsaveoperation_error_.md) if that method is overridden and this one is not, and it passes any error to the completion handler.

## Parameters

- `url`: The location to which the document contents are written.
- `typeName`: The document type.
- `saveOperation`: The type of save operation.
- `completionHandler`: The completion handler block object passed in to be invoked at some point in the future, perhaps after the method invocation has returned. The completion handler must be invoked on the main thread.

  The block takes one argument:

  - **`errorOrNil`**: If successful, pass a `nil` error. If not successful, pass an `NSError` object that encapsulates the reason why the document could not be saved.

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
- [func save(to: URL, ofType: String, for: NSDocument.SaveOperationType, delegate: Any?, didSave: Selector?, contextInfo: UnsafeMutableRawPointer?)](./save%28to,oftype,for,delegate,didsave,contextinfo%29.md)
  Saves the contents of the document to a file or file package located by a URL, that is formatted to a specified type, for a particular kind of save operation.
- [func fileAttributesToWrite(to: URL, ofType: String, for: NSDocument.SaveOperationType, originalContentsURL: URL?) throws -> [String : Any]](./fileattributestowrite%28to,oftype,for,originalcontentsurl%29.md)
  Returns the attributes to write to the file or file package at the specified URL, and targeting the specified type of save operation.
- [NSDocument.SaveOperationType](./saveoperationtype.md)
  Constants for specifying the type of document-save operation to perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/save(to:oftype:for:completionhandler:))*