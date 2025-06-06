# XMLNode

**Framework**: Foundation  
**Kind**: class

The nodes in the abstract, logical tree structure that represents an XML document.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class XMLNode
```

#### Overview

Node objects can be of different kinds, corresponding to the following markup constructs in an XML document: element, attribute, text, processing instruction, namespace, and comment. In addition, a document-node object (specifically, an instance of [`XMLDocument`](xmldocument.md)) represents an XML document in its entirety. [`XMLNode`](xmlnode.md) objects can also represent document type declarations as well as declarations in Document Type Definitions (DTDs). Class factory methods of [`XMLNode`](xmlnode.md) enable you to create nodes of each kind. Only document, element, and DTD nodes may have child nodes.

Among the XML family of classes (excluding [`XMLParser`](xmlparser.md)) the [`XMLNode`](xmlnode.md) class is the base class. Inheriting from it are the classes [`XMLElement`](xmlelement.md), [`XMLDocument`](xmldocument.md), [`XMLDTD`](xmldtd.md), and [`XMLDTDNode`](xmldtdnode.md). [`XMLNode`](xmlnode.md) specifies the interface common to all XML node objects and defines common node behavior and attributes, for example hierarchy level, node name and value, tree traversal, and the ability to emit representative XML markup text.

##### Subclassing Notes

You can subclass [`XMLNode`](xmlnode.md) if you want nodes of kinds different from the supported ones, You can also create a subclass with more specialized attributes or behavior than [`XMLNode`](xmlnode.md).

###### Methods to Override

To subclass [`XMLNode`](xmlnode.md) you need to override the primary initializer, [`init(kind:options:)`](xmlnode/init(kind:options:).md), and the methods listed below. In most cases, you need only invoke the superclass implementation, adding any subclass-specific code before or after the invocation, as necessary.

| [`kind`](xmlnode/kind-swift.property.md) | [`parent`](xmlnode/parent.md) |
| --- | --- |
| [`name`](xmlnode/name.md) | [`child(at:)`](xmlnode/child(at:).md) |
| [`name`](xmlnode/name.md) | [`childCount`](xmlnode/childcount.md) |
| [`objectValue`](xmlnode/objectvalue.md) | [`children`](xmlnode/children.md) |
| [`objectValue`](xmlnode/objectvalue.md) | [`detach()`](xmlnode/detach().md) |
| [`stringValue`](xmlnode/stringvalue.md) | [`localName`](xmlnode/localname.md) |
| [`setStringValue(_:resolvingEntities:)`](xmlnode/setstringvalue(_:resolvingentities:).md) | [`prefix`](xmlnode/prefix.md) |
| [`index`](xmlnode/index.md) | [`uri`](xmlnode/uri.md) |

By default [`XMLNode`](xmlnode.md) implements the `NSObject` [`isEqual(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/isEqual(_:)) method to perform a deep comparison: two [`XMLNode`](xmlnode.md) objects are not considered equal unless they have the same name, same child nodes, same attributes, and so on. The comparison looks at the node and its children, but does not include the node’s parent. If you want a different standard of comparison, override `isEqual:`.

###### Special Considerations

Because of the architecture and data model of NSXML, when it parses and processes a source of XML it cannot know about your subclass unless you override the [`XMLDocument`](xmldocument.md) class method [`replacementClass(for:)`](xmldocument/replacementclass(for:).md) to return your custom class in place of an NSXML class. If your custom class has no direct NSXML counterpart—for example, it is a subclass of [`XMLNode`](xmlnode.md) that represents CDATA sections—then you can walk the tree after it has been created and insert the new node where appropriate.

## Topics

### Creating and Initializing Node Objects
- [convenience init(kind: XMLNode.Kind)](xmlnode/init(kind:).md)
  Returns an `NSXMLNode` instance initialized with the constant indicating node kind.
- [init(kind: XMLNode.Kind, options: XMLNode.Options)](xmlnode/init(kind:options:).md)
  Returns an `NSXMLNode` instance initialized with the constant indicating node kind and one or more initialization options.
- [class func document() -> Any](xmlnode/document.md)
  Returns an empty document node.
