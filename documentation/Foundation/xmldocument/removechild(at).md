# removeChild(at:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Removes the child node of the receiver located at a specified position in its array of children.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func removeChild(at index: Int)
```

```objc
- (void) removeChildAtIndex:(NSUInteger) index;
```

## Discussion

Subsequent children have their indexes decreased by one. The removed [`XMLNode`](../xmlnode.md) object is autoreleased.

## Parameters

- `index`: An integer identifying the position of an child in the receiver’s array. If `index` is less than zero or greater than the number of children minus one, an out-of-bounds exception is raised.

## See Also

### Adding and Removing Child Nodes
- [func addChild(XMLNode)](./addchild%28_%29.md)
  Adds a child node after the last of the receiver’s existing children.
- [func insertChild(XMLNode, at: Int)](./insertchild%28_,at%29.md)
  Inserts a node object at specified position in the receiver’s array of children.
- [func insertChildren([XMLNode], at: Int)](./insertchildren%28_,at%29.md)
  Inserts an array of children at a specified position in the receiver’s array of children.
- [func replaceChild(at: Int, with: XMLNode)](./replacechild%28at,with%29.md)
  Replaces the child node of the receiver located at a specified position in its array of children with another node.
- [func setChildren([XMLNode]?)](./setchildren%28_%29.md)
  Sets the child nodes of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/removechild(at:))*