# unblockUserInteraction()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Unblocks the main thread during asynchronous saving.

**Availability**:
- macOS 10.7+

## Declaration

```swift
nonisolated
func unblockUserInteraction()
```

```objc
- (void) unblockUserInteraction;
```

## Discussion

If [`save(to:ofType:for:completionHandler:)`](./save%28to,oftype,for,completionhandler%29.md) is writing on a non-main thread because [`canAsynchronouslyWrite(to:ofType:for:)`](./canasynchronouslywrite%28to,oftype,for%29.md) has returned [`true`](../../Swift/true.md), but it is still blocking the main thread, this method unblocks the main thread. Otherwise, it does nothing. For example, the default implementation of [`fileWrapper(ofType:)`](./filewrapper%28oftype%29.md) invokes this when it has created the [`FileWrapper`](../../Foundation/filewrapper.md) object to return. Assuming that the `NSFileWrapper` is not mutated by subsequent user actions, it is effectively a “snapshot” of the document’s contents, and once it is created it is safe to resume handling user events on the main thread, even though some of those user events might change the document’s contents before the `NSFileWrapper` object has been safely written. You can invoke this method to make asynchronous saving actually asynchronous if you’ve overridden [`writeSafely(to:ofType:for:)`](./writesafely%28to,oftype,for%29.md), [`write(to:ofType:for:originalContentsURL:)`](./write%28to,oftype,for,originalcontentsurl%29.md), or [`write(to:ofType:)`](./write%28to,oftype%29.md) in such a way that the invocation of this method done by the [`write(to:ofType:)`](./write%28to,oftype%29.md) default implementation won’t happen during writing.

## See Also

### Writing the Document’s Content
- [func canAsynchronouslyWrite(to: URL, ofType: String, for: NSDocument.SaveOperationType) -> Bool](./canasynchronouslywrite%28to,oftype,for%29.md)
  Returns whether the receiver can concurrently write to a file or file package located by a URL, that is formatted for a specific type, for a specific kind of save operation.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/unblockuserinteraction())*