# read(from:options:documentAttributes:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets the contents of receiver from the file at the specified URL.

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

> **Deprecated**: Use [`read(from:options:documentAttributes:)`](./read%28from,options,documentattributes%29-54wth.md) instead.

## Declaration

```swift
func read(from url: URL, options: [AnyHashable : Any] = [:], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Bool
```

```objc
- (BOOL) readFromURL:(NSURL *) url options:(NSDictionary *) options documentAttributes:(NSDictionary **) dict;
```

#### Return Value

[`true`](../../Swift/true.md) if the attributed string is created successfully or [`false`](../../Swift/false.md) if it was not.

#### Discussion

Filter services can be used to convert the contents of the URL into a format recognized by Cocoa.

## Parameters

- `url`: The URL of the document to open.
- `options`: The option keys for importing the document. For a list of possible values, see “Option keys for importing documents” in [`NSAttributedString`](../nsattributedstring.md).
- `dict`: On return, contains the document attributes. For a list of possible values, see “Document Attributes” in [`NSAttributedString`](../nsattributedstring.md).

## See Also

### Deprecated
- [func read(from: Data, options: [AnyHashable : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Bool](./read%28from,options,documentattributes%29-967j7.md)
  Sets the contents of the receiver from the specified data object`.`
- [func read(fromFileURL: URL, options: [AnyHashable : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws](./read%28fromfileurl,options,documentattributes%29.md)
  Sets the contents of the receiver from the file at the given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/read(from:options:documentattributes:)-85y1d)*