# insertChild(_:at:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Inserts a node object at specified position in the receiver’s array of children.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func insertChild(_ child: XMLNode, at index: Int)
```

```objc
- (void) insertChild:(NSXMLNode *) child atIndex:(NSUInteger) index;
```

## Parameters

- `child`: The [`XMLNode`](../xmlnode.md) object to be inserted. The added node must be an `NSXMLNode` object representing a comment, processing instruction, or the root element.
- `index`: An integer specifying the index of the children array to insert `child`. The indexes of children after the new child are incremented. If `index` is less than zero or greater than the number of children, an out-of-bounds exception is raised.

## See Also

### Adding and Removing Child Nodes
- [func addChild(XMLNode)](./addchild%28_%29.md)
  Adds a child node after the last of the receiver’s existing children.
- [func insertChildren([XMLNode], at: Int)](./insertchildren%28_,at%29.md)
  Inserts an array of children at a specified position in the receiver’s array of children.
- [func removeChild(at: Int)](./removechild%28at%29.md)
  Removes the child node of the receiver located at a specified position in its array of children.
- [func replaceChild(at: Int, with: XMLNode)](./replacechild%28at,with%29.md)
  Replaces the child node of the receiver located at a specified position in its array of children with another node.
- [func setChildren([XMLNode]?)](./setchildren%28_%29.md)
  Sets the child nodes of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/insertchild(_:at:))*