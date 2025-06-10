# parent

**Framework**: Foundation  
**Kind**: property

Returns the parent node of the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
@NSCopying
var parent: XMLNode? { get }
```

#### Discussion

Document nodes and standalone nodes (that is, the root of a detached branch of a tree) have no parent, and sending this message to them returns `nil`. A one-to-one relationship does not always exists between a parent and its children; although a namespace or attribute node cannot be a child, it still has a parent element.

## See Also

- [var rootDocument: XMLDocument?](xmlnode/rootdocument.md)
  Returns the [`XMLDocument`](xmldocument.md) object containing the root element and representing the XML document as a whole.
- [func child(at: Int) -> XMLNode?](xmlnode/child(at:).md)
  Returns the child node of the receiver at the specified location.
- [var childCount: Int](xmlnode/childcount.md)
  Returns the number of child nodes the receiver has.
- [var children: [XMLNode]?](xmlnode/children.md)
  Returns an immutable array containing the child nodes of the receiver (as `NSXMLNode` objects).
- [var next: XMLNode?](xmlnode/next.md)
  Returns the next `NSXMLNode` object in document order.
- [var nextSibling: XMLNode?](xmlnode/nextsibling.md)
  Returns the next `NSXMLNode` object that is a sibling node to the receiver.
- [var previous: XMLNode?](xmlnode/previous.md)
  Returns the previous `NSXMLNode` object in document order.
- [var previousSibling: XMLNode?](xmlnode/previoussibling.md)
  Returns the previous `NSXMLNode` object that is a sibling node to the receiver.
- [func detach()](xmlnode/detach.md)
  Detaches the receiver from its parent node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/parent)*