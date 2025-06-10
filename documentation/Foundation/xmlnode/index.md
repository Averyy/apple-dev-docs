# index

**Framework**: Foundation  
**Kind**: property

Returns the index of the receiver identifying its position relative to its sibling nodes.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var index: Int { get }
```

#### Return Value

An integer that is the index of the receiver relative to its sibling nodes.

#### Discussion

The first child node of a parent has an index of zero.

## See Also

- [func child(at: Int) -> XMLNode?](xmlnode/child(at:).md)
  Returns the child node of the receiver at the specified location.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/index)*