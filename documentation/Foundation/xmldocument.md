# XMLDocument

**Framework**: Foundation  
**Kind**: class

An XML document as internalized into a logical tree structure.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class XMLDocument
```

## Mentions

- [setURI:](1806643-seturi.md)

#### Overview

An [`XMLDocument`](xmldocument.md) object can have multiple child nodes but only one element, the root element. Any other node must be a [`XMLNode`](xmlnode.md) object representing a comment or a processing instruction. If you attempt to add any other kind of child node to an [`XMLDocument`](xmldocument.md) object, such as an attribute, namespace, another document object, or an element other than the root, [`XMLDocument`](xmldocument.md) raises an exception. If you add a valid child node and that object already has a parent, [`XMLDocument`](xmldocument.md) raises an exception. An [`XMLDocument`](xmldocument.md) object may also have document-global attributes, such as XML version, character encoding, referenced DTD, and MIME type.

The initializers of the [`XMLDocument`](xmldocument.md) class read an external source of XML, whether it be a local file or remote website, parse it, and process it into the tree representation. You can also construct an [`XMLDocument`](xmldocument.md) programmatically. There are accessor methods for getting and setting document attributes, methods for transforming documents using XSLT, a method for dynamically validating a document, and methods for printing out the content of an [`XMLDocument`](xmldocument.md) as XML, XHTML, HTML, or plain text.

The [`XMLDocument`](xmldocument.md) class is thread-safe as long as any given instance is used only in one thread.

##### Subclassing Notes

###### Methods to Override

To subclass `NSXMLDocument` you need to override the primary initializer, [`init(data:options:)`](xmldocument/init(data:options:).md), and the methods listed below. In most cases, you need only invoke the superclass implementation, adding any subclass-specific code before or after the invocation, as necessary.

- [`rootElement()`](xmldocument/rootelement().md)
- [`setChildren(_:)`](xmldocument/setchildren(_:).md)
- [`removeChild(at:)`](xmldocument/removechild(at:).md)
- [`insertChild(_:at:)`](xmldocument/insertchild(_:at:).md)
- [`characterEncoding`](xmldocument/characterencoding.md)
- [`characterEncoding`](xmldocument/characterencoding.md)
- [`documentContentKind`](xmldocument/documentcontentkind.md)
- [`documentContentKind`](xmldocument/documentcontentkind.md)
- [`dtd`](xmldocument/dtd.md)
- [`mimeType`](xmldocument/mimetype.md)
- [`isStandalone`](xmldocument/isstandalone.md)
- [`version`](xmldocument/version.md)
- [`version`](xmldocument/version.md)

By default `NSXMLDocument` implements the `NSObject` [`isEqual(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/isEqual(_:)) method to perform a deep comparison: two `NSXMLDocument` objects are not considered equal unless they have the same name, same child nodes, same attributes, and so on. The comparison does not consider the parent node (and hence the node’s location). If you want a different standard of comparison, override `isEqual:`.

###### Special Considerations

Because of the architecture and data model of NSXML, when it parses and processes a source of XML it cannot know about your subclass unless you override the class method [`replacementClass(for:)`](xmldocument/replacementclass(for:).md) to return your custom class in place of an `NSXML` class. If your custom class has no direct `NSXML` counterpart—for example, it is a subclass of `NSXMLNode` that represents CDATA sections—then you can walk the tree after it has been created and insert the new node where appropriate.

## Topics

### Initializing NSXMLDocument Objects
- [convenience init(contentsOf: URL, options: XMLNode.Options) throws](xmldocument/init(contentsof:options:).md)
  Initializes and returns an NSXMLDocument object created from the XML or HTML contents of a URL-referenced source
- [init(data: Data, options: XMLNode.Options) throws](xmldocument/init(data:options:).md)
  Initializes and returns an `NSXMLDocument` object created from an [`NSData`](nsdata.md) object.
- [init(rootElement: XMLElement?)](xmldocument/init(rootelement:).md)
  Returns an `NSXMLDocument` object initialized with a single child, the root element.
- [convenience init(xmlString: String, options: XMLNode.Options) throws](xmldocument/init(xmlstring:options:).md)
  Initializes and returns an `NSXMLDocument` object created from a string containing XML markup text.
- [class func replacementClass(for: AnyClass) -> AnyClass](xmldocument/replacementclass(for:).md)
  Overridden by subclasses to substitute a custom class for an NSXML class that the parser uses to create node instances.
