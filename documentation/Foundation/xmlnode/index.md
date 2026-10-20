# index

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the index of the receiver identifying its position relative to its sibling nodes.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var index: Int { get }
```

```objc
@property (readonly) NSUInteger index;
```

#### Return Value

An integer that is the index of the receiver relative to its sibling nodes.

#### Discussion

The first child node of a parent has an index of zero.

## See Also

### Related Documentation
- [func child(at: Int) -> XMLNode?](./child%28at%29.md)
  Returns the child node of the receiver at the specified location.
### Managing XML Node Objects
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
- [var uri: String?](./uri.md)
  Returns the URI associated with the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/index)*