# save(to:ofType:for:completionHandler:)

**Framework**: AppKit  
**Kind**: method

Saves the contents of the document to a file or file package located by a URL, that is formatted to a specified type, for a particular kind of save operation, and invokes the passed-in completion handler.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func save(to url: URL, ofType typeName: String, for saveOperation: NSDocument.SaveOperationType) async throws
```

#### Discussion

The default implementation of this method invokes [`canAsynchronouslyWrite(to:ofType:for:)`](nsdocument/canasynchronouslywrite(to:oftype:for:).md). If writing can’t be done concurrently, it invokes [`writeSafely(to:ofType:for:)`](nsdocument/writesafely(to:oftype:for:).md) on the main thread thread. If writing can be done concurrently, it invokes that method on a different thread, but blocks the main thread until something invokes [`unblockUserInteraction()`](nsdocument/unblockuserinteraction().md). Either way, if [`writeSafely(to:ofType:for:)`](nsdocument/writesafely(to:oftype:for:).md) returns [`true`](https://developer.apple.com/documentation/swift/true), it updates the values in the [`fileModificationDate`](nsdocument/filemodificationdate.md), [`fileType`](nsdocument/filetype.md), [`fileURL`](nsdocument/fileurl.md), and [`autosavedContentsFileURL`](nsdocument/autosavedcontentsfileurl.md) properties and calls the [`updateChangeCount(_:)`](nsdocument/updatechangecount(_:).md) method as appropriate on the main thread. It also updates information that [`save(withDelegate:didSave:contextInfo:)`](nsdocument/save(withdelegate:didsave:contextinfo:).md) uses to check for modification, renaming, moving, deleting, and trashing of open documents, and deletes autosaved contents files when they have become obsolete. You can override this method to do things that need to be done before or after any save operation but be sure to invoke `super`.

For backward binary compatibility with OS X v10.6 and earlier, the default implementation of this method instead invokes [`saveToURL:ofType:forSaveOperation:error:`](nsdocument/savetourl:oftype:forsaveoperation:error:.md) if that method is overridden and this one is not, and it passes any error to the completion handler.

## Parameters

- `url`: The location to which the document contents are written.
- `typeName`: The document type.
- `saveOperation`: The type of save operation.
- `completionHandler`: The block takes one argument:

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
- [func save(to: URL, ofType: String, for: NSDocument.SaveOperationType, delegate: Any?, didSave: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsdocument/save(to:oftype:for:delegate:didsave:contextinfo:).md)
  Saves the contents of the document to a file or file package located by a URL, that is formatted to a specified type, for a particular kind of save operation.
- [func fileAttributesToWrite(to: URL, ofType: String, for: NSDocument.SaveOperationType, originalContentsURL: URL?) throws -> [String : Any]](nsdocument/fileattributestowrite(to:oftype:for:originalcontentsurl:).md)
  Returns the attributes to write to the file or file package at the specified URL, and targeting the specified type of save operation.
- [NSDocument.SaveOperationType](nsdocument/saveoperationtype.md)
  Constants for specifying the type of document-save operation to perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/save(to:oftype:for:completionhandler:))*