# init(URL:documentAttributes:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a new attributed string object from the data at the specified URL.

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

> **Deprecated**: Use [`init(URL:options:documentAttributes:)`](./init%28url,options,documentattributes%29.md) instead.

## Declaration

```swift
init?(URL url: URL, documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)
```

```swift
init?(url: URL, documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)
```

```objc
- (instancetype) initWithURL:(NSURL *) url documentAttributes:(NSDictionary **) dict;
```

## Return Value

Returns an initialized object, or `nil` if the data can’t be decoded.

## Discussion

The contents of `aURL` are examined to best load the file in whatever format it’s in. Filter services can be used to convert the file into a format recognized by Cocoa. Also returns by reference in `docAttributes` a dictionary containing document-level attributes described in `Document Attributes`. `docAttributes` may be `NULL`, in which case no document attributes are returned. Returns an initialized object, or `nil` if the file at `path` can’t be decoded.

## Parameters

- `url`: An `NSURL` object specifying the document to load.
- `dict`: An in-out dictionary containing document-level attributes described in `Document Attributes`. May be `NULL`, in which case no document attributes are returned.

## See Also

### Deprecated Initializers
- [init?(path: String, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](./init%28path,documentattributes%29.md)
  Initializes a new attribute string object from RTF or RTFD data in the file at the specified path.
- [init(fileURL: URL, options: [AnyHashable : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws](./init%28fileurl,options,documentattributes%29.md)
  Initializes a new attributed string object from the data at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/init(url:documentattributes:))*