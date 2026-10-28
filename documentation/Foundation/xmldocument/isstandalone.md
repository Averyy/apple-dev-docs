# isStandalone

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Sets a Boolean value that specifies whether the receiver represents a standalone XML document.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var isStandalone: Bool { get set }
```

```objc
@property (getter=isStandalone) BOOL standalone;
```

## Discussion

A standalone document does not have an external DTD associated with it.

## Parameters

- `standalone`: [`true`](../../Swift/true.md) if the receiver represents a standalone XML document, [`false`](../../Swift/false.md) otherwise.

## See Also

### Managing Document Attributes
- [var characterEncoding: String?](./characterencoding.md)
  Sets the character encoding of the receiver to `encoding`,
- [var documentContentKind: XMLDocument.ContentKind](./documentcontentkind.md)
  Sets the kind of output content for the receiver.
- [var dtd: XMLDTD?](./dtd.md)
  Returns an [`XMLDTD`](../xmldtd.md) object representing the internal DTD associated with the receiver.
- [var mimeType: String?](./mimetype.md)
  Returns the MIME type for the receiver.
- [var version: String?](./version.md)
  Sets the version of the receiver’s XML.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/isstandalone)*