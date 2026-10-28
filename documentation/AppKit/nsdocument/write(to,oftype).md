# write(to:ofType:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Writes the contents of the document to a file or file package located by a URL, that is formatted to a specified type.

**Availability**:
- macOS

## Declaration

```swift
nonisolated
func write(to url: URL, ofType typeName: String) throws
```

```objc
- (BOOL) writeToURL:(NSURL *) url ofType:(NSString *) typeName error:(NSError **) outError;
```

## Discussion

The default implementation of this method just invokes `[self fileWrapperOfType:typeName error:outError]` and writes the returned file wrapper to disk.

For backward binary compatibility with OS X v10.3 and earlier, the default implementation of this method instead invokes `[self writeToFile:[absoluteURL path] ofType:typeName]` if [`writeToFile:ofType:`](./writetofile_oftype_.md) is overridden and the URL uses the `file:` scheme.

> **Handling Errors in Swift**:  In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> When overriding this method, use the `throw` statement to throw an `NSError`, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: The location to which the document contents are written.
- `typeName`: The string that identifies the document type.

## See Also

### Writing the Document’s Content
- [func canAsynchronouslyWrite(to: URL, ofType: String, for: NSDocument.SaveOperationType) -> Bool](./canasynchronouslywrite%28to,oftype,for%29.md)
  Returns whether the receiver can concurrently write to a file or file package located by a URL, that is formatted for a specific type, for a specific kind of save operation.
- [func unblockUserInteraction()](./unblockuserinteraction%28%29.md)
  Unblocks the main thread during asynchronous saving.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/write(to:oftype:))*