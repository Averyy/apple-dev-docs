# XMLDTD

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A representation of a Document Type Definition.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class XMLDTD
```

```objc
@interface NSXMLDTD : NSXMLNode
```

#### Overview

An instance of the [`XMLDTD`](./xmldtd.md) class is held as a property of an [`XMLDocument`](./xmldocument.md) instance, accessed through the [`XMLDocument`](./xmldocument.md) property [`dtd`](./xmldocument/dtd.md).

In the data model, an [`XMLDTD`](./xmldtd.md) object is conceptually similar to namespace and attribute nodes: it is not considered to be a child of the [`XMLDocument`](./xmldocument.md) object although it is closely associated with it. It is at the “root” of a shallow tree consisting primarily of nodes representing DTD declarations. Acceptable child nodes are instances of the [`XMLDTDNode`](./xmldtdnode.md) class as well as [`XMLNode`](./xmlnode.md) objects representing comment nodes and processing-instruction nodes.

You create an `NSXMLDTD` object in one of three ways:

- By processing an XML document with its own internal (in-line) DTD
- By process a standalone (external) DTD
- Programmatically

Once an [`XMLDTD`](./xmldtd.md) instance is in place, you can add, remove, and change the [`XMLDTDNode`](./xmldtdnode.md) objects representing various DTD declarations. When you write the document out as XML, the new or modified internal DTD is included (assuming you set the DTD in the [`XMLDocument`](./xmldocument.md) instance). You may also programmatically create an external DTD and write that out to its own file.

## Topics

### Initializing an NSXMLDTD Object
- [convenience init(contentsOf: URL, options: XMLNode.Options) throws](./xmldtd/init%28contentsof,options%29.md)
  Initializes and returns an `NSXMLDTD` object created from the DTD declarations in a URL-referenced source.
- [init(data: Data, options: XMLNode.Options) throws](./xmldtd/init%28data,options%29.md)
  Initializes and returns an `NSXMLDTD` object created from the DTD declarations encapsulated in an [`NSData`](./nsdata.md) object
### Managing DTD Identifiers
- [var publicID: String?](./xmldtd/publicid.md)
  Returns the receiver’s public identifier.
- [var systemID: String?](./xmldtd/systemid.md)
  Returns the receiver’s system identifier.
### Manipulating Child Nodes
- [func addChild(XMLNode)](./xmldtd/addchild%28_%29.md)
  Adds a child node to the end of the list of existing children.
- [func insertChild(XMLNode, at: Int)](./xmldtd/insertchild%28_,at%29.md)
  Inserts a child node in the receiver’s list of children at a specific location in the list.
- [func insertChildren([XMLNode], at: Int)](./xmldtd/insertchildren%28_,at%29.md)
  Inserts an array of child nodes at a specified location in the receiver’s list of children.
- [func removeChild(at: Int)](./xmldtd/removechild%28at%29.md)
  Removes the child node at a particular location in the receiver’s list of children.
- [func replaceChild(at: Int, with: XMLNode)](./xmldtd/replacechild%28at,with%29.md)
  Replaces a child at a particular index with another child.
- [func setChildren([XMLNode]?)](./xmldtd/setchildren%28_%29.md)
  Removes all existing children of the receiver and replaces them with an array of new child nodes.
### Getting DTD Nodes by Name
- [class func predefinedEntityDeclaration(forName: String) -> XMLDTDNode?](./xmldtd/predefinedentitydeclaration%28forname%29.md)
  Returns a DTD node representing the predefined entity declaration with the specified name.
- [func elementDeclaration(forName: String) -> XMLDTDNode?](./xmldtd/elementdeclaration%28forname%29.md)
  Returns the DTD node representing an element declaration for a specified element.
- [func attributeDeclaration(forName: String, elementName: String) -> XMLDTDNode?](./xmldtd/attributedeclaration%28forname,elementname%29.md)
  Returns the DTD node representing an attribute-list declaration for a given attribute and its element.
- [func entityDeclaration(forName: String) -> XMLDTDNode?](./xmldtd/entitydeclaration%28forname%29.md)
  Returns the DTD node representing the entity declaration for a specified entity.
- [func notationDeclaration(forName: String) -> XMLDTDNode?](./xmldtd/notationdeclaration%28forname%29.md)
  Returns the DTD node representing the notation declaration identified by the specified notation name.
### Initializers
- [init()](./xmldtd/init%28%29.md)
- [convenience init(contentsOfURL: URL, options: XMLNode.Options) throws](./xmldtd/init%28contentsofurl,options%29.md)

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
- [class XMLDTDNode](./xmldtdnode.md)
  A representation of element, attribute-list, entity, and notation declarations in a Document Type Definition.
- [class XMLDocument](./xmldocument.md)
  An XML document as internalized into a logical tree structure.
- [class XMLElement](./xmlelement.md)
  The element nodes in an XML tree structure.
- [class XMLNode](./xmlnode.md)
  The nodes in the abstract, logical tree structure that represents an XML document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldtd)*