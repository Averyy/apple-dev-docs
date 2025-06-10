# documentContentKind

**Framework**: Foundation  
**Kind**: property

Sets the kind of output content for the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var documentContentKind: XMLDocument.ContentKind { get set }
```

#### Discussion

Most of the differences among document-content kind have to do with the handling of content-less tags such as `<br>`.

## Parameters

- `kind`: An   constant identifying a kind of document content. The valid NSXMLDocumentContentKind constants are  ,  ,  , and  .

## See Also

- [var characterEncoding: String?](xmldocument/characterencoding.md)
  Sets the character encoding of the receiver to `encoding`,
- [var dtd: XMLDTD?](xmldocument/dtd.md)
  Returns an [`XMLDTD`](xmldtd.md) object representing the internal DTD associated with the receiver.
- [var isStandalone: Bool](xmldocument/isstandalone.md)
  Sets a Boolean value that specifies whether the receiver represents a standalone XML document.
- [var mimeType: String?](xmldocument/mimetype.md)
  Returns the MIME type for the receiver.
- [var version: String?](xmldocument/version.md)
  Sets the version of the receiver’s XML.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/documentcontentkind)*