# XMLNode.Options

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

These constants are input and output options for all `NSXMLNode` objects (unless otherwise indicated), including [`XMLDocument`](../xmldocument.md) objects. You can specify these options in the `NSXMLNode` methods [`init(kind:options:)`](./init%28kind,options%29.md) and [`xmlString(options:)`](./xmlstring%28options%29.md).

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct Options
```

```c
enum NSXMLNodeOptions : NSUInteger;
```

#### Overview

The options with “Preserve” in their names are applicable only when external sources of XML are parsed; they have no effect on node objects that are programmatically created. Other options are used in initialization and output methods of `NSXMLDocument`; see the [`XMLDocument`](../xmldocument.md) reference documentation for details.

## Topics

### Constants
- [static var documentIncludeContentTypeDeclaration: XMLNode.Options](./options/documentincludecontenttypedeclaration.md)
  Includes a content type declaration for HTML or XHTML in the output of the document.
- [static var documentTidyHTML: XMLNode.Options](./options/documenttidyhtml.md)
  Formats HTML into valid XHTML during processing of the document.
- [static var documentTidyXML: XMLNode.Options](./options/documenttidyxml.md)
  Changes malformed XML into valid XML during processing of the document.
- [static var documentValidate: XMLNode.Options](./options/documentvalidate.md)
  Validates this document against its DTD (internal or external) or XML Schema.
- [static var documentXInclude: XMLNode.Options](./options/documentxinclude.md)
  Replaces all XInclude nodes in the document with the nodes referred to.
- [static var nodeCompactEmptyElement: XMLNode.Options](./options/nodecompactemptyelement.md)
  Requests that an element should be contracted when empty; for example, `<flag/>`.
- [static var nodeExpandEmptyElement: XMLNode.Options](./options/nodeexpandemptyelement.md)
  Requests that an element should be expanded when empty; for example, `<flag></flag>`. This is the default.
- [static var nodeIsCDATA: XMLNode.Options](./options/nodeiscdata.md)
  Specifies that a text node contains and is written out as a CDATA section.
- [static var nodeLoadExternalEntitiesAlways: XMLNode.Options](./options/nodeloadexternalentitiesalways.md)
  Requests that external entities are always loaded.
- [static var nodeLoadExternalEntitiesNever: XMLNode.Options](./options/nodeloadexternalentitiesnever.md)
  Requests that external entities are never loaded.
- [static var nodeLoadExternalEntitiesSameOriginOnly: XMLNode.Options](./options/nodeloadexternalentitiessameoriginonly.md)
  Requests that external entities are always loaded and only applies when a URL has been provided.
- [static var nodeNeverEscapeContents: XMLNode.Options](./options/nodeneverescapecontents.md)
- [static var nodePreserveAll: XMLNode.Options](./options/nodepreserveall.md)
- [static var nodePreserveAttributeOrder: XMLNode.Options](./options/nodepreserveattributeorder.md)
  Requests that NSXMLNode preserve the order of attributes as in the source XML.
- [static var nodePreserveCDATA: XMLNode.Options](./options/nodepreservecdata.md)
  Requests that NSXMLNode preserve CDATA blocks where defined in the input XML.
- [static var nodePreserveCharacterReferences: XMLNode.Options](./options/nodepreservecharacterreferences.md)
  Specifies that character references (`&#`*nnn*`;`) should not be resolved for XML output of this node.
- [static var nodePreserveDTD: XMLNode.Options](./options/nodepreservedtd.md)
  Specifies that declarations in a DTD should be preserved until it the DTD is modified. For example, parameter entities are by default expanded; with this option, they are written out as they originally occur in the DTD.
- [static var nodePreserveEmptyElements: XMLNode.Options](./options/nodepreserveemptyelements.md)
  Specifies that empty elements in the input XML be preserved in their contracted or expanded form.
- [static var nodePreserveEntities: XMLNode.Options](./options/nodepreserveentities.md)
  Specifies that entities (`&`*xyz*`;`) should not be resolved for XML output of this node.
- [static var nodePreserveNamespaceOrder: XMLNode.Options](./options/nodepreservenamespaceorder.md)
  Requests NSXML to preserve the order of namespace URI definitions as in the source XML.
- [static var nodePreservePrefixes: XMLNode.Options](./options/nodepreserveprefixes.md)
  Requests NSXMLNode not to choose prefixes based on the closest namespace URI definition.
- [static var nodePreserveQuotes: XMLNode.Options](./options/nodepreservequotes.md)
  Specifies that the quoting style used in the input XML (single or double quotes) be preserved.
- [static var nodePreserveWhitespace: XMLNode.Options](./options/nodepreservewhitespace.md)
  Requests NSXMLNode to preserve whitespace characters (such as tabs and carriage returns) in the XML source that are not part of node content.
- [static var nodePrettyPrint: XMLNode.Options](./options/nodeprettyprint.md)
  Print this node with extra space for readability. (Output)
- [static var nodePromoteSignificantWhitespace: XMLNode.Options](./options/nodepromotesignificantwhitespace.md)
- [static var nodeUseDoubleQuotes: XMLNode.Options](./options/nodeusedoublequotes.md)
  Requests that NSXML use double quotes for the value of an attribute or namespace node. This is the default.
- [static var nodeUseSingleQuotes: XMLNode.Options](./options/nodeusesinglequotes.md)
  Requests that NSXML use single quotes for the value of an attribute or namespace node.
### Initializers
- [init(rawValue: UInt)](./options/init%28rawvalue%29.md)
### Enumeration Cases
- [NSXMLNodeOptionsNone](../nsxmlnodeoptions/nsxmlnodeoptionsnone.md)
  No options are requested for this input or output action.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Constants
- [XMLNode.Kind](./kind-swift.enum.md)
  `NSXMLNode` declares the following constants of type NSXMLNodeKind for specifying a node’s kind in the initializer methods [`init(kind:)`](./init%28kind%29.md) and [`init(kind:options:)`](./init%28kind,options%29.md):
- [NSXMLNodeOptionsNone](../nsxmlnodeoptions/nsxmlnodeoptionsnone.md)
  No options are requested for this input or output action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/options)*