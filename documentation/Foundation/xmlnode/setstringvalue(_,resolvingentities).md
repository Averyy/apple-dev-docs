# setStringValue(_:resolvingEntities:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets the content of the receiver as a string value and, optionally, resolves character references, predefined entities, and user-defined entities as declared in the associated DTD.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func setStringValue(_ string: String, resolvingEntities resolve: Bool)
```

```objc
- (void) setStringValue:(NSString *) string resolvingEntities:(BOOL) resolve;
```

## Discussion

User-defined entities not declared in the DTD remain in their unresolved form. This method can only be invoked on `NSXMLNode` objects that may have content, specifically elements, attributes, namespaces, processing instructions, text, and DTD-declaration nodes. Setting the string value of a node object removes all existing children, including processing instructions and comments. Setting the string value of an element -node object creates a text node as the sole child.

## Parameters

- `string`: A string to assign as the value of the receiver.
- `resolve`: [`true`](../../Swift/true.md) to resolve character references, predefined entities, and user-defined entities as declared in the associated DTD; [`false`](../../Swift/false.md) otherwise. Namespace and processing-instruction nodes have their entities resolved even if `resolve` is [`false`](../../Swift/false.md).

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
- [setURI:](../nsxmlnode-seturi.md)
  Sets the URI of the receiver.
- [var uri: String?](./uri.md)
  Returns the URI associated with the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/setstringvalue(_:resolvingentities:))*