# element(withName:stringValue:)

**Framework**: Foundation  
**Kind**: method

Returns an [`XMLElement`](xmlelement.md) object with a single text-node child containing the specified text.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class func element(withName name: String, stringValue string: String) -> Any
```

#### Return Value

An `NSXMLElement` object with a single text-node child—an `NSXMLNode` object of kind [`XMLNode.Kind.text`](xmlnode/kind-swift.enum/text.md)—containing the text specified in `string`. Returns `nil` if the object couldn’t be created.

#### Discussion

The equivalent XML markup is `<``name``>``string``</``name``>`.

## Parameters

- `name`: A string that is the name (tag identifier) of the element.
- `string`: A string that is the content of the receiver’s text node.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/element(withname:stringvalue:))*