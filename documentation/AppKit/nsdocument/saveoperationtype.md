# NSDocument.SaveOperationType

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants for specifying the type of document-save operation to perform.

**Availability**:
- macOS

## Declaration

```swift
enum SaveOperationType
```

```c
enum NSSaveOperationType : NSUInteger;
```

## Overview

These values are used with method parameters of type [`NSDocument.SaveOperationType`](./saveoperationtype.md). Depending on the method, the save operation type can affect the title of the Save dialog and can affect which files are displayed in the dialog.

## Topics

### Constants
- [NSDocument.SaveOperationType.saveOperation](./saveoperationtype/saveoperation.md)
  An operation that overwrites a document’s file or file package with the document’s contents.
- [NSDocument.SaveOperationType.saveAsOperation](./saveoperationtype/saveasoperation.md)
  An operation that writes the document’s contents to a new location and updates the document to point to that location
- [NSDocument.SaveOperationType.saveToOperation](./saveoperationtype/savetooperation.md)
  An operation that writes a copy of the document’s contents to the specified location, without changing the original document’s location.
- [NSDocument.SaveOperationType.autosaveElsewhereOperation](./saveoperationtype/autosaveelsewhereoperation.md)
  An operation that writes an autosave version of the file to a different location.
- [NSDocument.SaveOperationType.autosaveInPlaceOperation](./saveoperationtype/autosaveinplaceoperation.md)
  An operation that overwrites the document’s current contents with autosave data.
- [NSDocument.SaveOperationType.autosaveAsOperation](./saveoperationtype/autosaveasoperation.md)
  An operation that writes a document’s contents to a new file or file package even though the user has not explicitly requested it, then changes the document’s current location to point to the just-written file or file package.
- [NSAutosaveOperation](../nssaveoperationtype/nsautosaveoperation.md)
  Old name for the [`NSAutosaveElsewhereOperation`](./saveoperationtype/autosaveelsewhereoperation.md) operation type.
### Initializers
- [init?(rawValue: UInt)](./saveoperationtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [func save(to: URL, ofType: String, for: NSDocument.SaveOperationType, completionHandler: ((any Error)?) -> Void)](./save%28to,oftype,for,completionhandler%29.md)
  Saves the contents of the document to a file or file package located by a URL, that is formatted to a specified type, for a particular kind of save operation, and invokes the passed-in completion handler.
- [func fileAttributesToWrite(to: URL, ofType: String, for: NSDocument.SaveOperationType, originalContentsURL: URL?) throws -> [String : Any]](./fileattributestowrite%28to,oftype,for,originalcontentsurl%29.md)
  Returns the attributes to write to the file or file package at the specified URL, and targeting the specified type of save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/saveoperationtype)*