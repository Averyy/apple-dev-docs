# read(from:ofType:)

**Framework**: AppKit  
**Kind**: method

Sets the contents of this document by reading from a file or file package, of a specified type, located by a URL.

**Availability**:
- macOS ?+

## Declaration

```swift
nonisolated
func read(from url: URL, ofType typeName: String) throws
```

#### Discussion

The default implementation of this method just creates an NSFileWrapper and invokes `[self readFromFileWrapper:theFileWrapper ofType:typeName error:outError]`.

For backward binary compatibility with OS X v10.3 and earlier, the default implementation of this method instead invokes `[self readFromFile:[absoluteURL path] ofType:typeName]` if [`readFromFile:ofType:`](nsdocument/readfromfile:oftype:.md) is overridden and the URL uses the `file:` scheme.

> **Note**:  In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure. When overriding this method, use the `throw` statement to throw an `NSError`, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

 In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure.

When overriding this method, use the `throw` statement to throw an `NSError`, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: The location from which the document contents are read.
- `typeName`: The string that identifies the document type.

## See Also

- [class func canConcurrentlyReadDocuments(ofType: String) -> Bool](nsdocument/canconcurrentlyreaddocuments(oftype:).md)
  Returns a Boolean value that indicates whether the receiver reads multiple documents of the given type concurrently.
- [func read(from: FileWrapper, ofType: String) throws](nsdocument/read(from:oftype:)-3rzsi.md)
  Sets the contents of this document by reading from a file wrapper of a specified type.
- [func read(from: Data, ofType: String) throws](nsdocument/read(from:oftype:)-6g6ai.md)
  Sets the contents of this document by reading from data of a specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/read(from:oftype:)-1vttv)*