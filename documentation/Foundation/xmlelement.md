# XMLElement

**Framework**: Foundation  
**Kind**: class

The element nodes in an XML tree structure.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class XMLElement
```

## Mentions

- [setURI:](1806643-seturi.md)

#### Overview

An [`XMLElement`](xmlelement.md) object may have child nodes, specifically comment nodes, processing-instruction nodes, text nodes, and other [`XMLElement`](xmlelement.md) nodes. It may also have attribute nodes and namespace nodes associated with it (however, namespace and attribute nodes are not considered children). Any attempt to add a [`XMLDocument`](xmldocument.md) node, [`XMLDTD`](xmldtd.md) node, namespace node, or attribute node as a child raises an exception. If you add a child node to an [`XMLElement`](xmlelement.md) object and that child already has a parent, [`XMLElement`](xmlelement.md) raises an exception; the child must be detached or copied first.

##### Subclassing Notes

You can subclass `NSXMLElement` if you want element nodes with more specialized attributes or behavior, for example, paragraph and font attributes that specify how the string value of the element should appear.

###### Methods to Override

To subclass `NSXMLElement` you need to override the primary initializer, [`init(name:uri:)`](xmlelement/init(name:uri:).md), and the methods listed below. In most cases, you need only invoke the superclass implementation, adding any subclass-specific code before or after the invocation, as necessary.

| [`addAttribute(_:)`](xmlelement/addattribute(_:).md) | [`removeNamespace(forPrefix:)`](xmlelement/removenamespace(forprefix:).md) |
| --- | --- |
| [`removeAttribute(forName:)`](xmlelement/removeattribute(forname:).md) | [`namespaces`](xmlelement/namespaces.md) |
| [`attributes`](xmlelement/attributes.md) | [`namespaces`](xmlelement/namespaces.md) |
| [`attribute(forLocalName:uri:)`](xmlelement/attribute(forlocalname:uri:).md) | [`insertChild(_:at:)`](xmlelement/insertchild(_:at:).md) |
| [`attributes`](xmlelement/attributes.md) | [`removeChild(at:)`](xmlelement/removechild(at:).md) |
| [`addNamespace(_:)`](xmlelement/addnamespace(_:).md) | [`setChildren(_:)`](xmlelement/setchildren(_:).md) |

`NSXMLElement` implements  [`isEqual(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/isEqual(_:)) to perform a deep comparison: two [`XMLDocument`](xmldocument.md) objects are not considered equal unless they have the same name, same child nodes, same attributes, and so on. If you want a different standard of comparison, override `isEqual:`.

###### Special Considerations

Because of the architecture and data model of NSXML, when it parses and processes a source of XML it cannot know about your subclass unless you override the class method [`replacementClass(for:)`](xmldocument/replacementclass(for:).md) to return your custom class in place of an NSXML class. If your custom class has no direct NSXML counterpart—for example, it is a subclass of `NSXMLNode` that represents CDATA sections—then you can walk the tree after it has been created and insert the new node where appropriate.

Note that you can safely set the root element of the XML document (using the `NSXMLDocument` [`setRootElement(_:)`](xmldocument/setrootelement(_:).md)method) to be an instance of your subclass because this method only checks to see if the added node is of an element kind (`NSXMLElementKind`). These precautions do not apply, of course, if you are creating an XML tree programmatically.

## Topics

### Initializing NSXMLElement Objects
- [convenience init(name: String)](xmlelement/init(name:).md)
  Returns an `NSXMLElement` object initialized with the specified name.
- [convenience init(name: String, stringValue: String?)](xmlelement/init(name:stringvalue:).md)
  Returns an `NSXMLElement` object initialized with a specified name and a single text-node child containing a specified value.
- [init(name: String, uri: String?)](xmlelement/init(name:uri:).md)
  Returns an `NSXMLElement` object initialized with the specified name and URI.
- [init(xmlString: String) throws](xmlelement/init(xmlstring:).md)
  Returns an `NSXMLElement` object created from a specified string containing XML markup.