- [class func document(withRootElement: XMLElement) -> Any](xmlnode/document(withrootelement:).md)
  Returns an [`XMLDocument`](xmldocument.md) object initialized with a given root element.
- [class func element(withName: String) -> Any](xmlnode/element(withname:).md)
  Returns an [`XMLElement`](xmlelement.md) object with a given tag identifier, or name
- [class func element(withName: String, children: [XMLNode]?, attributes: [XMLNode]?) -> Any](xmlnode/element(withname:children:attributes:).md)
  Returns an [`XMLElement`](xmlelement.md) object with the given tag (name), attributes, and children.
- [class func element(withName: String, stringValue: String) -> Any](xmlnode/element(withname:stringvalue:).md)
  Returns an [`XMLElement`](xmlelement.md) object with a single text-node child containing the specified text.
- [class func element(withName: String, uri: String) -> Any](xmlnode/element(withname:uri:).md)
  Returns an element whose fully qualified name is specified.
- [class func attribute(withName: String, stringValue: String) -> Any](xmlnode/attribute(withname:stringvalue:).md)
  Returns an `NSXMLNode` object representing an attribute node with a given name and string.
- [class func attribute(withName: String, uri: String, stringValue: String) -> Any](xmlnode/attribute(withname:uri:stringvalue:).md)
  Returns an `NSXMLNode` object representing an attribute node with a given qualified name and string.
- [class func text(withStringValue: String) -> Any](xmlnode/text(withstringvalue:).md)
  Returns an `NSXMLNode` object representing a text node with specified content.
- [class func comment(withStringValue: String) -> Any](xmlnode/comment(withstringvalue:).md)
  Returns an [`XMLNode`](xmlnode.md) object representing a comment node containing given text.
- [class func namespace(withName: String, stringValue: String) -> Any](xmlnode/namespace(withname:stringvalue:).md)
  Returns an `NSXMLNode` object representing a namespace with a specified name and URI.
- [class func dtdNode(withXMLString: String) -> Any?](xmlnode/dtdnode(withxmlstring:).md)
  Returns a [`XMLDTDNode`](xmldtdnode.md) object representing the DTD declaration for an element, attribute, entity, or notation based on a given string.
- [class func predefinedNamespace(forPrefix: String) -> XMLNode?](xmlnode/predefinednamespace(forprefix:).md)
  Returns an `NSXMLNode` object representing one of the predefined namespaces with the specified prefix.
- [class func processingInstruction(withName: String, stringValue: String) -> Any](xmlnode/processinginstruction(withname:stringvalue:).md)
  Returns an `NSXMLNode` object representing a processing instruction with a specified name and value.
### Managing XML Node Objects
- [var index: Int](xmlnode/index.md)
  Returns the index of the receiver identifying its position relative to its sibling nodes.
- [var kind: XMLNode.Kind](xmlnode/kind-swift.property.md)
  Returns the kind of node the receiver is as a constant of type [`XMLNode.Kind`](xmlnode/kind-swift.enum.md).
- [var level: Int](xmlnode/level.md)
  Returns the nesting level of the receiver within the tree hierarchy.
- [var name: String?](xmlnode/name.md)
  Returns the name of the receiver.
- [var objectValue: Any?](xmlnode/objectvalue.md)
  Returns the object value of the receiver.
- [var stringValue: String?](xmlnode/stringvalue.md)
  Returns the content of the receiver as a string value.
- [func setStringValue(String, resolvingEntities: Bool)](xmlnode/setstringvalue(_:resolvingentities:).md)
  Sets the content of the receiver as a string value and, optionally, resolves character references, predefined entities, and user-defined entities as declared in the associated DTD.
- [var uri: String?](xmlnode/uri.md)
  Returns the URI associated with the receiver.
### Navigating the Tree of Nodes
- [var rootDocument: XMLDocument?](xmlnode/rootdocument.md)
  Returns the [`XMLDocument`](xmldocument.md) object containing the root element and representing the XML document as a whole.
- [var parent: XMLNode?](xmlnode/parent.md)
  Returns the parent node of the receiver.
