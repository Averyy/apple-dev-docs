# documentTidyHTML

**Framework**: Foundation  
**Kind**: property

Formats HTML into valid XHTML during processing of the document.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
static var documentTidyHTML: XMLNode.Options { get }
```

#### Discussion

When tidying, `NSXMLDocument` adds a line break before the close tag of a block-level element (`<p>`, `<div>`, `<h1>`, and so on); it also makes the string value of `<br>` or `<hr>` a line break. These operations make the string value of the HTML `<body>` more readable. After using this option, avoid outputting the document as anything other than the default kind, `NSXMLDocumentXHTMLKind`.

(Input)

## See Also

- [static var documentTidyXML: XMLNode.Options](xmlnode/options/documenttidyxml.md)
  Changes malformed XML into valid XML during processing of the document.
- [static var documentValidate: XMLNode.Options](xmlnode/options/documentvalidate.md)
  Validates this document against its DTD (internal or external) or XML Schema.
- [static var documentXInclude: XMLNode.Options](xmlnode/options/documentxinclude.md)
  Replaces all XInclude nodes in the document with the nodes referred to.
- [static var documentIncludeContentTypeDeclaration: XMLNode.Options](xmlnode/options/documentincludecontenttypedeclaration.md)
  Includes a content type declaration for HTML or XHTML in the output of the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/options/documenttidyhtml)*