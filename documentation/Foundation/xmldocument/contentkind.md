# XMLDocument.ContentKind

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

Type used to define the kind of document content.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
enum ContentKind
```

```c
enum NSXMLDocumentContentKind : NSUInteger;
```

#### Overview

For possible values, see doc:xmldocument/document_content_types.

## Topics

### Enumeration Cases
- [XMLDocument.ContentKind.html](./contentkind/html.md)
  Outputs empty tags in HTML without a close tag, such as `<br>`.
- [XMLDocument.ContentKind.text](./contentkind/text.md)
  Outputs the string value of the document by extracting the string values from all text nodes.
- [XMLDocument.ContentKind.xhtml](./contentkind/xhtml.md)
  The document output is XHTML.
- [XMLDocument.ContentKind.xml](./contentkind/xml.md)
  The default type of document content type, which is XML.
### Initializers
- [init?(rawValue: UInt)](./contentkind/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [Input and Output Options](../input_and_output_options.md)
  Input and output options specifically intended for `NSXMLDocument` objects.
- [Document Content Types](../document-content-types.md)
  Define document types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/contentkind)*