# documentXInclude

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Replaces all XInclude nodes in the document with the nodes referred to.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
static var documentXInclude: XMLNode.Options { get }
```

```c
NSXMLDocumentXInclude
```

## Discussion

XInclude allows clients to include parts of another XML document within a document.

(Input)

## See Also

### Constants
- [static var documentTidyHTML: XMLNode.Options](./documenttidyhtml.md)
  Formats HTML into valid XHTML during processing of the document.
- [static var documentTidyXML: XMLNode.Options](./documenttidyxml.md)
  Changes malformed XML into valid XML during processing of the document.
- [static var documentValidate: XMLNode.Options](./documentvalidate.md)
  Validates this document against its DTD (internal or external) or XML Schema.
- [static var documentIncludeContentTypeDeclaration: XMLNode.Options](./documentincludecontenttypedeclaration.md)
  Includes a content type declaration for HTML or XHTML in the output of the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/options/documentxinclude)*