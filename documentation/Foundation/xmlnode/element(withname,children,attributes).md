# element(withName:children:attributes:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns an [`XMLElement`](../xmlelement.md) object with the given tag (name), attributes, and children.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class func element(withName name: String, children: [XMLNode]?, attributes: [XMLNode]?) -> Any
```

```objc
+ (id) elementWithName:(NSString *) name children:(NSArray<NSXMLNode *> *) children attributes:(NSArray<NSXMLNode *> *) attributes;
```

#### Return Value

An `NSXMLElement` object or `nil` if the object couldn’t be created.

## Parameters

- `name`: A string that is the name (tag identifier) of the element.
- `children`: An array of `NSXMLElement` objects or `NSXMLNode` objects of kinds [`XMLNode.Kind.element`](./kind-swift.enum/element.md), [`XMLNode.Kind.processingInstruction`](./kind-swift.enum/processinginstruction.md), [`XMLNode.Kind.comment`](./kind-swift.enum/comment.md), and [`XMLNode.Kind.text`](./kind-swift.enum/text.md). Specify `nil` if there are no children to add to this node object.
- `attributes`: An array of `NSXMLNode` objects of kind [`XMLNode.Kind.attribute`](./kind-swift.enum/attribute.md). Specify `nil` if there are no attributes to add to this node object.

## See Also

### Creating and Initializing Node Objects
- [convenience init(kind: XMLNode.Kind)](./init%28kind%29.md)
  Returns an `NSXMLNode` instance initialized with the constant indicating node kind.
- [init(kind: XMLNode.Kind, options: XMLNode.Options)](./init%28kind,options%29.md)
  Returns an `NSXMLNode` instance initialized with the constant indicating node kind and one or more initialization options.
- [class func document() -> Any](./document%28%29.md)
  Returns an empty document node.
- [class func document(withRootElement: XMLElement) -> Any](./document%28withrootelement%29.md)
  Returns an [`XMLDocument`](../xmldocument.md) object initialized with a given root element.
- [class func element(withName: String) -> Any](./element%28withname%29.md)
  Returns an [`XMLElement`](../xmlelement.md) object with a given tag identifier, or name
- [class func element(withName: String, stringValue: String) -> Any](./element%28withname,stringvalue%29.md)
  Returns an [`XMLElement`](../xmlelement.md) object with a single text-node child containing the specified text.
- [class func element(withName: String, uri: String) -> Any](./element%28withname,uri%29.md)
  Returns an element whose fully qualified name is specified.
- [class func attribute(withName: String, stringValue: String) -> Any](./attribute%28withname,stringvalue%29.md)
  Returns an `NSXMLNode` object representing an attribute node with a given name and string.
- [class func attribute(withName: String, uri: String, stringValue: String) -> Any](./attribute%28withname,uri,stringvalue%29.md)
  Returns an `NSXMLNode` object representing an attribute node with a given qualified name and string.
- [class func text(withStringValue: String) -> Any](./text%28withstringvalue%29.md)
  Returns an `NSXMLNode` object representing a text node with specified content.
- [class func comment(withStringValue: String) -> Any](./comment%28withstringvalue%29.md)
  Returns an [`XMLNode`](../xmlnode.md) object representing a comment node containing given text.
- [class func namespace(withName: String, stringValue: String) -> Any](./namespace%28withname,stringvalue%29.md)
  Returns an `NSXMLNode` object representing a namespace with a specified name and URI.
- [class func dtdNode(withXMLString: String) -> Any?](./dtdnode%28withxmlstring%29.md)
  Returns a [`XMLDTDNode`](../xmldtdnode.md) object representing the DTD declaration for an element, attribute, entity, or notation based on a given string.
- [class func predefinedNamespace(forPrefix: String) -> XMLNode?](./predefinednamespace%28forprefix%29.md)
  Returns an `NSXMLNode` object representing one of the predefined namespaces with the specified prefix.
- [class func processingInstruction(withName: String, stringValue: String) -> Any](./processinginstruction%28withname,stringvalue%29.md)
  Returns an `NSXMLNode` object representing a processing instruction with a specified name and value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/element(withname:children:attributes:))*