# write(to:ofType:for:originalContentsURL:)

**Framework**: Appkit  
**Kind**: method

Writes the contents of the document to a file or file package located by a URL.

**Availability**:
- macOS ?+

## Declaration

```swift
nonisolated
func write(to url: URL, ofType typeName: String, for saveOperation: NSDocument.SaveOperationType, originalContentsURL absoluteOriginalContentsURL: URL?) throws
```

#### Discussion

The default implementation of this method merely invokes `[self writeToURL:absoluteURL ofType:typeName error:outError]`. You can override this method instead of one of the three simple writing methods ([`write(to:ofType:)`](nsdocument/write(to:oftype:).md),[`fileWrapper(ofType:)`](nsdocument/filewrapper(oftype:).md), and [`data(ofType:)`](nsdocument/data(oftype:).md)) if your document writing machinery needs access to the on-disk representation of the document revision that is about to be overwritten. The value of `absoluteURL` is often not the same as `[self fileURL]`. Other times it is not the same as the URL for the final save destination. Likewise, `absoluteOriginalContentsURL` is often not the same value as `[self fileURL]`. If `absoluteOriginalContentsURL` is `nil`, either the document has never been saved or the user deleted the document file since it was opened.

For backward binary compatibility with OS X v10.3 and earlier, if [`writeToFile:ofType:originalFile:saveOperation:`](nsdocument/writetofile:oftype:originalfile:saveoperation:.md) is overridden and both URLs use the `file:` scheme, the default implementation of this method instead invokes:

```objc
[self writeToFile:[absoluteURL path]
      ofType:typeName
      originalFile:[absoluteOriginalContentsURL path]
      saveOperation:aSaveOperation];
```

The save operation used in this case is never `NSAutosaveOperation`; `NSSaveToOperation` is used instead.

> **Note**:  In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure. When overriding this method, use the `throw` statement to throw an `NSError`, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: The location to which the document contents are written.
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
- [func save(to: URL, ofType: String, for: NSDocument.SaveOperationType, delegate: Any?, didSave: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsdocument/save(to:oftype:for:delegate:didsave:contextinfo:).md)
  Saves the contents of the document to a file or file package located by a URL, that is formatted to a specified type, for a particular kind of save operation.
- [func save(to: URL, ofType: String, for: NSDocument.SaveOperationType, completionHandler: ((any Error)?) -> Void)](nsdocument/save(to:oftype:for:completionhandler:).md)
  Saves the contents of the document to a file or file package located by a URL, that is formatted to a specified type, for a particular kind of save operation, and invokes the passed-in completion handler.
- [func fileAttributesToWrite(to: URL, ofType: String, for: NSDocument.SaveOperationType, originalContentsURL: URL?) throws -> [String : Any]](nsdocument/fileattributestowrite(to:oftype:for:originalcontentsurl:).md)
  Returns the attributes to write to the file or file package at the specified URL, and targeting the specified type of save operation.
- [NSDocument.SaveOperationType](nsdocument/saveoperationtype.md)
  Constants for specifying the type of document-save operation to perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/write(to:oftype:for:originalcontentsurl:))*