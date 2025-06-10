# uri

**Framework**: Foundation  
**Kind**: property

Returns the URI associated with the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var uri: String? { get set }
```

#### Discussion

A node’s URI is derived from its namespace or a document’s URI; for documents, the URI comes either from the parsed XML or is explicitly set. You cannot change the URI for a particular node other for than a namespace or document node.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/uri)*