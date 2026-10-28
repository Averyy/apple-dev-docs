# init(path:documentAttributes:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a new attribute string object from RTF or RTFD data in the file at the specified path.

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

> **Deprecated**: Use [`init(URL:options:documentAttributes:)`](./init%28url,options,documentattributes%29.md) instead.

## Declaration

```swift
init?(path: String, documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)
```

```objc
- (instancetype) initWithPath:(NSString *) path documentAttributes:(NSDictionary **) dict;
```

## Return Value

Returns an initialized object, or `nil` if the data can’t be decoded.

## Discussion

The contents of `path` will be examined to best load the file in whatever format it’s in. Filter services can be used to convert the file into a format recognized by Cocoa. Also returns by reference in `docAttributes` a dictionary containing document-level attributes described in `Document Attributes`. `docAttributes` may be `NULL`, in which case no document attributes are returned. Returns an initialized object, or `nil` if the file at `path` can’t be decoded.

## Parameters

- `path`: The path to an RTF or RTFD file.
- `dict`: An in-out dictionary containing document-level attributes described in `Document Attributes`. May be `NULL`, in which case no document attributes are returned.

## See Also

### Deprecated Initializers
- [init?(URL: URL, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](./init%28url,documentattributes%29.md)
  Initializes a new attributed string object from the data at the specified URL.
- [init(fileURL: URL, options: [AnyHashable : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws](./init%28fileurl,options,documentattributes%29.md)
  Initializes a new attributed string object from the data at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/init(path:documentattributes:))*