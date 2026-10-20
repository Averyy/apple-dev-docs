# replaceChild(at:with:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Replaces a child at a particular index with another child.

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

The replaced child node is released.

## Parameters

- `index`: An integer identifying the position of a node in the receiver’s list of child nodes.
- `node`: An [`XMLNode`](../xmlnode.md) object to replace the object at `index`.

## See Also

### Manipulating Child Nodes
- [func addChild(XMLNode)](./addchild%28_%29.md)
  Adds a child node to the end of the list of existing children.
- [func insertChild(XMLNode, at: Int)](./insertchild%28_,at%29.md)
  Inserts a child node in the receiver’s list of children at a specific location in the list.
- [func insertChildren([XMLNode], at: Int)](./insertchildren%28_,at%29.md)
  Inserts an array of child nodes at a specified location in the receiver’s list of children.
- [func removeChild(at: Int)](./removechild%28at%29.md)
  Removes the child node at a particular location in the receiver’s list of children.
- [func setChildren([XMLNode]?)](./setchildren%28_%29.md)
  Removes all existing children of the receiver and replaces them with an array of new child nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldtd/replacechild(at:with:))*