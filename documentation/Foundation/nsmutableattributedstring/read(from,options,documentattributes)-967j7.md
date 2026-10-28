# read(from:options:documentAttributes:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets the contents of the receiver from the specified data object`.`

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

> **Deprecated**: Use [`read(from:options:documentAttributes:)`](./read%28from,options,documentattributes%29-5mbcx.md) instead.

## Declaration

```swift
func read(from data: Data, options: [AnyHashable : Any] = [:], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Bool
```

```objc
- (BOOL) readFromData:(NSData *) data options:(NSDictionary *) options documentAttributes:(NSDictionary **) dict;
```

## Return Value

[`true`](../../Swift/true.md) if the attributed string is created successfully or [`false`](../../Swift/false.md) if it was not.

## Parameters

- `data`: The data to read.
- `options`: The option keys for importing the document. For a list of possible values, see “Option keys for importing documents” in [`NSAttributedString`](../nsattributedstring.md).
- `dict`: On return, contains the document attributes. For a list of possible values, see “Document Attributes” in [`NSAttributedString`](../nsattributedstring.md).

## See Also

### Deprecated
- [func read(from: URL, options: [AnyHashable : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Bool](./read%28from,options,documentattributes%29-85y1d.md)
  Sets the contents of receiver from the file at the specified URL.
- [func read(fromFileURL: URL, options: [AnyHashable : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws](./read%28fromfileurl,options,documentattributes%29.md)
  Sets the contents of the receiver from the file at the given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/read(from:options:documentattributes:)-967j7)*