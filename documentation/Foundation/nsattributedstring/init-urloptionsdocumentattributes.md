# init(URL:options:documentAttributes:)

**Framework**: Foundation  
**Kind**: init

Creates an attributed string from the contents of the specified URL.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(url: URL, options: [NSAttributedString.DocumentReadingOptionKey : Any] = [:], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws
```

#### Return Value

Returns an initialized attributed string object, or `nil` if the method can’t decode the data.

#### Discussion

Filter services can be used to convert the file into a format recognized by Cocoa. The `options` dictionary specifies how the document should be loaded and can contain the values described in [`NSAttributedStringDocumentReadingOptionKey`](https://developer.apple.com/documentation/UIKit/NSAttributedStringDocumentReadingOptionKey). If you specify the [`documentType`](nsattributedstring/documentreadingoptionkey/documenttype.md) or [`fileType`](nsattributedstring/documentreadingoptionkey/filetype.md) attribute, this method treats the data as if it is in the specified format. If you don’t specify one of these options, the method examines the document and loads it using whatever format it seems to contain.

If an error occurs, the method returns `nil` and sets the `error` parameter to an [`NSError`](nserror.md) object with information about why it couldn’t create the attributed string object.

> **Note**:  In Swift, this API is imported as an initializer and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: An   object specifying the document to load.
- `options`: Attributes for interpreting the document contents. Specify the   or   option to interpret the data as a specific type. When sharing files between different platforms, specify the   or   options for any required text scaling behaviors. Specify the   attribute for plain-text files. Specify the   key to apply document attributes to the returned string. If you specify an empty dictionary, the method identifies the data format from the data itself.
- `dict`: An in-out dictionary containing document-level attributes. On output, this method updates the dictionary to contain any document-specific keys found in the data. Specify   if you don’t want the document attributes.

## See Also

- [init(data: Data, options: [NSAttributedString.DocumentReadingOptionKey : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws](nsattributedstring/init(data:options:documentattributes:).md)
  Creates an attributed string from the contents of the specified data object.
- [init?(docFormat: Data, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](nsattributedstring/init(docformat:documentattributes:).md)
  Creates an attributed string from Microsoft Word format data in the specified data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/init(url:options:documentattributes:))*