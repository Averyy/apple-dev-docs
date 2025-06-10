# next

**Framework**: Foundation  
**Kind**: property

Returns the next `NSXMLNode` object in document order.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
@NSCopying
var next: XMLNode? { get }
```

#### Discussion

You use this method to “walk” forward through the tree structure representing an XML document or document section. (Use [`previous`](xmlnode/previous.md) to traverse the tree in the opposite direction.) Document order is the natural order that XML constructs appear in markup text. If you send this message to the last node in the tree, `nil` is returned. `NSXMLNode` bypasses namespace and attribute nodes when it traverses a tree in document order.

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
- [var nextSibling: XMLNode?](xmlnode/nextsibling.md)
  Returns the next `NSXMLNode` object that is a sibling node to the receiver.
- [var previous: XMLNode?](xmlnode/previous.md)
  Returns the previous `NSXMLNode` object in document order.
- [var previousSibling: XMLNode?](xmlnode/previoussibling.md)
  Returns the previous `NSXMLNode` object that is a sibling node to the receiver.
- [func detach()](xmlnode/detach.md)
  Detaches the receiver from its parent node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/next)*