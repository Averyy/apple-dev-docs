# read(from:ofType:)

**Framework**: Appkit  
**Kind**: method

Sets the contents of this document by reading from data of a specified type.

**Availability**:
- macOS ?+

## Declaration

```swift
nonisolated
func read(from data: Data, ofType typeName: String) throws
```

#### Discussion

The default implementation of this method throws an exception because at least one of the three reading methods (this method, [`read(from:ofType:)`](nsdocument/read(from:oftype:)-1vttv.md), [`read(from:ofType:)`](nsdocument/read(from:oftype:)-3rzsi.md)), or every method that may invoke [`read(from:ofType:)`](nsdocument/read(from:oftype:)-1vttv.md), must be overridden.

> **Note**:  In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure. When overriding this method, use the `throw` statement to throw an `NSError`, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `data`: The data object from which the document contents are read.
- `typeName`: The string that identifies the document type.

## See Also

- [class func canConcurrentlyReadDocuments(ofType: String) -> Bool](nsdocument/canconcurrentlyreaddocuments(oftype:).md)
  Returns a Boolean value that indicates whether the receiver reads multiple documents of the given type concurrently.
- [func read(from: URL, ofType: String) throws](nsdocument/read(from:oftype:)-1vttv.md)
  Sets the contents of this document by reading from a file or file package, of a specified type, located by a URL.
- [func read(from: FileWrapper, ofType: String) throws](nsdocument/read(from:oftype:)-3rzsi.md)
  Sets the contents of this document by reading from a file wrapper of a specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/read(from:oftype:)-6g6ai)*