# documentContentKind

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Sets the kind of output content for the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var documentContentKind: XMLDocument.ContentKind { get set }
```

```objc
@property NSXMLDocumentContentKind documentContentKind;
```

#### Discussion

Most of the differences among document-content kind have to do with the handling of content-less tags such as `<br>`.

## Parameters

- `kind`: An `enum` constant identifying a kind of document content. The valid NSXMLDocumentContentKind constants are `NSXMLDocumentXMLKind`, `NSXMLDocumentXHTMLKind`, `NSXMLDocumentHTMLKind`, and `NSXMLDocumentTextKind`.

## See Also

### Managing Document Attributes
- [var characterEncoding: String?](./characterencoding.md)
  Sets the character encoding of the receiver to `encoding`,
- [var dtd: XMLDTD?](./dtd.md)
  Returns an [`XMLDTD`](../xmldtd.md) object representing the internal DTD associated with the receiver.
- [var isStandalone: Bool](./isstandalone.md)
  Sets a Boolean value that specifies whether the receiver represents a standalone XML document.
- [var mimeType: String?](./mimetype.md)
  Returns the MIME type for the receiver.
- [var version: String?](./version.md)
  Sets the version of the receiver’s XML.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/documentcontentkind)*