# previousSibling

**Framework**: Foundation  
**Kind**: property

Returns the previous `NSXMLNode` object that is a sibling node to the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
@NSCopying
var previousSibling: XMLNode? { get }
```

#### Discussion

This object will have an [`index`](xmlnode/index.md) value that is one less than the receiver’s. If there are no more previous siblings (that is, other child nodes of the receiver’s parent) the method returns `nil`

## See Also

- [var rootDocument: XMLDocument?](xmlnode/rootdocument.md)
  Returns the [`XMLDocument`](xmldocument.md) object containing the root element and representing the XML document as a whole.
- [var parent: XMLNode?](xmlnode/parent.md)
  Returns the parent node of the receiver.
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
- [func detach()](xmlnode/detach.md)
  Detaches the receiver from its parent node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/previoussibling)*