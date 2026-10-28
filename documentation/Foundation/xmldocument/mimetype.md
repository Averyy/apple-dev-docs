# mimeType

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the MIME type for the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var mimeType: String? { get set }
```

```objc
@property (copy, nullable) NSString * MIMEType;
```

## Return Value

The MIME type for the receiver (for example, “text/xml”).

## Discussion

MIME types are assigned by IANA (see [http://www.iana.org/assignments/media-types/index.html](http://www.iana.org/assignments/media-types/index.html)).

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
- [var version: String?](./version.md)
  Sets the version of the receiver’s XML.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/mimetype)*