# textEncodingName

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The name of the text encoding to use.

**Availability**:
- macOS 10.0+

## Declaration

```swift
static let textEncodingName: NSAttributedString.DocumentAttributeKey
```

#### Discussion

An [`NSString`](../../nsstring.md) object containing the name, IANA or otherwise, of a text encoding to be used. This attribute is mutually exclusive with [`characterEncoding`](./characterencoding.md).

## See Also

### Getting document type keys
- [static let documentType: NSAttributedString.DocumentAttributeKey](./documenttype.md)
  The document type.
- [static let fileType: NSAttributedString.DocumentAttributeKey](./filetype.md)
  The document type for interpreting the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/documentattributekey/textencodingname)*