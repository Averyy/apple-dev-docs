# documentXInclude

**Framework**: Foundation  
**Kind**: property

Replaces all XInclude nodes in the document with the nodes referred to.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
static var documentXInclude: XMLNode.Options { get }
```

#### Discussion

XInclude allows clients to include parts of another XML document within a document.

(Input)

## See Also

- [static var documentTidyHTML: XMLNode.Options](xmlnode/options/documenttidyhtml.md)
  Formats HTML into valid XHTML during processing of the document.
- [static var documentTidyXML: XMLNode.Options](xmlnode/options/documenttidyxml.md)
  Changes malformed XML into valid XML during processing of the document.
- [static var documentValidate: XMLNode.Options](xmlnode/options/documentvalidate.md)
  Validates this document against its DTD (internal or external) or XML Schema.
- [static var documentIncludeContentTypeDeclaration: XMLNode.Options](xmlnode/options/documentincludecontenttypedeclaration.md)
  Includes a content type declaration for HTML or XHTML in the output of the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/options/documentxinclude)*