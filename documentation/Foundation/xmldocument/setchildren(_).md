# setChildren(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets the child nodes of the receiver.

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

## Parameters

- `children`: An array of [`XMLNode`](../xmlnode.md) objects. Each of these objects must represent comments, processing instructions, or the root element; otherwise, an exception is raised. Pass in `nil` to remove all children.

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
- [func replaceChild(at: Int, with: XMLNode)](./replacechild%28at,with%29.md)
  Replaces the child node of the receiver located at a specified position in its array of children with another node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/setchildren(_:))*