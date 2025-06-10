# XMLNode.Options

**Framework**: Foundation  
**Kind**: struct

These constants are input and output options for all `NSXMLNode` objects (unless otherwise indicated), including [`XMLDocument`](xmldocument.md) objects. You can specify these options in the `NSXMLNode` methods [`init(kind:options:)`](xmlnode/init(kind:options:).md) and [`xmlString(options:)`](xmlnode/xmlstring(options:).md).

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct Options
```

#### Overview

The options with “Preserve” in their names are applicable only when external sources of XML are parsed; they have no effect on node objects that are programmatically created. Other options are used in initialization and output methods of `NSXMLDocument`; see the [`XMLDocument`](xmldocument.md) reference documentation for details.

## Topics

### Constants
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
- [static var nodePreserveCharacterReferences: XMLNode.Options](xmlnode/options/nodepreservecharacterreferences.md)
  Specifies that character references (`&#``;`) should not be resolved for XML output of this node.
- [static var nodePreserveDTD: XMLNode.Options](xmlnode/options/nodepreservedtd.md)
  Specifies that declarations in a DTD should be preserved until it the DTD is modified. For example, parameter entities are by default expanded; with this option, they are written out as they originally occur in the DTD.
- [static var nodePreserveEmptyElements: XMLNode.Options](xmlnode/options/nodepreserveemptyelements.md)
  Specifies that empty elements in the input XML be preserved in their contracted or expanded form.
- [static var nodePreserveEntities: XMLNode.Options](xmlnode/options/nodepreserveentities.md)
  Specifies that entities (`&``;`) should not be resolved for XML output of this node.
- [static var nodePreserveNamespaceOrder: XMLNode.Options](xmlnode/options/nodepreservenamespaceorder.md)
  Requests NSXML to preserve the order of namespace URI definitions as in the source XML.
- [static var nodePreservePrefixes: XMLNode.Options](xmlnode/options/nodepreserveprefixes.md)
  Requests NSXMLNode not to choose prefixes based on the closest namespace URI definition.
- [static var nodePreserveQuotes: XMLNode.Options](xmlnode/options/nodepreservequotes.md)
  Specifies that the quoting style used in the input XML (single or double quotes) be preserved.
- [static var nodePreserveWhitespace: XMLNode.Options](xmlnode/options/nodepreservewhitespace.md)
  Requests NSXMLNode to preserve whitespace characters (such as tabs and carriage returns) in the XML source that are not part of node content.
- [static var nodePrettyPrint: XMLNode.Options](xmlnode/options/nodeprettyprint.md)
  Print this node with extra space for readability. (Output)
- [static var nodePromoteSignificantWhitespace: XMLNode.Options](xmlnode/options/nodepromotesignificantwhitespace.md)
- [static var nodeUseDoubleQuotes: XMLNode.Options](xmlnode/options/nodeusedoublequotes.md)
  Requests that NSXML use double quotes for the value of an attribute or namespace node. This is the default.
- [static var nodeUseSingleQuotes: XMLNode.Options](xmlnode/options/nodeusesinglequotes.md)
  Requests that NSXML use single quotes for the value of an attribute or namespace node.
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
- [static var nodePreserveCharacterReferences: XMLNode.Options](xmlnode/options/nodepreservecharacterreferences.md)
  Specifies that character references (`&#``;`) should not be resolved for XML output of this node.
- [static var nodePreserveDTD: XMLNode.Options](xmlnode/options/nodepreservedtd.md)
  Specifies that declarations in a DTD should be preserved until it the DTD is modified. For example, parameter entities are by default expanded; with this option, they are written out as they originally occur in the DTD.
- [static var nodePreserveEmptyElements: XMLNode.Options](xmlnode/options/nodepreserveemptyelements.md)
  Specifies that empty elements in the input XML be preserved in their contracted or expanded form.
- [static var nodePreserveEntities: XMLNode.Options](xmlnode/options/nodepreserveentities.md)
  Specifies that entities (`&``;`) should not be resolved for XML output of this node.
- [static var nodePreserveNamespaceOrder: XMLNode.Options](xmlnode/options/nodepreservenamespaceorder.md)
  Requests NSXML to preserve the order of namespace URI definitions as in the source XML.
- [static var nodePreservePrefixes: XMLNode.Options](xmlnode/options/nodepreserveprefixes.md)
  Requests NSXMLNode not to choose prefixes based on the closest namespace URI definition.
- [static var nodePreserveQuotes: XMLNode.Options](xmlnode/options/nodepreservequotes.md)
  Specifies that the quoting style used in the input XML (single or double quotes) be preserved.
- [static var nodePreserveWhitespace: XMLNode.Options](xmlnode/options/nodepreservewhitespace.md)
  Requests NSXMLNode to preserve whitespace characters (such as tabs and carriage returns) in the XML source that are not part of node content.
- [static var nodePrettyPrint: XMLNode.Options](xmlnode/options/nodeprettyprint.md)
  Print this node with extra space for readability. (Output)
- [static var nodePromoteSignificantWhitespace: XMLNode.Options](xmlnode/options/nodepromotesignificantwhitespace.md)
- [static var nodeUseDoubleQuotes: XMLNode.Options](xmlnode/options/nodeusedoublequotes.md)
  Requests that NSXML use double quotes for the value of an attribute or namespace node. This is the default.
- [static var nodeUseSingleQuotes: XMLNode.Options](xmlnode/options/nodeusesinglequotes.md)
  Requests that NSXML use single quotes for the value of an attribute or namespace node.
### Initializers
- [init(rawValue: UInt)](xmlnode/options/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [XMLNode.Kind](xmlnode/kind-swift.enum.md)
  `NSXMLNode` declares the following constants of type NSXMLNodeKind for specifying a node’s kind in the initializer methods [`init(kind:)`](xmlnode/init(kind:).md) and [`init(kind:options:)`](xmlnode/init(kind:options:).md):


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/options)*