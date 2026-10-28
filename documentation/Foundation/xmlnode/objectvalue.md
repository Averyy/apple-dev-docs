# objectValue

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the object value of the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var objectValue: Any? { get set }
```

```objc
@property (retain, nullable) id objectValue;
```

## Return Value

The object value of the receiver, which may be the same as the value returned by [`stringValue`](./stringvalue.md). For nodes without content (for example, document nodes), this method returns the string value, or an empty string if there is no string value.

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
- [var stringValue: String?](./stringvalue.md)
  Returns the content of the receiver as a string value.
- [func setStringValue(String, resolvingEntities: Bool)](./setstringvalue%28_,resolvingentities%29.md)
  Sets the content of the receiver as a string value and, optionally, resolves character references, predefined entities, and user-defined entities as declared in the associated DTD.
- [setURI:](../nsxmlnode-seturi.md)
  Sets the URI of the receiver.
- [var uri: String?](./uri.md)
  Returns the URI associated with the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/objectvalue)*