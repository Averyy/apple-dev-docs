# documentTidyXML

**Framework**: Foundation  
**Kind**: property

Changes malformed XML into valid XML during processing of the document.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
static var documentTidyXML: XMLNode.Options { get }
```

#### Discussion

It also eliminates “pretty-printing” formatting, such as leading tab characters. It does respect the `xml:space="preserve"` attribute.

(Input)

## See Also

- [static var documentTidyHTML: XMLNode.Options](xmlnode/options/documenttidyhtml.md)
  Formats HTML into valid XHTML during processing of the document.
- [static var documentValidate: XMLNode.Options](xmlnode/options/documentvalidate.md)
  Validates this document against its DTD (internal or external) or XML Schema.
- [static var documentXInclude: XMLNode.Options](xmlnode/options/documentxinclude.md)
  Replaces all XInclude nodes in the document with the nodes referred to.
- [static var documentIncludeContentTypeDeclaration: XMLNode.Options](xmlnode/options/documentincludecontenttypedeclaration.md)
  Includes a content type declaration for HTML or XHTML in the output of the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/options/documenttidyxml)*