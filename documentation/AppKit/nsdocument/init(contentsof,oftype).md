# init(contentsOf:ofType:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes a document located by a URL of a specified type.

**Availability**:
- macOS

## Declaration

```swift
convenience init(contentsOf url: URL, ofType typeName: String) throws
```

```objc
- (instancetype) initWithContentsOfURL:(NSURL *) url ofType:(NSString *) typeName error:(NSError **) outError;
```

#### Return Value

The initialized `NSDocument` object, or, if the document could not be created, `nil`.

#### Discussion

You can override this method to customize the reopening of autosaved documents.

This method is invoked by the `NSDocumentController` method [`makeDocument(withContentsOf:ofType:)`](../nsdocumentcontroller/makedocument%28withcontentsof,oftype%29.md). The default implementation of this method calls the [`init()`](./init%28%29.md) and [`read(from:ofType:)`](./read%28from,oftype%29-1vttv.md) methods and sets values for the [`fileURL`](./fileurl.md), [`fileType`](./filetype.md), and [`fileModificationDate`](./filemodificationdate.md) properties.

For backward binary compatibility with OS X v10.3 and earlier, the default implementation of this method instead invokes [`initWithContentsOfFile:ofType:`](./initwithcontentsoffile_oftype_.md) if it is overridden and the URL uses the `file:` scheme. It still updates the  [`fileModificationDate`](./filemodificationdate.md) property in this situation.

> **Handling Errors in Swift**:  In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> When overriding this method, use the `throw` statement to throw an `NSError`, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: The URL from which the contents of the document are obtained.
- `typeName`: The string that identifies the document type.

## See Also

### Creating a Document Object
- [init()](./init%28%29.md)
  Initializes and returns an empty document object.
- [convenience init(for: URL?, withContentsOf: URL, ofType: String) throws](./init%28for,withcontentsof,oftype%29.md)
  Initializes a document with the specified contents, and places the resulting document’s file at the designated location.
- [convenience init(type: String) throws](./init%28type%29.md)
  Initializes a document of a specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/init(contentsof:oftype:))*