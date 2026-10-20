# replaceChild(at:with:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Replaces the child node of the receiver located at a specified position in its array of children with another node.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func replaceChild(at index: Int, with node: XMLNode)
```

```objc
- (void) replaceChildAtIndex:(NSUInteger) index withNode:(NSXMLNode *) node;
```

#### Discussion

The removed `NSXMLNode` object is autoreleased.

## Parameters

- `index`: An integer identifying a position in the receiver’s array of children. If `index` is less than zero or greater than the number of children minus one, an out-of-bounds exception is raised.
- `node`: An [`XMLNode`](../xmlnode.md) object to replace the one at `index`; it must represent a comment, a processing instruction, or the root element.

## See Also

### Adding and Removing Child Nodes
- [func addChild(XMLNode)](./addchild%28_%29.md)
  Adds a child node after the last of the receiver’s existing children.
- [func insertChild(XMLNode, at: Int)](./insertchild%28_,at%29.md)
  Inserts a node object at specified position in the receiver’s array of children.
- [func insertChildren([XMLNode], at: Int)](./insertchildren%28_,at%29.md)
  Inserts an array of children at a specified position in the receiver’s array of children.
- [func removeChild(at: Int)](./removechild%28at%29.md)
  Removes the child node of the receiver located at a specified position in its array of children.
- [func setChildren([XMLNode]?)](./setchildren%28_%29.md)
  Sets the child nodes of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/replacechild(at:with:))*