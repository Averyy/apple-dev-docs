# previous

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the previous `NSXMLNode` object in document order.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
@NSCopying
var previous: XMLNode? { get }
```

```objc
@property (copy, readonly, nullable) NSXMLNode * previousNode;
```

#### Discussion

You use this method to “walk” backward through the tree structure representing an XML document or document section. (Use [`next`](./next.md) to traverse the tree in the opposite direction.) Document order is the natural order that XML constructs appear in markup text. If you send this message to the first node in the tree (that is, the root element), `nil` is returned. `NSXMLNode` bypasses namespace and attribute nodes when it traverses a tree in document order.

## See Also

### Navigating the Tree of Nodes
- [var rootDocument: XMLDocument?](./rootdocument.md)
  Returns the [`XMLDocument`](../xmldocument.md) object containing the root element and representing the XML document as a whole.
- [var parent: XMLNode?](./parent.md)
  Returns the parent node of the receiver.
- [func child(at: Int) -> XMLNode?](./child%28at%29.md)
  Returns the child node of the receiver at the specified location.
- [var childCount: Int](./childcount.md)
  Returns the number of child nodes the receiver has.
- [var children: [XMLNode]?](./children.md)
  Returns an immutable array containing the child nodes of the receiver (as `NSXMLNode` objects).
- [var next: XMLNode?](./next.md)
  Returns the next `NSXMLNode` object in document order.
- [var nextSibling: XMLNode?](./nextsibling.md)
  Returns the next `NSXMLNode` object that is a sibling node to the receiver.
- [var previousSibling: XMLNode?](./previoussibling.md)
  Returns the previous `NSXMLNode` object that is a sibling node to the receiver.
- [func detach()](./detach%28%29.md)
  Detaches the receiver from its parent node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/previous)*