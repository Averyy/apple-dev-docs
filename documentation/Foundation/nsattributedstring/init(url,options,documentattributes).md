# init(URL:options:documentAttributes:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

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
init(URL url: URL, options: [NSAttributedString.DocumentReadingOptionKey : Any] = [:], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws
```

```swift
init(url: URL, options: [NSAttributedString.DocumentReadingOptionKey : Any] = [:], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws
```

```objc
- (instancetype) initWithURL:(NSURL *) url options:(NSDictionary<NSString *,id> *) options documentAttributes:(NSDictionary<NSString *,id> **) dict error:(NSError **) error;
```

#### Return Value

Returns an initialized attributed string object, or `nil` if the method can’t decode the data.

#### Discussion

Filter services can be used to convert the file into a format recognized by Cocoa. The `options` dictionary specifies how the document should be loaded and can contain the values described in [`NSAttributedStringDocumentReadingOptionKey`](../../UIKit/nsattributedstringdocumentreadingoptionkey.md). If you specify the [`documentType`](./documentreadingoptionkey/documenttype.md) or [`fileType`](./documentreadingoptionkey/filetype.md) attribute, this method treats the data as if it is in the specified format. If you don’t specify one of these options, the method examines the document and loads it using whatever format it seems to contain.

If an error occurs, the method returns `nil` and sets the `error` parameter to an [`NSError`](../nserror.md) object with information about why it couldn’t create the attributed string object.

> **Handling Errors in Swift**:  In Swift, this API is imported as an initializer and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: An `NSURL` object specifying the document to load.
- `options`: Attributes for interpreting the document contents. Specify the [`documentType`](./documentattributekey/documenttype.md) or [`fileType`](./documentreadingoptionkey/filetype.md) option to interpret the data as a specific type. When sharing files between different platforms, specify the [`sourceTextScaling`](./documentreadingoptionkey/sourcetextscaling.md) or [`targetTextScaling`](./documentreadingoptionkey/targettextscaling.md) options for any required text scaling behaviors. Specify the [`characterEncoding`](./documentattributekey/characterencoding.md) attribute for plain-text files. Specify the [`defaultAttributes`](./documentattributekey/defaultattributes.md) key to apply document attributes to the returned string. If you specify an empty dictionary, the method identifies the data format from the data itself.
- `dict`: An in-out dictionary containing document-level attributes. On output, this method updates the dictionary to contain any document-specific keys found in the data. Specify `nil` if you don’t want the document attributes.

## See Also

### Creating from a data file
- [init(data: Data, options: [NSAttributedString.DocumentReadingOptionKey : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws](./init%28data,options,documentattributes%29.md)
  Creates an attributed string from the contents of the specified data object.
- [init?(docFormat: Data, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](./init%28docformat,documentattributes%29.md)
  Creates an attributed string from Microsoft Word format data in the specified data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/init(url:options:documentattributes:))*