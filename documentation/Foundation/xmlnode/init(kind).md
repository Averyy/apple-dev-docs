# init(kind:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns an `NSXMLNode` instance initialized with the constant indicating node kind.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
convenience init(kind: XMLNode.Kind)
```

```objc
- (instancetype) initWithKind:(NSXMLNodeKind) kind;
```

#### Return Value

An `NSXMLNode` object initialized with kind or `nil` if the object couldn’t be created. If `kind` is not a valid NSXMLNodeKind constant, the method returns an `NSXMLNode` object of kind `NSXMLInvalidKind`.

#### Discussion

This method invokes [`init(kind:options:)`](./init%28kind,options%29.md) with the `options` parameter set to `NSXMLNodeOptionsNone`.

Do not use this initializer for creating instances of [`XMLDTDNode`](../xmldtdnode.md) for attribute-list declarations. Instead, use the [`dtdNode(withXMLString:)`](./dtdnode%28withxmlstring%29.md) class method of this class or the [`init(xmlString:)`](../xmldtdnode/init%28xmlstring%29-1dyhd.md) method of the `NSXMLDTDNode` class.

## Parameters

- `kind`: An `enum` constant of type [`XMLNode.Kind`](./kind-swift.enum.md) that indicates the type of node. See Constants for a list of valid NSXMLNodeKind constants.

## See Also

### Related Documentation
- [Tree-Based XML Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NSXML_Concepts/NSXML.html#//apple_ref/doc/uid/TP40001269)
### Creating and Initializing Node Objects
- [init(kind: XMLNode.Kind, options: XMLNode.Options)](./init%28kind,options%29.md)
  Returns an `NSXMLNode` instance initialized with the constant indicating node kind and one or more initialization options.
- [class func document() -> Any](./document%28%29.md)
  Returns an empty document node.
- [class func document(withRootElement: XMLElement) -> Any](./document%28withrootelement%29.md)
  Returns an [`XMLDocument`](../xmldocument.md) object initialized with a given root element.
- [class func element(withName: String) -> Any](./element%28withname%29.md)
  Returns an [`XMLElement`](../xmlelement.md) object with a given tag identifier, or name
- [class func element(withName: String, children: [XMLNode]?, attributes: [XMLNode]?) -> Any](./element%28withname,children,attributes%29.md)
  Returns an [`XMLElement`](../xmlelement.md) object with the given tag (name), attributes, and children.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/init(kind:))*