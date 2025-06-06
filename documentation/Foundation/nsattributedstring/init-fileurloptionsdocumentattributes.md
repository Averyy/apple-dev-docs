# init(fileURL:options:documentAttributes:)

**Framework**: Foundation  
**Kind**: init

Initializes a new attributed string object from the data at the specified URL.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
init(fileURL url: URL, options: [AnyHashable : Any] = [:], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws
```

#### Return Value

Returns an initialized attributed string object, or `nil` if the data can’t be decoded.

#### Discussion

The HTML importer should not be called from a background thread (that is, the `options` dictionary includes [`documentType`](nsattributedstring/documentattributekey/documenttype.md) with a value of [`html`](nsattributedstring/documenttype/html.md)). It will try to synchronize with the main thread, fail, and time out. Calling it from the main thread works (but can still time out if the HTML contains references to external resources, which should be avoided at all costs). The HTML import mechanism is meant for implementing something like markdown (that is, text styles, colors, and so on), not for general HTML import.

> **Note**:  In Swift, this API is imported as an initializer and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: An   object specifying the document to load.
- `options`: Document attributes for interpreting the document contents.  ,  , and   are supported option keys. If not specified, the method examines the data to attempt to determine the appropriate attributes.
- `dict`: If non- , returns a dictionary with various document-wide attributes accessible via document attribute keys.

## See Also

- [init?(path: String, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](nsattributedstring/init(path:documentattributes:).md)
  Initializes a new attribute string object from RTF or RTFD data in the file at the specified path.
- [init?(URL: URL, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](nsattributedstring/init(url:documentattributes:).md)
  Initializes a new attributed string object from the data at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/init(fileurl:options:documentattributes:))*