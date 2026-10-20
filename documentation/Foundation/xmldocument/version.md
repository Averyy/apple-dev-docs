# version

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Sets the version of the receiver’s XML.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var version: String? { get set }
```

```objc
@property (copy, nullable) NSString * version;
```

#### Discussion

Currently, the version should be either “1.0 “or “1.1”.

## Parameters

- `version`: A string object identifying the version of the XML.

## See Also

### Managing Document Attributes
- [var characterEncoding: String?](./characterencoding.md)
  Sets the character encoding of the receiver to `encoding`,
- [var documentContentKind: XMLDocument.ContentKind](./documentcontentkind.md)
  Sets the kind of output content for the receiver.
- [var dtd: XMLDTD?](./dtd.md)
  Returns an [`XMLDTD`](../xmldtd.md) object representing the internal DTD associated with the receiver.
- [var isStandalone: Bool](./isstandalone.md)
  Sets a Boolean value that specifies whether the receiver represents a standalone XML document.
- [var mimeType: String?](./mimetype.md)
  Returns the MIME type for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/version)*