# setStringValue(_:resolvingEntities:)

**Framework**: Foundation  
**Kind**: method

Sets the content of the receiver as a string value and, optionally, resolves character references, predefined entities, and user-defined entities as declared in the associated DTD.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func setStringValue(_ string: String, resolvingEntities resolve: Bool)
```

#### Discussion

User-defined entities not declared in the DTD remain in their unresolved form. This method can only be invoked on `NSXMLNode` objects that may have content, specifically elements, attributes, namespaces, processing instructions, text, and DTD-declaration nodes. Setting the string value of a node object removes all existing children, including processing instructions and comments. Setting the string value of an element -node object creates a text node as the sole child.

## Parameters

- `string`: A string to assign as the value of the receiver.
- `resolve`:   to resolve character references, predefined entities, and user-defined entities as declared in the associated DTD;   otherwise. Namespace and processing-instruction nodes have their entities resolved even if   is  .

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
- [var uri: String?](xmlnode/uri.md)
  Returns the URI associated with the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/setstringvalue(_:resolvingentities:))*