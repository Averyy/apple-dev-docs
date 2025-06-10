# kind

**Framework**: Foundation  
**Kind**: property

Returns the kind of node the receiver is as a constant of type [`XMLNode.Kind`](xmlnode/kind-swift.enum.md).

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var kind: XMLNode.Kind { get }
```

#### Discussion

`NSXMLNode` objects can represent documents, elements, attributes, namespaces, text, processing instructions, comments, document type declarations, and specific declarations within DTDs. See Constants for a list of valid NSXMLNodeKind constants

## See Also

- [convenience init(kind: XMLNode.Kind)](xmlnode/init(kind:).md)
  Returns an `NSXMLNode` instance initialized with the constant indicating node kind.
- [var index: Int](xmlnode/index.md)
  Returns the index of the receiver identifying its position relative to its sibling nodes.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/kind-swift.property)*