# rootDocument

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the [`XMLDocument`](../xmldocument.md) object containing the root element and representing the XML document as a whole.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var rootDocument: XMLDocument? { get }
```

```objc
@property (retain, readonly, nullable) NSXMLDocument * rootDocument;
```

## Discussion

If the receiver is a standalone node (that is, a node at the head of a detached branch of the tree), this method returns `nil`.

## See Also

### Navigating the Tree of Nodes
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
- [var previous: XMLNode?](./previous.md)
  Returns the previous `NSXMLNode` object in document order.
- [var previousSibling: XMLNode?](./previoussibling.md)
  Returns the previous `NSXMLNode` object that is a sibling node to the receiver.
- [func detach()](./detach%28%29.md)
  Detaches the receiver from its parent node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/rootdocument)*