# writeSafely(to:ofType:for:)

**Framework**: AppKit  
**Kind**: method

Writes the contents of the document to a file or file package located by a URL.

**Availability**:
- macOS ?+

## Declaration

```swift
nonisolated
func writeSafely(to url: URL, ofType typeName: String, for saveOperation: NSDocument.SaveOperationType) throws
```

#### Discussion

The default implementation of this method invokes [`write(to:ofType:for:originalContentsURL:)`](nsdocument/write(to:oftype:for:originalcontentsurl:).md). It also invokes [`fileAttributesToWrite(to:ofType:for:originalContentsURL:)`](nsdocument/fileattributestowrite(to:oftype:for:originalcontentsurl:).md) and writes the returned attributes, if any, to the file. It may copy some attributes from the old on-disk revision of the document at the same time, if applicable.

This method is responsible for doing document writing in a way that minimizes the danger of leaving the disk to which writing is being done in an inconsistent state in the event of an app crash, system crash, hardware failure, power outage, and so on. If you override this method, be sure to invoke the superclass implementation.

For `NSSaveOperation`, the default implementation of this method uses the value in the [`keepBackupFile`](nsdocument/keepbackupfile.md) property to determine whether or not the old on-disk revision of the document, if there was one, should be preserved after being renamed.

For backward binary compatibility with OS X v10.3 and earlier, the default implementation of this method instead invokes [`writeWithBackupToFile:ofType:saveOperation:`](nsdocument/writewithbackuptofile:oftype:saveoperation:.md) if that method is is overridden and the URL uses the `file:` scheme. The save operation in this case is never `NSAutosaveOperation`; `NSSaveToOperation` is used instead.

> **Note**:  In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure. When overriding this method, use the `throw` statement to throw an `NSError`, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

 In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure.

When overriding this method, use the `throw` statement to throw an `NSError`, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: The location to which the document contents are written.
- `typeName`: The string that identifies the document type.
- `saveOperation`: The type of save operation.

## See Also

- [func canAsynchronouslyWrite(to: URL, ofType: String, for: NSDocument.SaveOperationType) -> Bool](nsdocument/canasynchronouslywrite(to:oftype:for:).md)
  Returns whether the receiver can concurrently write to a file or file package located by a URL, that is formatted for a specific type, for a specific kind of save operation.
- [func unblockUserInteraction()](nsdocument/unblockuserinteraction.md)
  Unblocks the main thread during asynchronous saving.
- [func write(to: URL, ofType: String) throws](nsdocument/write(to:oftype:).md)
  Writes the contents of the document to a file or file package located by a URL, that is formatted to a specified type.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/writesafely(to:oftype:for:))*