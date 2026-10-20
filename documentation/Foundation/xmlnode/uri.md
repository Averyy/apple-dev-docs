# uri

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the URI associated with the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var uri: String? { get set }
```

```objc
@property (copy, nullable) NSString * URI;
```

#### Discussion

A node’s URI is derived from its namespace or a document’s URI; for documents, the URI comes either from the parsed XML or is explicitly set. You cannot change the URI for a particular node other for than a namespace or document node.

## See Also

### Managing XML Node Objects
- [var index: Int](./index.md)
  Returns the index of the receiver identifying its position relative to its sibling nodes.
- [var kind: XMLNode.Kind](./kind-swift.property.md)
  Returns the kind of node the receiver is as a constant of type [`XMLNode.Kind`](./kind-swift.enum.md).
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/uri)*