- [convenience init(kind: XMLNode.Kind, options: XMLNode.Options)](xmlelement/init(kind:options:).md)
### Obtaining Child Elements
- [func elements(forName: String) -> [XMLElement]](xmlelement/elements(forname:).md)
  Returns the child element nodes (as `NSXMLElement` objects) of the receiver that have a specified name.
- [func elements(forLocalName: String, uri: String?) -> [XMLElement]](xmlelement/elements(forlocalname:uri:).md)
  Returns the child element nodes (as `NSXMLElement` objects) of the receiver that are matched with the specified local name and URI.
### Manipulating Child Elements
- [func addChild(XMLNode)](xmlelement/addchild(_:).md)
  Adds a child node at the end of the receiver’s current list of children.
- [func insertChild(XMLNode, at: Int)](xmlelement/insertchild(_:at:).md)
  Inserts a new child node at a specified location in the receiver’s list of child nodes.
- [func insertChildren([XMLNode], at: Int)](xmlelement/insertchildren(_:at:).md)
  Inserts an array of child nodes at a specified location in the receiver’s list of children.
- [func removeChild(at: Int)](xmlelement/removechild(at:).md)
  Removes the child node of the receiver identified by a given index.
- [func replaceChild(at: Int, with: XMLNode)](xmlelement/replacechild(at:with:).md)
  Replaces a child node at a specified location with another child node.
- [func setChildren([XMLNode]?)](xmlelement/setchildren(_:).md)
  Sets all child nodes of the receiver at once, replacing any existing children.
- [func normalizeAdjacentTextNodesPreservingCDATA(Bool)](xmlelement/normalizeadjacenttextnodespreservingcdata(_:).md)
  Coalesces adjacent text nodes of the receiver that you have explicitly added, optionally including CDATA sections.
### Handling Attributes
- [func addAttribute(XMLNode)](xmlelement/addattribute(_:).md)
  Adds an attribute node to the receiver.
- [func attribute(forName: String) -> XMLNode?](xmlelement/attribute(forname:).md)
  Returns the attribute node of the receiver with the specified name.
- [func attribute(forLocalName: String, uri: String?) -> XMLNode?](xmlelement/attribute(forlocalname:uri:).md)
  Returns the attribute node of the receiver that is identified by a local name and URI.
- [var attributes: [XMLNode]?](xmlelement/attributes.md)
  Sets all attributes of the receiver at once, replacing any existing attribute nodes.
- [func removeAttribute(forName: String)](xmlelement/removeattribute(forname:).md)
  Removes an attribute node identified by name.
- [func setAttributesWith([String : String])](xmlelement/setattributeswith(_:).md)
  Sets the attributes of the receiver based on the key-value pairs specified in the passed dictionary.
- [func setAttributesAs([AnyHashable : Any])](xmlelement/setattributesas(_:).md)
  Sets the attributes of the receiver based on the key-value pairs specified in the passed-in dictionary.
### Handling Namespaces
- [func addNamespace(XMLNode)](xmlelement/addnamespace(_:).md)
  Adds a namespace node to the receiver.
- [var namespaces: [XMLNode]?](xmlelement/namespaces.md)
  Sets all of the namespace nodes of the receiver at once, replacing any existing namespace nodes.
- [func namespace(forPrefix: String) -> XMLNode?](xmlelement/namespace(forprefix:).md)
  Returns the namespace node with a specified prefix.
- [func removeNamespace(forPrefix: String)](xmlelement/removenamespace(forprefix:).md)
  Removes a namespace node that is identified by a given prefix.
- [func resolveNamespace(forName: String) -> XMLNode?](xmlelement/resolvenamespace(forname:).md)
  Returns the namespace node with the prefix matching the given qualified name.
- [func resolvePrefix(forNamespaceURI: String) -> String?](xmlelement/resolveprefix(fornamespaceuri:).md)
  Returns the prefix associated with the specified URI.

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
- [class XMLDTDNode](xmldtdnode.md)
  A representation of element, attribute-list, entity, and notation declarations in a Document Type Definition.
- [class XMLDocument](xmldocument.md)
  An XML document as internalized into a logical tree structure.
- [class XMLNode](xmlnode.md)
  The nodes in the abstract, logical tree structure that represents an XML document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement)*