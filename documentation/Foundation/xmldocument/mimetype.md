# mimeType

**Framework**: Foundation  
**Kind**: property

Returns the MIME type for the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var mimeType: String? { get set }
```

#### Return Value

The MIME type for the receiver (for example, “text/xml”).

#### Discussion

MIME types are assigned by IANA (see [`http://www.iana.org/assignments/media-types/index.html`](https://developer.apple.comhttp://www.iana.org/assignments/media-types/index.html)).

## See Also

- [var characterEncoding: String?](xmldocument/characterencoding.md)
  Sets the character encoding of the receiver to `encoding`,
- [var documentContentKind: XMLDocument.ContentKind](xmldocument/documentcontentkind.md)
  Sets the kind of output content for the receiver.
- [var dtd: XMLDTD?](xmldocument/dtd.md)
  Returns an [`XMLDTD`](xmldtd.md) object representing the internal DTD associated with the receiver.
- [var isStandalone: Bool](xmldocument/isstandalone.md)
  Sets a Boolean value that specifies whether the receiver represents a standalone XML document.
- [var version: String?](xmldocument/version.md)
  Sets the version of the receiver’s XML.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/mimetype)*