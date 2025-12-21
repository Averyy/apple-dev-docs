# XMLDocument.ContentKind

**Framework**: Foundation  
**Kind**: enum

Type used to define the kind of document content.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
enum ContentKind
```

#### Overview

For possible values, see doc:xmldocument/document_content_types.

## Topics

### Enumeration Cases
- [XMLDocument.ContentKind.html](xmldocument/contentkind/html.md)
  Outputs empty tags in HTML without a close tag, such as `<br>`.
- [XMLDocument.ContentKind.text](xmldocument/contentkind/text.md)
  Outputs the string value of the document by extracting the string values from all text nodes.
- [XMLDocument.ContentKind.xhtml](xmldocument/contentkind/xhtml.md)
  The document output is XHTML.
- [XMLDocument.ContentKind.xml](xmldocument/contentkind/xml.md)
  The default type of document content type, which is XML.
### Initializers
- [init?(rawValue: UInt)](xmldocument/contentkind/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Input and Output Options](input_and_output_options.md)
  Input and output options specifically intended for `NSXMLDocument` objects.
- [Document Content Types](document-content-types.md)
  Define document types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/contentkind)*