- [func child(at: Int) -> XMLNode?](xmlnode/child(at:).md)
  Returns the child node of the receiver at the specified location.
- [var childCount: Int](xmlnode/childcount.md)
  Returns the number of child nodes the receiver has.
- [var children: [XMLNode]?](xmlnode/children.md)
  Returns an immutable array containing the child nodes of the receiver (as `NSXMLNode` objects).
- [var next: XMLNode?](xmlnode/next.md)
  Returns the next `NSXMLNode` object in document order.
- [var nextSibling: XMLNode?](xmlnode/nextsibling.md)
  Returns the next `NSXMLNode` object that is a sibling node to the receiver.
- [var previous: XMLNode?](xmlnode/previous.md)
  Returns the previous `NSXMLNode` object in document order.
- [var previousSibling: XMLNode?](xmlnode/previoussibling.md)
  Returns the previous `NSXMLNode` object that is a sibling node to the receiver.
- [func detach()](xmlnode/detach.md)
  Detaches the receiver from its parent node.
### Emitting Node Content
- [var xmlString: String](xmlnode/xmlstring.md)
  Returns the string representation of the receiver as it would appear in an XML document.
- [func xmlString(options: XMLNode.Options) -> String](xmlnode/xmlstring(options:).md)
  Returns the string representation of the receiver as it would appear in an XML document, with one or more output options specified.
- [func canonicalXMLStringPreservingComments(Bool) -> String](xmlnode/canonicalxmlstringpreservingcomments(_:).md)
  Returns a string object encapsulating the receiver’s XML in canonical form.
- [var description: String](xmlnode/description.md)
### Executing Queries
- [func nodes(forXPath: String) throws -> [XMLNode]](xmlnode/nodes(forxpath:).md)
  Returns the nodes resulting from executing an XPath query upon the receiver.
- [func objects(forXQuery: String) throws -> [Any]](xmlnode/objects(forxquery:).md)
  Returns the objects resulting from executing an XQuery query upon the receiver.
- [func objects(forXQuery: String, constants: [String : Any]?) throws -> [Any]](xmlnode/objects(forxquery:constants:).md)
  Returns the objects resulting from executing an XQuery query upon the receiver.
- [var xPath: String?](xmlnode/xpath.md)
  Returns the XPath expression identifying the receiver’s location in the document tree.
### Managing Namespaces
- [var localName: String?](xmlnode/localname.md)
  Returns the local name of the receiver.
- [class func localName(forName: String) -> String](xmlnode/localname(forname:).md)
  Returns the local name from the specified qualified name.
- [var prefix: String?](xmlnode/prefix.md)
  Returns the prefix of the receiver’s name.
- [class func prefix(forName: String) -> String?](xmlnode/prefix(forname:).md)
  Returns the prefix from the specified qualified name.
### Constants
- [XMLNode.Kind](xmlnode/kind-swift.enum.md)
  `NSXMLNode` declares the following constants of type NSXMLNodeKind for specifying a node’s kind in the initializer methods [`init(kind:)`](xmlnode/init(kind:).md) and [`init(kind:options:)`](xmlnode/init(kind:options:).md):
- [XMLNode.Options](xmlnode/options.md)
  These constants are input and output options for all `NSXMLNode` objects (unless otherwise indicated), including [`XMLDocument`](xmldocument.md) objects. You can specify these options in the `NSXMLNode` methods [`init(kind:options:)`](xmlnode/init(kind:options:).md) and [`xmlString(options:)`](xmlnode/xmlstring(options:).md).
### Initializers
- [init()](xmlnode/init.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [XMLDTD](xmldtd.md)
- [XMLDTDNode](xmldtdnode.md)
- [XMLDocument](xmldocument.md)
- [XMLElement](xmlelement.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class XMLDTD](xmldtd.md)
  A representation of a Document Type Definition.
- [class XMLDTDNode](xmldtdnode.md)
  A representation of element, attribute-list, entity, and notation declarations in a Document Type Definition.
- [class XMLDocument](xmldocument.md)
  An XML document as internalized into a logical tree structure.
- [class XMLElement](xmlelement.md)
  The element nodes in an XML tree structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode)*