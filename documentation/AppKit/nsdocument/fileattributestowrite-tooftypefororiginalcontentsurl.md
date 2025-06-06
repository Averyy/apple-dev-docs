# fileAttributesToWrite(to:ofType:for:originalContentsURL:)

**Framework**: AppKit  
**Kind**: method

Returns the attributes to write to the file or file package at the specified URL, and targeting the specified type of save operation.

**Availability**:
- macOS ?+

## Declaration

```swift
nonisolated
func fileAttributesToWrite(to url: URL, ofType typeName: String, for saveOperation: NSDocument.SaveOperationType, originalContentsURL absoluteOriginalContentsURL: URL?) throws -> [String : Any]
```

#### Return Value

A dictionary containing the attributes to be written, or `nil` if unsuccessful.

#### Discussion

Your subclass of `NSDocument` can override this method to control the attributes that are set during a save operation. An override of this method should return a copy of the dictionary returned by its superclass’s version of this method, with appropriate alterations.

The set of valid file attributes is a subset of those understood by the `NSFileManager` class. The default implementation of this method returns an empty dictionary for an `NSSaveOperation` or `NSAutosaveInPlaceOperation`, or a dictionary with an appropriate `NSFileExtensionHidden` entry for any other kind of save operation. You can override this method to customize the attributes that are written to document files.

For backward binary compatibility with OS X v10.5 and earlier, the default implementation of this method returns a dictionary with `NSFileHFSCode` and `NSFileHFSTypeCode` entries that have a value of 0 for `NSSaveOperation`, in apps linked against OS X v10.5 or earlier.

For backward binary compatibility with OS X v10.3 and earlier, the default implementation of this method instead invokes `[self fileAttributesToWriteToFile:[url path] ofType:typeName saveOperation:aSaveOperation]` if [`fileAttributesToWriteToFile:ofType:saveOperation:`](nsdocument/fileattributestowritetofile:oftype:saveoperation:.md) is overridden and the URL uses the `file:` scheme. The save operation used in this case is never one of the autosaving ones: `NSSaveToOperation` is used instead.

The default implementation of [`writeSafely(to:ofType:for:)`](nsdocument/writesafely(to:oftype:for:).md) automatically copies important attributes like file permissions, creation date, and Finder information from the old on-disk version of a document to the new one during an `NSSaveOperation` or `NSAutosaveInPlaceOperation`. This method is meant to be used just for attributes that need to be written for the first time, for `NSSaveAsOperation` and `NSSaveToOperation`. The `url` and `absoluteOriginalContentsURL` parameters are passed in for completeness; NSDocument’s default implementation doesn’t need to use them.

> **Note**:  In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure. When overriding this method, use the `throw` statement to throw an `NSError`, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

 In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure.

When overriding this method, use the `throw` statement to throw an `NSError`, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: The location to which the document is being written.
- `typeName`: The string that identifies the document type.
- `saveOperation`: The type of save operation.
- `absoluteOriginalContentsURL`: The location of the previously saved copy of the document (if not  ).

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
- [NSDocument.SaveOperationType](nsdocument/saveoperationtype.md)
  Constants for specifying the type of document-save operation to perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/fileattributestowrite(to:oftype:for:originalcontentsurl:))*