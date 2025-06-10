# insertChild(_:at:)

**Framework**: Foundation  
**Kind**: method

Inserts a child node in the receiver’s list of children at a specific location in the list.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func insertChild(_ child: XMLNode, at index: Int)
```

## Parameters

- `child`: An XML-node object that represents the child to insert.
- `index`: An integer identifying the location in the receiver’s list of children to insert  . The indices of subsequent children in the list are incremented by one.

## See Also

- [func addChild(XMLNode)](xmldtd/addchild(_:).md)
  Adds a child node to the end of the list of existing children.
- [func insertChildren([XMLNode], at: Int)](xmldtd/insertchildren(_:at:).md)
  Inserts an array of child nodes at a specified location in the receiver’s list of children.
- [func removeChild(at: Int)](xmldtd/removechild(at:).md)
  Removes the child node at a particular location in the receiver’s list of children.
- [func replaceChild(at: Int, with: XMLNode)](xmldtd/replacechild(at:with:).md)
  Replaces a child at a particular index with another child.
- [func setChildren([XMLNode]?)](xmldtd/setchildren(_:).md)
  Removes all existing children of the receiver and replaces them with an array of new child nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldtd/insertchild(_:at:))*