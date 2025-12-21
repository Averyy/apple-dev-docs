# read(from:options:documentAttributes:)

**Framework**: Foundation  
**Kind**: method

Sets the contents of receiver from the file at the specified URL.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func read(from url: URL, options: [AnyHashable : Any] = [:], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the attributed string is created successfully or [`false`](https://developer.apple.com/documentation/Swift/false) if it was not.

#### Discussion

Filter services can be used to convert the contents of the URL into a format recognized by Cocoa.

## Parameters

- `url`: The URL of the document to open.
- `options`: The option keys for importing the document. For a list of possible values, see “Option keys for importing documents” in  .
- `dict`: On return, contains the document attributes. For a list of possible values, see “Document Attributes” in  .

## See Also

- [func read(from: Data, options: [AnyHashable : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Bool](nsmutableattributedstring/read(from:options:documentattributes:)-967j7.md)
  Sets the contents of the receiver from the specified data object`.`
- [func read(fromFileURL: URL, options: [AnyHashable : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws](nsmutableattributedstring/read(fromfileurl:options:documentattributes:).md)
  Sets the contents of the receiver from the file at the given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/read(from:options:documentattributes:)-85y1d)*