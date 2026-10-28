# characterEncoding

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Sets the character encoding of the receiver to `encoding`,

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var characterEncoding: String? { get set }
```

```objc
@property (copy, nullable) NSString * characterEncoding;
```

## Discussion

Typically the encoding is specified in the XML declaration of a document that is processed, but it can be set at any time. If the specified encoding does not match the actual encoding, parsing of the document might fail.

## Parameters

- `encoding`: A string that specifies an encoding; it must match the name of an IANA character set. See [http://www.iana.org/assignments/character-sets](http://www.iana.org/assignments/character-sets) for a list of valid encoding specifiers.

## See Also

### Managing Document Attributes
- [var documentContentKind: XMLDocument.ContentKind](./documentcontentkind.md)
  Sets the kind of output content for the receiver.
- [var dtd: XMLDTD?](./dtd.md)
  Returns an [`XMLDTD`](../xmldtd.md) object representing the internal DTD associated with the receiver.
- [var isStandalone: Bool](./isstandalone.md)
  Sets a Boolean value that specifies whether the receiver represents a standalone XML document.
- [var mimeType: String?](./mimetype.md)
  Returns the MIME type for the receiver.
- [var version: String?](./version.md)
  Sets the version of the receiver’s XML.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/characterencoding)*