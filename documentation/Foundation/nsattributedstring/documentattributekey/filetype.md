# fileType

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The document type for interpreting the document.

**Availability**:
- macOS 10.6+

## Declaration

```swift
static let fileType: NSAttributedString.DocumentAttributeKey
```

## Discussion

The value of this attribute is an [`NSString`](../../nsstring.md) object indicating which document type was used to interpret the document, specified as a UTI; for reading, this is available along with [`documentType`](./documenttype.md), but for writing the two are mutually exclusive.

## See Also

### Getting document type keys
- [static let documentType: NSAttributedString.DocumentAttributeKey](./documenttype.md)
  The document type.
- [static let textEncodingName: NSAttributedString.DocumentAttributeKey](./textencodingname.md)
  The name of the text encoding to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/documentattributekey/filetype)*