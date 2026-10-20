# child(at:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the child node of the receiver at the specified location.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func child(at index: Int) -> XMLNode?
```

```objc
- (NSXMLNode *) childAtIndex:(NSUInteger) index;
```

#### Return Value

An NSXMLNode object or `nil` f the receiver has no children.

#### Discussion

The receiver should be an `NSXMLNode` object representing a document, element, or document type declaration. The returned node object can represent an element, comment, text, or processing instruction.

## Parameters

- `index`: An integer specifying a node position in the receiver’s array of children. If `index` is out of bounds, an exception is raised.

## See Also

### Navigating the Tree of Nodes
- [var rootDocument: XMLDocument?](./rootdocument.md)
  Returns the [`XMLDocument`](../xmldocument.md) object containing the root element and representing the XML document as a whole.
- [var parent: XMLNode?](./parent.md)
  Returns the parent node of the receiver.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/child(at:))*