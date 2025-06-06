# NSDocument.SaveOperationType

**Framework**: AppKit  
**Kind**: enum

Constants for specifying the type of document-save operation to perform.

**Availability**:
- macOS ?+

## Declaration

```swift
enum SaveOperationType
```

#### Overview

These values are used with method parameters of type [`NSDocument.SaveOperationType`](nsdocument/saveoperationtype.md). Depending on the method, the save operation type can affect the title of the Save dialog and can affect which files are displayed in the dialog.

## Topics

### Constants
- [NSDocument.SaveOperationType.saveOperation](nsdocument/saveoperationtype/saveoperation.md)
  An operation that overwrites a document’s file or file package with the document’s contents.
- [NSDocument.SaveOperationType.saveAsOperation](nsdocument/saveoperationtype/saveasoperation.md)
  An operation that writes the document’s contents to a new location and updates the document to point to that location
- [NSDocument.SaveOperationType.saveToOperation](nsdocument/saveoperationtype/savetooperation.md)
  An operation that writes a copy of the document’s contents to the specified location, without changing the original document’s location.
- [NSDocument.SaveOperationType.autosaveElsewhereOperation](nsdocument/saveoperationtype/autosaveelsewhereoperation.md)
  An operation that writes an autosave version of the file to a different location.
- [NSDocument.SaveOperationType.autosaveInPlaceOperation](nsdocument/saveoperationtype/autosaveinplaceoperation.md)
  An operation that overwrites the document’s current contents with autosave data.
- [NSDocument.SaveOperationType.autosaveAsOperation](nsdocument/saveoperationtype/autosaveasoperation.md)
  An operation that writes a document’s contents to a new file or file package even though the user has not explicitly requested it, then changes the document’s current location to point to the just-written file or file package.
### Initializers
- [init?(rawValue: UInt)](nsdocument/saveoperationtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

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
- [func save(to: URL, ofType: String, for: NSDocument.SaveOperationType, completionHandler: ((any Error)?) -> Void)](nsdocument/save(to:oftype:for:completionhandler:).md)
  Saves the contents of the document to a file or file package located by a URL, that is formatted to a specified type, for a particular kind of save operation, and invokes the passed-in completion handler.
- [func fileAttributesToWrite(to: URL, ofType: String, for: NSDocument.SaveOperationType, originalContentsURL: URL?) throws -> [String : Any]](nsdocument/fileattributestowrite(to:oftype:for:originalcontentsurl:).md)
  Returns the attributes to write to the file or file package at the specified URL, and targeting the specified type of save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/saveoperationtype)*