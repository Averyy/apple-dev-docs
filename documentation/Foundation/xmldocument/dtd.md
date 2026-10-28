# dtd

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns an [`XMLDTD`](../xmldtd.md) object representing the internal DTD associated with the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
@NSCopying
var dtd: XMLDTD? { get set }
```

```objc
@property (copy, nullable) NSXMLDTD * DTD;
```

## Return Value

An [`XMLDTD`](../xmldtd.md) object representing the internal DTD associated with the receiver or `nil` if no DTD has been associated.

## See Also

### Managing Document Attributes
- [var characterEncoding: String?](./characterencoding.md)
  Sets the character encoding of the receiver to `encoding`,
- [var documentContentKind: XMLDocument.ContentKind](./documentcontentkind.md)
  Sets the kind of output content for the receiver.
- [var isStandalone: Bool](./isstandalone.md)
  Sets a Boolean value that specifies whether the receiver represents a standalone XML document.
- [var mimeType: String?](./mimetype.md)
  Returns the MIME type for the receiver.
- [var version: String?](./version.md)
  Sets the version of the receiver’s XML.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/dtd)*