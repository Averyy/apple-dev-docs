# kind

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the kind of node the receiver is as a constant of type [`XMLNode.Kind`](./kind-swift.enum.md).

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var kind: XMLNode.Kind { get }
```

```objc
@property (readonly) NSXMLNodeKind kind;
```

## Discussion

`NSXMLNode` objects can represent documents, elements, attributes, namespaces, text, processing instructions, comments, document type declarations, and specific declarations within DTDs. See Constants for a list of valid NSXMLNodeKind constants

## See Also

### Related Documentation
- [convenience init(kind: XMLNode.Kind)](./init%28kind%29.md)
  Returns an `NSXMLNode` instance initialized with the constant indicating node kind.
### Managing XML Node Objects
- [var index: Int](./index.md)
  Returns the index of the receiver identifying its position relative to its sibling nodes.
- [var level: Int](./level.md)
  Returns the nesting level of the receiver within the tree hierarchy.
- [var name: String?](./name.md)
  Returns the name of the receiver.
- [var objectValue: Any?](./objectvalue.md)
  Returns the object value of the receiver.
- [var stringValue: String?](./stringvalue.md)
  Returns the content of the receiver as a string value.
- [func setStringValue(String, resolvingEntities: Bool)](./setstringvalue%28_,resolvingentities%29.md)
  Sets the content of the receiver as a string value and, optionally, resolves character references, predefined entities, and user-defined entities as declared in the associated DTD.
- [setURI:](../nsxmlnode-seturi.md)
  Sets the URI of the receiver.
- [var uri: String?](./uri.md)
  Returns the URI associated with the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/kind-swift.property)*