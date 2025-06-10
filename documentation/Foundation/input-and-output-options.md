# Input and Output Options

**Framework**: Foundation

Input and output options specifically intended for `NSXMLDocument` objects.

#### Overview

Because `NSXMLDocument` is a subclass of [`XMLNode`](xmlnode.md), you can also use the relevant input and output options described in Constants in the `NSXMLNode` class reference. You can specify input options in the `NSXMLDocument` methods [`init(contentsOf:options:)`](xmldocument/init(contentsof:options:).md), [`init(data:options:)`](xmldocument/init(data:options:).md), [`init(xmlString:options:)`](xmldocument/init(xmlstring:options:).md). The [`xmlData(options:)`](xmldocument/xmldata(options:).md) method takes output options.

## Topics

### Constants
- [static var documentTidyHTML: XMLNode.Options](xmlnode/options/documenttidyhtml.md)
  Formats HTML into valid XHTML during processing of the document.
- [static var documentTidyXML: XMLNode.Options](xmlnode/options/documenttidyxml.md)
  Changes malformed XML into valid XML during processing of the document.
- [static var documentValidate: XMLNode.Options](xmlnode/options/documentvalidate.md)
  Validates this document against its DTD (internal or external) or XML Schema.
- [static var documentXInclude: XMLNode.Options](xmlnode/options/documentxinclude.md)
  Replaces all XInclude nodes in the document with the nodes referred to.
- [static var documentIncludeContentTypeDeclaration: XMLNode.Options](xmlnode/options/documentincludecontenttypedeclaration.md)
  Includes a content type declaration for HTML or XHTML in the output of the document.

## See Also

- [XMLDocument.ContentKind](xmldocument/contentkind.md)
  Type used to define the kind of document content.
- [Document Content Types](document-content-types.md)
  Define document types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/input_and_output_options)*