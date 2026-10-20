# nodePreserveEntities

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Specifies that entities (`&`*xyz*`;`) should not be resolved for XML output of this node.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
static var nodePreserveEntities: XMLNode.Options { get }
```

```c
NSXMLNodePreserveEntities
```

## See Also

### Constants
- [static var documentIncludeContentTypeDeclaration: XMLNode.Options](./documentincludecontenttypedeclaration.md)
  Includes a content type declaration for HTML or XHTML in the output of the document.
- [static var documentTidyHTML: XMLNode.Options](./documenttidyhtml.md)
  Formats HTML into valid XHTML during processing of the document.
- [static var documentTidyXML: XMLNode.Options](./documenttidyxml.md)
  Changes malformed XML into valid XML during processing of the document.
- [static var documentValidate: XMLNode.Options](./documentvalidate.md)
  Validates this document against its DTD (internal or external) or XML Schema.
- [static var documentXInclude: XMLNode.Options](./documentxinclude.md)
  Replaces all XInclude nodes in the document with the nodes referred to.
- [static var nodeCompactEmptyElement: XMLNode.Options](./nodecompactemptyelement.md)
  Requests that an element should be contracted when empty; for example, `<flag/>`.
- [static var nodeExpandEmptyElement: XMLNode.Options](./nodeexpandemptyelement.md)
  Requests that an element should be expanded when empty; for example, `<flag></flag>`. This is the default.
- [static var nodeIsCDATA: XMLNode.Options](./nodeiscdata.md)
  Specifies that a text node contains and is written out as a CDATA section.
- [static var nodeLoadExternalEntitiesAlways: XMLNode.Options](./nodeloadexternalentitiesalways.md)
  Requests that external entities are always loaded.
- [static var nodeLoadExternalEntitiesNever: XMLNode.Options](./nodeloadexternalentitiesnever.md)
  Requests that external entities are never loaded.
- [static var nodeLoadExternalEntitiesSameOriginOnly: XMLNode.Options](./nodeloadexternalentitiessameoriginonly.md)
  Requests that external entities are always loaded and only applies when a URL has been provided.
- [static var nodeNeverEscapeContents: XMLNode.Options](./nodeneverescapecontents.md)
- [static var nodePreserveAll: XMLNode.Options](./nodepreserveall.md)
- [static var nodePreserveAttributeOrder: XMLNode.Options](./nodepreserveattributeorder.md)
  Requests that NSXMLNode preserve the order of attributes as in the source XML.
- [static var nodePreserveCDATA: XMLNode.Options](./nodepreservecdata.md)
  Requests that NSXMLNode preserve CDATA blocks where defined in the input XML.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/options/nodepreserveentities)*