# XMLElement

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

The element nodes in an XML tree structure.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class XMLElement
```

```objc
@interface NSXMLElement : NSXMLNode
```

## Mentions

- [setURI:](./nsxmlnode-seturi.md)

## Overview

An [`XMLElement`](./xmlelement.md) object may have child nodes, specifically comment nodes, processing-instruction nodes, text nodes, and other [`XMLElement`](./xmlelement.md) nodes. It may also have attribute nodes and namespace nodes associated with it (however, namespace and attribute nodes are not considered children). Any attempt to add a [`XMLDocument`](./xmldocument.md) node, [`XMLDTD`](./xmldtd.md) node, namespace node, or attribute node as a child raises an exception. If you add a child node to an [`XMLElement`](./xmlelement.md) object and that child already has a parent, [`XMLElement`](./xmlelement.md) raises an exception; the child must be detached or copied first.

### Subclassing Notes

You can subclass `NSXMLElement` if you want element nodes with more specialized attributes or behavior, for example, paragraph and font attributes that specify how the string value of the element should appear.

#### Methods to Override

To subclass `NSXMLElement` you need to override the primary initializer, [`init(name:uri:)`](./xmlelement/init%28name,uri%29-1r286.md), and the methods listed below. In most cases, you need only invoke the superclass implementation, adding any subclass-specific code before or after the invocation, as necessary.

| [`addAttribute(_:)`](./xmlelement/addattribute%28_%29.md) | [`removeNamespace(forPrefix:)`](./xmlelement/removenamespace%28forprefix%29.md) |
| --- | --- |
| [`removeAttribute(forName:)`](./xmlelement/removeattribute%28forname%29.md) | [`namespaces`](./xmlelement/namespaces.md) |
| [`attributes`](./xmlelement/attributes.md) | [`namespaces`](./xmlelement/namespaces.md) |
| [`attribute(forLocalName:uri:)`](./xmlelement/attribute%28forlocalname,uri%29.md) | [`insertChild(_:at:)`](./xmlelement/insertchild%28_,at%29.md) |
| [`attributes`](./xmlelement/attributes.md) | [`removeChild(at:)`](./xmlelement/removechild%28at%29.md) |
| [`addNamespace(_:)`](./xmlelement/addnamespace%28_%29.md) | [`setChildren(_:)`](./xmlelement/setchildren%28_%29.md) |

`NSXMLElement` implements  [`isEqual(_:)`](../ObjectiveC/nsobjectprotocol/isequal%28_%29.md) to perform a deep comparison: two [`XMLDocument`](./xmldocument.md) objects are not considered equal unless they have the same name, same child nodes, same attributes, and so on. If you want a different standard of comparison, override `isEqual:`.

#### Special Considerations

Because of the architecture and data model of NSXML, when it parses and processes a source of XML it cannot know about your subclass unless you override the class method [`replacementClass(for:)`](./xmldocument/replacementclass%28for%29.md) to return your custom class in place of an NSXML class. If your custom class has no direct NSXML counterpart—for example, it is a subclass of `NSXMLNode` that represents CDATA sections—then you can walk the tree after it has been created and insert the new node where appropriate.

Note that you can safely set the root element of the XML document (using the `NSXMLDocument` [`setRootElement(_:)`](./xmldocument/setrootelement%28_%29.md)method) to be an instance of your subclass because this method only checks to see if the added node is of an element kind (`NSXMLElementKind`). These precautions do not apply, of course, if you are creating an XML tree programmatically.

## Topics

### Initializing NSXMLElement Objects
- [convenience init(name: String)](./xmlelement/init%28name%29.md)
  Returns an `NSXMLElement` object initialized with the specified name.
- [convenience init(name: String, stringValue: String?)](./xmlelement/init%28name,stringvalue%29.md)
  Returns an `NSXMLElement` object initialized with a specified name and a single text-node child containing a specified value.
- [init(name: String, uri: String?)](./xmlelement/init%28name,uri%29-1r286.md)
  Returns an `NSXMLElement` object initialized with the specified name and URI.
- [init(xmlString: String) throws](./xmlelement/init%28xmlstring%29-7vkg7.md)
  Returns an `NSXMLElement` object created from a specified string containing XML markup.
- [convenience init(kind: XMLNode.Kind, options: XMLNode.Options)](./xmlelement/init%28kind,options%29.md)
### Obtaining Child Elements
- [func elements(forName: String) -> [XMLElement]](./xmlelement/elements%28forname%29.md)
  Returns the child element nodes (as `NSXMLElement` objects) of the receiver that have a specified name.
- [func elements(forLocalName: String, uri: String?) -> [XMLElement]](./xmlelement/elements%28forlocalname,uri%29.md)
  Returns the child element nodes (as `NSXMLElement` objects) of the receiver that are matched with the specified local name and URI.
### Manipulating Child Elements
- [func addChild(XMLNode)](./xmlelement/addchild%28_%29.md)
  Adds a child node at the end of the receiver’s current list of children.
- [func insertChild(XMLNode, at: Int)](./xmlelement/insertchild%28_,at%29.md)
  Inserts a new child node at a specified location in the receiver’s list of child nodes.
- [func insertChildren([XMLNode], at: Int)](./xmlelement/insertchildren%28_,at%29.md)
  Inserts an array of child nodes at a specified location in the receiver’s list of children.
- [func removeChild(at: Int)](./xmlelement/removechild%28at%29.md)
  Removes the child node of the receiver identified by a given index.
- [func replaceChild(at: Int, with: XMLNode)](./xmlelement/replacechild%28at,with%29.md)
  Replaces a child node at a specified location with another child node.
- [func setChildren([XMLNode]?)](./xmlelement/setchildren%28_%29.md)
  Sets all child nodes of the receiver at once, replacing any existing children.
- [func normalizeAdjacentTextNodesPreservingCDATA(Bool)](./xmlelement/normalizeadjacenttextnodespreservingcdata%28_%29.md)
  Coalesces adjacent text nodes of the receiver that you have explicitly added, optionally including CDATA sections.
### Handling Attributes
- [func addAttribute(XMLNode)](./xmlelement/addattribute%28_%29.md)
  Adds an attribute node to the receiver.
- [func attribute(forName: String) -> XMLNode?](./xmlelement/attribute%28forname%29.md)
  Returns the attribute node of the receiver with the specified name.
- [func attribute(forLocalName: String, uri: String?) -> XMLNode?](./xmlelement/attribute%28forlocalname,uri%29.md)
  Returns the attribute node of the receiver that is identified by a local name and URI.
- [var attributes: [XMLNode]?](./xmlelement/attributes.md)
  Sets all attributes of the receiver at once, replacing any existing attribute nodes.
- [func removeAttribute(forName: String)](./xmlelement/removeattribute%28forname%29.md)
  Removes an attribute node identified by name.
- [func setAttributesWith([String : String])](./xmlelement/setattributeswith%28_%29.md)
  Sets the attributes of the receiver based on the key-value pairs specified in the passed dictionary.
- [func setAttributesAs([AnyHashable : Any])](./xmlelement/setattributesas%28_%29.md)
  Sets the attributes of the receiver based on the key-value pairs specified in the passed-in dictionary.
### Setting Element URI
- [setURI:](./nsxmlnode-seturi.md)
  Sets the URI of the receiver.
### Handling Namespaces
- [func addNamespace(XMLNode)](./xmlelement/addnamespace%28_%29.md)
  Adds a namespace node to the receiver.
- [var namespaces: [XMLNode]?](./xmlelement/namespaces.md)
  Sets all of the namespace nodes of the receiver at once, replacing any existing namespace nodes.
- [func namespace(forPrefix: String) -> XMLNode?](./xmlelement/namespace%28forprefix%29.md)
  Returns the namespace node with a specified prefix.
- [func removeNamespace(forPrefix: String)](./xmlelement/removenamespace%28forprefix%29.md)
  Removes a namespace node that is identified by a given prefix.
- [func resolveNamespace(forName: String) -> XMLNode?](./xmlelement/resolvenamespace%28forname%29.md)
  Returns the namespace node with the prefix matching the given qualified name.
- [func resolvePrefix(forNamespaceURI: String) -> String?](./xmlelement/resolveprefix%28fornamespaceuri%29.md)
  Returns the prefix associated with the specified URI.
### Initializers
- [init(XMLString: String) throws](./xmlelement/init%28xmlstring%29-1wgno.md)
- [init(name: String, URI: String?)](./xmlelement/init%28name,uri%29-67uti.md)

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
- [class XMLDTDNode](./xmldtdnode.md)
  A representation of element, attribute-list, entity, and notation declarations in a Document Type Definition.
- [class XMLDocument](./xmldocument.md)
  An XML document as internalized into a logical tree structure.
- [class XMLNode](./xmlnode.md)
  The nodes in the abstract, logical tree structure that represents an XML document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement)*