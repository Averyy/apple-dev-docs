# read(from:ofType:)

**Framework**: AppKit  
**Kind**: method

Sets the contents of this document by reading from a file wrapper of a specified type.

**Availability**:
- macOS ?+

## Declaration

```swift
nonisolated
func read(from fileWrapper: FileWrapper, ofType typeName: String) throws
```

#### Discussion

The default implementation of this method invokes `[self readFromData:[fileWrapper regularFileContents] ofType:typeName error:outError]`.

For backward binary compatibility with OS X v10.3 and earlier, the default implementation of this method instead invokes `[self loadFileWrapperRepresentation:fileWrapper ofType:typeName]` if [`loadFileWrapperRepresentation:ofType:`](nsdocument/loadfilewrapperrepresentation:oftype:.md) is overridden.

> **Note**:  In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure. When overriding this method, use the `throw` statement to throw an `NSError`, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `fileWrapper`: The file wrapper from which the document contents are read.
- `typeName`: The string that identifies the document type.

## See Also

- [class func canConcurrentlyReadDocuments(ofType: String) -> Bool](nsdocument/canconcurrentlyreaddocuments(oftype:).md)
  Returns a Boolean value that indicates whether the receiver reads multiple documents of the given type concurrently.
- [func read(from: URL, ofType: String) throws](nsdocument/read(from:oftype:)-1vttv.md)
  Sets the contents of this document by reading from a file or file package, of a specified type, located by a URL.
- [func read(from: Data, ofType: String) throws](nsdocument/read(from:oftype:)-6g6ai.md)
  Sets the contents of this document by reading from data of a specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/read(from:oftype:)-3rzsi)*