# replaceChild(at:with:)

**Framework**: Foundation  
**Kind**: method

Replaces a child at a particular index with another child.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func replaceChild(at index: Int, with node: XMLNode)
```

#### Discussion

The replaced child node is released.

## Parameters

- `index`: An integer identifying the position of a node in the receiver’s list of child nodes.
- `node`: An   object to replace the object at  .

## See Also

- [func addChild(XMLNode)](xmldtd/addchild(_:).md)
  Adds a child node to the end of the list of existing children.
- [func insertChild(XMLNode, at: Int)](xmldtd/insertchild(_:at:).md)
  Inserts a child node in the receiver’s list of children at a specific location in the list.
- [func insertChildren([XMLNode], at: Int)](xmldtd/insertchildren(_:at:).md)
  Inserts an array of child nodes at a specified location in the receiver’s list of children.
- [func removeChild(at: Int)](xmldtd/removechild(at:).md)
  Removes the child node at a particular location in the receiver’s list of children.
- [func setChildren([XMLNode]?)](xmldtd/setchildren(_:).md)
  Removes all existing children of the receiver and replaces them with an array of new child nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldtd/replacechild(at:with:))*