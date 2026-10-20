# init(fileURL:options:documentAttributes:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a new attributed string object from the data at the specified URL.

**Availability**:
- iOS 7.0+ - Deprecated in 9.0
- iPadOS 7.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use [`init(URL:options:documentAttributes:)`](./init%28url,options,documentattributes%29.md) instead.

## Declaration

```swift
init(fileURL url: URL, options: [AnyHashable : Any] = [:], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws
```

```objc
- (instancetype) initWithFileURL:(NSURL *) url options:(NSDictionary *) options documentAttributes:(NSDictionary **) dict error:(NSError **) error;
```

#### Return Value

Returns an initialized attributed string object, or `nil` if the data can’t be decoded.

#### Discussion

The HTML importer should not be called from a background thread (that is, the `options` dictionary includes [`documentType`](./documentattributekey/documenttype.md) with a value of [`html`](./documenttype/html.md)). It will try to synchronize with the main thread, fail, and time out. Calling it from the main thread works (but can still time out if the HTML contains references to external resources, which should be avoided at all costs). The HTML import mechanism is meant for implementing something like markdown (that is, text styles, colors, and so on), not for general HTML import.

> **Handling Errors in Swift**:  In Swift, this API is imported as an initializer and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: An `NSURL` object specifying the document to load.
- `options`: Document attributes for interpreting the document contents. [`documentType`](./documentattributekey/documenttype.md), [`characterEncoding`](./documentattributekey/characterencoding.md), and [`defaultAttributes`](./documentattributekey/defaultattributes.md) are supported option keys. If not specified, the method examines the data to attempt to determine the appropriate attributes.
- `dict`: If non-`NULL`, returns a dictionary with various document-wide attributes accessible via document attribute keys.

## See Also

### Deprecated Initializers
- [init?(path: String, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](./init%28path,documentattributes%29.md)
  Initializes a new attribute string object from RTF or RTFD data in the file at the specified path.
- [init?(URL: URL, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](./init%28url,documentattributes%29.md)
  Initializes a new attributed string object from the data at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/init(fileurl:options:documentattributes:))*