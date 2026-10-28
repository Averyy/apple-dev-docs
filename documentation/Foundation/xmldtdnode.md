# XMLDTDNode

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A representation of element, attribute-list, entity, and notation declarations in a Document Type Definition.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class XMLDTDNode
```

```objc
@interface NSXMLDTDNode : NSXMLNode
```

## Overview

[`XMLDTDNode`](./xmldtdnode.md) objects are the sole children of a [`XMLDTD`](./xmldtd.md) object (possibly along with comment nodes and processing-instruction nodes). They themselves cannot have any children.

[`XMLDTDNode`](./xmldtdnode.md) objects can be of four kinds—element, attribute-list, entity, or notation declaration—and can also be of a subkind, as specified by a [`XMLDTDNode.DTDKind`](./xmldtdnode/dtdkind-swift.enum.md) constant. For example, a DTD entity-declaration node could represent an unparsed entity declaration ([`XMLDTDNode.DTDKind.unparsed`](./xmldtdnode/dtdkind-swift.enum/unparsed.md)) rather than a parameter entity declaration ([`XMLDTDNode.DTDKind.parameter`](./xmldtdnode/dtdkind-swift.enum/parameter.md)). You can use a DTD node’s subkind to help determine how to handle the value of the node.

You can create an [`XMLDTDNode`](./xmldtdnode.md) object with the [`init(xmlString:)`](./xmldtdnode/init%28xmlstring%29-1dyhd.md) method, the [`XMLNode`](./xmlnode.md) class method [`dtdNode(withXMLString:)`](./xmlnode/dtdnode%28withxmlstring%29.md), or with the [`XMLNode`](./xmlnode.md) initializer [`init(kind:options:)`](./xmlnode/init%28kind,options%29.md) (in the latter method supplying the appropriate [`XMLNode.Kind`](./xmlnode/kind-swift.enum.md) constant).

Setting the object value or string value of an [`XMLDTDNode`](./xmldtdnode.md) objects affects different parts of different kinds of declaration. See the related programming topic for more information.

## Topics

### Initializing an NSXMLDTDNode Object
- [init?(xmlString: String)](./xmldtdnode/init%28xmlstring%29-1dyhd.md)
  Returns an `NSXMLDTDNode` object initialized with the DTD declaration in a given string.
### Managing the DTD Node Kind
- [var dtdKind: XMLDTDNode.DTDKind](./xmldtdnode/dtdkind-swift.property.md)
  Returns the receiver’s DTD kind.
### Managing DTD Identifiers
- [var isExternal: Bool](./xmldtdnode/isexternal.md)
  True if the system id is set. Valid for entities and notations.
- [var notationName: String?](./xmldtdnode/notationname.md)
  Returns the name of the notation associated with the receiver.
- [var publicID: String?](./xmldtdnode/publicid.md)
  Returns the public identifier associated with the receiver.
- [var systemID: String?](./xmldtdnode/systemid.md)
  Returns the system identifier associated with the receiver.
### Constants
- [XMLDTDNode.DTDKind](./xmldtdnode/dtdkind-swift.enum.md)
  The type defined for the constants that specify the kind and subkind of DTD declaration represented by an `NSXMLDTDNode` object. You set the DTD-node kind using the doc:nsxmldtdnode/1806486-setdtdkind method.
- [DTD Node Kind Constants](./dtd_node_kind_constants.md)
  Constants that specify the kind and subkind of DTD declaration represented by an `NSXMLDTDNode` object. You set the DTD-node kind using the doc:nsxmldtdnode/1806486-setdtdkind method.
### Initializers
- [init()](./xmldtdnode/init%28%29.md)
- [init?(XMLString: String)](./xmldtdnode/init%28xmlstring%29-1bnga.md)
- [init(kind: XMLNode.Kind, options: XMLNode.Options)](./xmldtdnode/init%28kind,options%29.md)

## Relationships

### Inherits From
- [XMLNode](./xmlnode.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](./nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Tree-Based Processing
- [class XMLDTD](./xmldtd.md)
  A representation of a Document Type Definition.
- [class XMLDocument](./xmldocument.md)
  An XML document as internalized into a logical tree structure.
- [class XMLElement](./xmlelement.md)
  The element nodes in an XML tree structure.
- [class XMLNode](./xmlnode.md)
  The nodes in the abstract, logical tree structure that represents an XML document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldtdnode)*