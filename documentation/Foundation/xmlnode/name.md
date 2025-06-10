# name

**Framework**: Foundation  
**Kind**: property

Returns the name of the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var name: String? { get set }
```

#### Return Value

Returns a string specifying the name of the receiver. May return `nil` if the receiver is not a valid kind of node (see discussion).

#### Discussion

This method is applicable only to `NSXMLNode` objects representing elements, attributes, namespaces, processing instructions, and DTD-declaration nodes. If the receiver is not an object of one of these kinds, this method returns `nil`. For example, in the following construction:

```objc
<title>Chapter One</title>
```

The returned name for the element is “title”. If the name is associated with a namespace, the qualified name is returned. For example, if you create an element with local name “foo” and URI “http://bar.com” and the namespace “xmlns:baz=‘http://bar.com’” is applied to this node, when you invoke this method on the node you get “baz:foo”.

## See Also

- [var index: Int](xmlnode/index.md)
  Returns the index of the receiver identifying its position relative to its sibling nodes.
- [var kind: XMLNode.Kind](xmlnode/kind-swift.property.md)
  Returns the kind of node the receiver is as a constant of type [`XMLNode.Kind`](xmlnode/kind-swift.enum.md).
- [var level: Int](xmlnode/level.md)
  Returns the nesting level of the receiver within the tree hierarchy.
- [var objectValue: Any?](xmlnode/objectvalue.md)
  Returns the object value of the receiver.
- [var stringValue: String?](xmlnode/stringvalue.md)
  Returns the content of the receiver as a string value.
- [func setStringValue(String, resolvingEntities: Bool)](xmlnode/setstringvalue(_:resolvingentities:).md)
  Sets the content of the receiver as a string value and, optionally, resolves character references, predefined entities, and user-defined entities as declared in the associated DTD.
- [var uri: String?](xmlnode/uri.md)
  Returns the URI associated with the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/name)*