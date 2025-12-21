# read(from:options:documentAttributes:)

**Framework**: Foundation  
**Kind**: method

Sets the contents of the receiver from the specified data object`.`

**Availability**:
- macOS 10.0+

## Declaration

```swift
func read(from data: Data, options: [AnyHashable : Any] = [:], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the attributed string is created successfully or [`false`](https://developer.apple.com/documentation/Swift/false) if it was not.

## Parameters

- `data`: The data to read.
- `options`: The option keys for importing the document. For a list of possible values, see “Option keys for importing documents” in  .
- `dict`: On return, contains the document attributes. For a list of possible values, see “Document Attributes” in  .

## See Also

- [func read(from: URL, options: [AnyHashable : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Bool](nsmutableattributedstring/read(from:options:documentattributes:)-85y1d.md)
  Sets the contents of receiver from the file at the specified URL.
- [func read(fromFileURL: URL, options: [AnyHashable : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws](nsmutableattributedstring/read(fromfileurl:options:documentattributes:).md)
  Sets the contents of the receiver from the file at the given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/read(from:options:documentattributes:)-967j7)*