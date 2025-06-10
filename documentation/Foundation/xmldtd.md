# XMLDTD

**Framework**: Foundation  
**Kind**: class

A representation of a Document Type Definition.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class XMLDTD
```

#### Overview

An instance of the [`XMLDTD`](xmldtd.md) class is held as a property of an [`XMLDocument`](xmldocument.md) instance, accessed through the [`XMLDocument`](xmldocument.md) property [`dtd`](xmldocument/dtd.md).

In the data model, an [`XMLDTD`](xmldtd.md) object is conceptually similar to namespace and attribute nodes: it is not considered to be a child of the [`XMLDocument`](xmldocument.md) object although it is closely associated with it. It is at the “root” of a shallow tree consisting primarily of nodes representing DTD declarations. Acceptable child nodes are instances of the [`XMLDTDNode`](xmldtdnode.md) class as well as [`XMLNode`](xmlnode.md) objects representing comment nodes and processing-instruction nodes.

You create an `NSXMLDTD` object in one of three ways:

- By processing an XML document with its own internal (in-line) DTD
- By process a standalone (external) DTD
- Programmatically

Once an [`XMLDTD`](xmldtd.md) instance is in place, you can add, remove, and change the [`XMLDTDNode`](xmldtdnode.md) objects representing various DTD declarations. When you write the document out as XML, the new or modified internal DTD is included (assuming you set the DTD in the [`XMLDocument`](xmldocument.md) instance). You may also programmatically create an external DTD and write that out to its own file.

## Topics

### Initializing an NSXMLDTD Object
- [convenience init(contentsOf: URL, options: XMLNode.Options) throws](xmldtd/init(contentsof:options:).md)
  Initializes and returns an `NSXMLDTD` object created from the DTD declarations in a URL-referenced source.
- [init(data: Data, options: XMLNode.Options) throws](xmldtd/init(data:options:).md)
  Initializes and returns an `NSXMLDTD` object created from the DTD declarations encapsulated in an [`NSData`](nsdata.md) object
### Managing DTD Identifiers
- [var publicID: String?](xmldtd/publicid.md)
  Returns the receiver’s public identifier.
- [var systemID: String?](xmldtd/systemid.md)
  Returns the receiver’s system identifier.
### Manipulating Child Nodes
- [func addChild(XMLNode)](xmldtd/addchild(_:).md)
  Adds a child node to the end of the list of existing children.
- [func insertChild(XMLNode, at: Int)](xmldtd/insertchild(_:at:).md)
  Inserts a child node in the receiver’s list of children at a specific location in the list.
- [func insertChildren([XMLNode], at: Int)](xmldtd/insertchildren(_:at:).md)
  Inserts an array of child nodes at a specified location in the receiver’s list of children.
- [func removeChild(at: Int)](xmldtd/removechild(at:).md)
  Removes the child node at a particular location in the receiver’s list of children.
- [func replaceChild(at: Int, with: XMLNode)](xmldtd/replacechild(at:with:).md)
  Replaces a child at a particular index with another child.
- [func setChildren([XMLNode]?)](xmldtd/setchildren(_:).md)
  Removes all existing children of the receiver and replaces them with an array of new child nodes.
### Getting DTD Nodes by Name
- [class func predefinedEntityDeclaration(forName: String) -> XMLDTDNode?](xmldtd/predefinedentitydeclaration(forname:).md)
  Returns a DTD node representing the predefined entity declaration with the specified name.
- [func elementDeclaration(forName: String) -> XMLDTDNode?](xmldtd/elementdeclaration(forname:).md)
  Returns the DTD node representing an element declaration for a specified element.
- [func attributeDeclaration(forName: String, elementName: String) -> XMLDTDNode?](xmldtd/attributedeclaration(forname:elementname:).md)
  Returns the DTD node representing an attribute-list declaration for a given attribute and its element.
- [func entityDeclaration(forName: String) -> XMLDTDNode?](xmldtd/entitydeclaration(forname:).md)
  Returns the DTD node representing the entity declaration for a specified entity.
- [func notationDeclaration(forName: String) -> XMLDTDNode?](xmldtd/notationdeclaration(forname:).md)
  Returns the DTD node representing the notation declaration identified by the specified notation name.
### Initializers
- [init()](xmldtd/init.md)

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

- [class XMLDTDNode](xmldtdnode.md)
  A representation of element, attribute-list, entity, and notation declarations in a Document Type Definition.
- [class XMLDocument](xmldocument.md)
  An XML document as internalized into a logical tree structure.
- [class XMLElement](xmlelement.md)
  The element nodes in an XML tree structure.
- [class XMLNode](xmlnode.md)
  The nodes in the abstract, logical tree structure that represents an XML document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldtd)*