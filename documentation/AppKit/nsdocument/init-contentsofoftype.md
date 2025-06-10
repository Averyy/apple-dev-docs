# init(contentsOf:ofType:)

**Framework**: AppKit  
**Kind**: init

Initializes a document located by a URL of a specified type.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
convenience init(contentsOf url: URL, ofType typeName: String) throws
```

#### Return Value

The initialized `NSDocument` object, or, if the document could not be created, `nil`.

#### Discussion

You can override this method to customize the reopening of autosaved documents.

This method is invoked by the `NSDocumentController` method [`makeDocument(withContentsOf:ofType:)`](nsdocumentcontroller/makedocument(withcontentsof:oftype:).md). The default implementation of this method calls the [`init()`](nsdocument/init().md) and [`read(from:ofType:)`](nsdocument/read(from:oftype:)-1vttv.md) methods and sets values for the [`fileURL`](nsdocument/fileurl.md), [`fileType`](nsdocument/filetype.md), and [`fileModificationDate`](nsdocument/filemodificationdate.md) properties.

For backward binary compatibility with OS X v10.3 and earlier, the default implementation of this method instead invokes [`initWithContentsOfFile:ofType:`](nsdocument/initwithcontentsoffile:oftype:.md) if it is overridden and the URL uses the `file:` scheme. It still updates the  [`fileModificationDate`](nsdocument/filemodificationdate.md) property in this situation.

> **Note**:  In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure. When overriding this method, use the `throw` statement to throw an `NSError`, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: The URL from which the contents of the document are obtained.
- `typeName`: The string that identifies the document type.

## See Also

- [init()](nsdocument/init.md)
  Initializes and returns an empty document object.
- [convenience init(for: URL?, withContentsOf: URL, ofType: String) throws](nsdocument/init(for:withcontentsof:oftype:).md)
  Initializes a document with the specified contents, and places the resulting document’s file at the designated location.
- [convenience init(type: String) throws](nsdocument/init(type:).md)
  Initializes a document of a specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/init(contentsof:oftype:))*