# insertChild(_:at:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Inserts a child node in the receiver’s list of children at a specific location in the list.

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

- `child`: An XML-node object that represents the child to insert.
- `index`: An integer identifying the location in the receiver’s list of children to insert `child`. The indices of subsequent children in the list are incremented by one.

## See Also

### Manipulating Child Nodes
- [func addChild(XMLNode)](./addchild%28_%29.md)
  Adds a child node to the end of the list of existing children.
- [func insertChildren([XMLNode], at: Int)](./insertchildren%28_,at%29.md)
  Inserts an array of child nodes at a specified location in the receiver’s list of children.
- [func removeChild(at: Int)](./removechild%28at%29.md)
  Removes the child node at a particular location in the receiver’s list of children.
- [func replaceChild(at: Int, with: XMLNode)](./replacechild%28at,with%29.md)
  Replaces a child at a particular index with another child.
- [func setChildren([XMLNode]?)](./setchildren%28_%29.md)
  Removes all existing children of the receiver and replaces them with an array of new child nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldtd/insertchild(_:at:))*