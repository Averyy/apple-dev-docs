# read(from:ofType:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the contents of this document by reading from data of a specified type.

**Availability**:
- macOS

## Declaration

```swift
nonisolated
func read(from data: Data, ofType typeName: String) throws
```

```objc
- (BOOL) readFromData:(NSData *) data ofType:(NSString *) typeName error:(NSError **) outError;
```

## Discussion

The default implementation of this method throws an exception because at least one of the three reading methods (this method, [`read(from:ofType:)`](./read%28from,oftype%29-1vttv.md), [`read(from:ofType:)`](./read%28from,oftype%29-3rzsi.md)), or every method that may invoke [`read(from:ofType:)`](./read%28from,oftype%29-1vttv.md), must be overridden.

> **Handling Errors in Swift**:  In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> When overriding this method, use the `throw` statement to throw an `NSError`, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `data`: The data object from which the document contents are read.
- `typeName`: The string that identifies the document type.

## See Also

### Reading the Document’s Content
- [class func canConcurrentlyReadDocuments(ofType: String) -> Bool](./canconcurrentlyreaddocuments%28oftype%29.md)
  Returns a Boolean value that indicates whether the receiver reads multiple documents of the given type concurrently.
- [func read(from: URL, ofType: String) throws](./read%28from,oftype%29-1vttv.md)
  Sets the contents of this document by reading from a file or file package, of a specified type, located by a URL.
- [func read(from: FileWrapper, ofType: String) throws](./read%28from,oftype%29-3rzsi.md)
  Sets the contents of this document by reading from a file wrapper of a specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/read(from:oftype:)-6g6ai)*