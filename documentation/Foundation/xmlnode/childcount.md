# childCount

**Framework**: Foundation  
**Kind**: property

Returns the number of child nodes the receiver has.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var childCount: Int { get }
```

#### Discussion

This receiver should be an `NSXMLNode` object representing a document, element, or document type declaration. For performance reasons, use this method instead of getting the count from the array returned by [`children`](xmlnode/children.md) (for example, `[[thisNode children] count`]).

## See Also

- [var rootDocument: XMLDocument?](xmlnode/rootdocument.md)
  Returns the [`XMLDocument`](xmldocument.md) object containing the root element and representing the XML document as a whole.
- [var parent: XMLNode?](xmlnode/parent.md)
  Returns the parent node of the receiver.
- [func child(at: Int) -> XMLNode?](xmlnode/child(at:).md)
  Returns the child node of the receiver at the specified location.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/childcount)*