### Managing Document Attributes
- [var characterEncoding: String?](xmldocument/characterencoding.md)
  Sets the character encoding of the receiver to `encoding`,
- [var documentContentKind: XMLDocument.ContentKind](xmldocument/documentcontentkind.md)
  Sets the kind of output content for the receiver.
- [var dtd: XMLDTD?](xmldocument/dtd.md)
  Returns an [`XMLDTD`](xmldtd.md) object representing the internal DTD associated with the receiver.
- [var isStandalone: Bool](xmldocument/isstandalone.md)
  Sets a Boolean value that specifies whether the receiver represents a standalone XML document.
- [var mimeType: String?](xmldocument/mimetype.md)
  Returns the MIME type for the receiver.
- [var version: String?](xmldocument/version.md)
  Sets the version of the receiver’s XML.
### Managing the Root Element
- [func rootElement() -> XMLElement?](xmldocument/rootelement.md)
  Returns the root element of the receiver.
- [func setRootElement(XMLElement)](xmldocument/setrootelement(_:).md)
  Set the root element of the receiver.
### Adding and Removing Child Nodes
- [func addChild(XMLNode)](xmldocument/addchild(_:).md)
  Adds a child node after the last of the receiver’s existing children.
- [func insertChild(XMLNode, at: Int)](xmldocument/insertchild(_:at:).md)
  Inserts a node object at specified position in the receiver’s array of children.
- [func insertChildren([XMLNode], at: Int)](xmldocument/insertchildren(_:at:).md)
  Inserts an array of children at a specified position in the receiver’s array of children.
- [func removeChild(at: Int)](xmldocument/removechild(at:).md)
  Removes the child node of the receiver located at a specified position in its array of children.
- [func replaceChild(at: Int, with: XMLNode)](xmldocument/replacechild(at:with:).md)
  Replaces the child node of the receiver located at a specified position in its array of children with another node.
- [func setChildren([XMLNode]?)](xmldocument/setchildren(_:).md)
  Sets the child nodes of the receiver.
### Transforming a Document Using XSLT
- [func object(byApplyingXSLT: Data, arguments: [String : String]?) throws -> Any](xmldocument/object(byapplyingxslt:arguments:).md)
  Applies the XSLT pattern rules and templates (specified as a data object) to the receiver and returns a document object containing transformed XML or HTML markup.
- [func object(byApplyingXSLTString: String, arguments: [String : String]?) throws -> Any](xmldocument/object(byapplyingxsltstring:arguments:).md)
  Applies the XSLT pattern rules and templates (specified as a string) to the receiver and returns a document object containing transformed XML or HTML markup.
- [func objectByApplyingXSLT(at: URL, arguments: [String : String]?) throws -> Any](xmldocument/objectbyapplyingxslt(at:arguments:).md)
  Applies the XSLT pattern rules and templates located at a specified URL to the receiver and returns a document object containing transformed XML markup or an [`NSData`](nsdata.md) object containing plain text, RTF text, and so on.
### Writing a Document as XML Data
- [var xmlData: Data](xmldocument/xmldata.md)
  Returns the XML string representation of the receiver—that is, the entire document—encapsulated in a data object.
- [func xmlData(options: XMLNode.Options) -> Data](xmldocument/xmldata(options:).md)
  Returns the XML string representation of the receiver—that is, the entire document—encapsulated in a data object.
### Validating a Document
- [func validate() throws](xmldocument/validate.md)
  Validates the document against the governing schema and returns whether the document conforms to the schema.
### Constants
- [Input and Output Options](input_and_output_options.md)
  Input and output options specifically intended for `NSXMLDocument` objects.
- [XMLDocument.ContentKind](xmldocument/contentkind.md)
  Type used to define the kind of document content.
- [Document Content Types](document-content-types.md)
  Define document types.
### Initializers
- [init()](xmldocument/init.md)

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

## See Also

- [class XMLDTD](xmldtd.md)
  A representation of a Document Type Definition.
- [class XMLDTDNode](xmldtdnode.md)
  A representation of element, attribute-list, entity, and notation declarations in a Document Type Definition.
- [class XMLElement](xmlelement.md)
  The element nodes in an XML tree structure.
- [class XMLNode](xmlnode.md)
  The nodes in the abstract, logical tree structure that represents an XML document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument)*