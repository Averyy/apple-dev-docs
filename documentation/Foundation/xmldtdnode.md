# XMLDTDNode

**Framework**: Foundation  
**Kind**: class

A representation of element, attribute-list, entity, and notation declarations in a Document Type Definition.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class XMLDTDNode
```

#### Overview

[`XMLDTDNode`](xmldtdnode.md) objects are the sole children of a [`XMLDTD`](xmldtd.md) object (possibly along with comment nodes and processing-instruction nodes). They themselves cannot have any children.

[`XMLDTDNode`](xmldtdnode.md) objects can be of four kinds—element, attribute-list, entity, or notation declaration—and can also be of a subkind, as specified by a [`XMLDTDNode.DTDKind`](xmldtdnode/dtdkind-swift.enum.md) constant. For example, a DTD entity-declaration node could represent an unparsed entity declaration ([`XMLDTDNode.DTDKind.unparsed`](xmldtdnode/dtdkind-swift.enum/unparsed.md)) rather than a parameter entity declaration ([`XMLDTDNode.DTDKind.parameter`](xmldtdnode/dtdkind-swift.enum/parameter.md)). You can use a DTD node’s subkind to help determine how to handle the value of the node.

You can create an [`XMLDTDNode`](xmldtdnode.md) object with the [`init(xmlString:)`](xmldtdnode/init(xmlstring:).md) method, the [`XMLNode`](xmlnode.md) class method [`dtdNode(withXMLString:)`](xmlnode/dtdnode(withxmlstring:).md), or with the [`XMLNode`](xmlnode.md) initializer [`init(kind:options:)`](xmlnode/init(kind:options:).md) (in the latter method supplying the appropriate [`XMLNode.Kind`](xmlnode/kind-swift.enum.md) constant).

Setting the object value or string value of an [`XMLDTDNode`](xmldtdnode.md) objects affects different parts of different kinds of declaration. See the related programming topic for more information.

## Topics

### Initializing an NSXMLDTDNode Object
- [init?(xmlString: String)](xmldtdnode/init(xmlstring:).md)
  Returns an `NSXMLDTDNode` object initialized with the DTD declaration in a given string.
### Managing the DTD Node Kind
- [var dtdKind: XMLDTDNode.DTDKind](xmldtdnode/dtdkind-swift.property.md)
  Returns the receiver’s DTD kind.
### Managing DTD Identifiers
- [var isExternal: Bool](xmldtdnode/isexternal.md)
- [var notationName: String?](xmldtdnode/notationname.md)
  Returns the name of the notation associated with the receiver.
- [var publicID: String?](xmldtdnode/publicid.md)
  Returns the public identifier associated with the receiver.
- [var systemID: String?](xmldtdnode/systemid.md)
  Returns the system identifier associated with the receiver.
### Constants
- [XMLDTDNode.DTDKind](xmldtdnode/dtdkind-swift.enum.md)
  The type defined for the constants that specify the kind and subkind of DTD declaration represented by an `NSXMLDTDNode` object. You set the DTD-node kind using the doc:nsxmldtdnode/1806486-setdtdkind method.
- [DTD Node Kind Constants](dtd_node_kind_constants.md)
  Constants that specify the kind and subkind of DTD declaration represented by an `NSXMLDTDNode` object. You set the DTD-node kind using the doc:nsxmldtdnode/1806486-setdtdkind method.
### Initializers
- [init()](xmldtdnode/init.md)
- [init(kind: XMLNode.Kind, options: XMLNode.Options)](xmldtdnode/init(kind:options:).md)

## Relationships

### Inherits From
- [XMLNode](xmlnode.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class XMLDTD](xmldtd.md)
  A representation of a Document Type Definition.
- [class XMLDocument](xmldocument.md)
  An XML document as internalized into a logical tree structure.
- [class XMLElement](xmlelement.md)
  The element nodes in an XML tree structure.
- [class XMLNode](xmlnode.md)
  The nodes in the abstract, logical tree structure that represents an XML document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldtdnode)*