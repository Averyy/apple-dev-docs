# nodePreservePrefixes

**Framework**: Foundation  
**Kind**: property

Requests NSXMLNode not to choose prefixes based on the closest namespace URI definition.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
static var nodePreservePrefixes: XMLNode.Options { get }
```

## See Also

- [static var documentIncludeContentTypeDeclaration: XMLNode.Options](xmlnode/options/documentincludecontenttypedeclaration.md)
  Includes a content type declaration for HTML or XHTML in the output of the document.
- [static var documentTidyHTML: XMLNode.Options](xmlnode/options/documenttidyhtml.md)
  Formats HTML into valid XHTML during processing of the document.
- [static var documentTidyXML: XMLNode.Options](xmlnode/options/documenttidyxml.md)
  Changes malformed XML into valid XML during processing of the document.
- [static var documentValidate: XMLNode.Options](xmlnode/options/documentvalidate.md)
  Validates this document against its DTD (internal or external) or XML Schema.
- [static var documentXInclude: XMLNode.Options](xmlnode/options/documentxinclude.md)
  Replaces all XInclude nodes in the document with the nodes referred to.
- [static var nodeCompactEmptyElement: XMLNode.Options](xmlnode/options/nodecompactemptyelement.md)
  Requests that an element should be contracted when empty; for example, `<flag/>`.
- [static var nodeExpandEmptyElement: XMLNode.Options](xmlnode/options/nodeexpandemptyelement.md)
  Requests that an element should be expanded when empty; for example, `<flag></flag>`. This is the default.
- [static var nodeIsCDATA: XMLNode.Options](xmlnode/options/nodeiscdata.md)
  Specifies that a text node contains and is written out as a CDATA section.
- [static var nodeLoadExternalEntitiesAlways: XMLNode.Options](xmlnode/options/nodeloadexternalentitiesalways.md)
  Requests that external entities are always loaded.
- [static var nodeLoadExternalEntitiesNever: XMLNode.Options](xmlnode/options/nodeloadexternalentitiesnever.md)
  Requests that external entities are never loaded.
- [static var nodeLoadExternalEntitiesSameOriginOnly: XMLNode.Options](xmlnode/options/nodeloadexternalentitiessameoriginonly.md)
  Requests that external entities are always loaded and only applies when a URL has been provided.
- [static var nodeNeverEscapeContents: XMLNode.Options](xmlnode/options/nodeneverescapecontents.md)
- [static var nodePreserveAll: XMLNode.Options](xmlnode/options/nodepreserveall.md)
- [static var nodePreserveAttributeOrder: XMLNode.Options](xmlnode/options/nodepreserveattributeorder.md)
  Requests that NSXMLNode preserve the order of attributes as in the source XML.
- [static var nodePreserveCDATA: XMLNode.Options](xmlnode/options/nodepreservecdata.md)
  Requests that NSXMLNode preserve CDATA blocks where defined in the input XML.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/options/nodepreserveprefixes)*