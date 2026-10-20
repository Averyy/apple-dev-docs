# insertChildren(_:at:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Inserts an array of child nodes at a specified location in the receiver’s list of children.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func insertChildren(_ children: [XMLNode], at index: Int)
```

```objc
- (void) insertChildren:(NSArray<NSXMLNode *> *) children atIndex:(NSUInteger) index;
```

## Parameters

- `children`: An array of [`XMLNode`](../xmlnode.md) objects to insert as children of the receiver.
- `index`: An integer identifying the location in the list of current children to make the insertion. The indices of subsequent children in the list are incremented by the number of inserted children.

## See Also

### Manipulating Child Nodes
- [func addChild(XMLNode)](./addchild%28_%29.md)
  Adds a child node to the end of the list of existing children.
- [func insertChild(XMLNode, at: Int)](./insertchild%28_,at%29.md)
  Inserts a child node in the receiver’s list of children at a specific location in the list.
- [func removeChild(at: Int)](./removechild%28at%29.md)
  Removes the child node at a particular location in the receiver’s list of children.
- [func replaceChild(at: Int, with: XMLNode)](./replacechild%28at,with%29.md)
  Replaces a child at a particular index with another child.
- [func setChildren([XMLNode]?)](./setchildren%28_%29.md)
  Removes all existing children of the receiver and replaces them with an array of new child nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldtd/insertchildren(_:at:))*