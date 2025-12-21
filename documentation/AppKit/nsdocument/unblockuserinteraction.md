# unblockUserInteraction()

**Framework**: AppKit  
**Kind**: method

Unblocks the main thread during asynchronous saving.

**Availability**:
- macOS 10.7+

## Declaration

```swift
nonisolated
func unblockUserInteraction()
```

#### Discussion

If [`save(to:ofType:for:completionHandler:)`](nsdocument/save(to:oftype:for:completionhandler:).md) is writing on a non-main thread because [`canAsynchronouslyWrite(to:ofType:for:)`](nsdocument/canasynchronouslywrite(to:oftype:for:).md) has returned [`true`](https://developer.apple.com/documentation/Swift/true), but it is still blocking the main thread, this method unblocks the main thread. Otherwise, it does nothing. For example, the default implementation of [`fileWrapper(ofType:)`](nsdocument/filewrapper(oftype:).md) invokes this when it has created the [`FileWrapper`](https://developer.apple.com/documentation/Foundation/FileWrapper) object to return. Assuming that the `NSFileWrapper` is not mutated by subsequent user actions, it is effectively a “snapshot” of the document’s contents, and once it is created it is safe to resume handling user events on the main thread, even though some of those user events might change the document’s contents before the `NSFileWrapper` object has been safely written. You can invoke this method to make asynchronous saving actually asynchronous if you’ve overridden [`writeSafely(to:ofType:for:)`](nsdocument/writesafely(to:oftype:for:).md), [`write(to:ofType:for:originalContentsURL:)`](nsdocument/write(to:oftype:for:originalcontentsurl:).md), or [`write(to:ofType:)`](nsdocument/write(to:oftype:).md) in such a way that the invocation of this method done by the [`write(to:ofType:)`](nsdocument/write(to:oftype:).md) default implementation won’t happen during writing.

## See Also

- [func canAsynchronouslyWrite(to: URL, ofType: String, for: NSDocument.SaveOperationType) -> Bool](nsdocument/canasynchronouslywrite(to:oftype:for:).md)
  Returns whether the receiver can concurrently write to a file or file package located by a URL, that is formatted for a specific type, for a specific kind of save operation.
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
- [func save(to: URL, ofType: String, for: NSDocument.SaveOperationType, delegate: Any?, didSave: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsdocument/save(to:oftype:for:delegate:didsave:contextinfo:).md)
  Saves the contents of the document to a file or file package located by a URL, that is formatted to a specified type, for a particular kind of save operation.
- [func save(to: URL, ofType: String, for: NSDocument.SaveOperationType, completionHandler: ((any Error)?) -> Void)](nsdocument/save(to:oftype:for:completionhandler:).md)
  Saves the contents of the document to a file or file package located by a URL, that is formatted to a specified type, for a particular kind of save operation, and invokes the passed-in completion handler.
- [func fileAttributesToWrite(to: URL, ofType: String, for: NSDocument.SaveOperationType, originalContentsURL: URL?) throws -> [String : Any]](nsdocument/fileattributestowrite(to:oftype:for:originalcontentsurl:).md)
  Returns the attributes to write to the file or file package at the specified URL, and targeting the specified type of save operation.
- [NSDocument.SaveOperationType](nsdocument/saveoperationtype.md)
  Constants for specifying the type of document-save operation to perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/unblockuserinteraction())*