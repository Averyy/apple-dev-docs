# setChildren(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Removes all existing children of the receiver and replaces them with an array of new child nodes.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func setChildren(_ children: [XMLNode]?)
```

```objc
- (void) setChildren:(NSArray<NSXMLNode *> *) children;
```

## Discussion

Replaced or removed child nodes are released.

## Parameters

- `children`: An array of [`XMLNode`](../xmlnode.md) objects. To remove all existing children, pass in `nil`.

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
- [func replaceChild(at: Int, with: XMLNode)](./replacechild%28at,with%29.md)
  Replaces a child at a particular index with another child.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldtd/setchildren(_:))*