# Document Content Types

**Framework**: Foundation

Define document types.

#### Overview

You specify one of the NSXMLDocumentContentKind constants in [`documentContentKind`](xmldocument/documentcontentkind.md) to indicate the kind of content required for document output.

## Topics

### Constants
- [XMLDocument.ContentKind.xml](xmldocument/contentkind/xml.md)
  The default type of document content type, which is XML.
- [XMLDocument.ContentKind.xhtml](xmldocument/contentkind/xhtml.md)
  The document output is XHTML.
- [XMLDocument.ContentKind.html](xmldocument/contentkind/html.md)
  Outputs empty tags in HTML without a close tag, such as `<br>`.
- [XMLDocument.ContentKind.text](xmldocument/contentkind/text.md)
  Outputs the string value of the document by extracting the string values from all text nodes.

## See Also

- [Input and Output Options](input_and_output_options.md)
  Input and output options specifically intended for `NSXMLDocument` objects.
- [XMLDocument.ContentKind](xmldocument/contentkind.md)
  Type used to define the kind of document content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/document-content-types)*