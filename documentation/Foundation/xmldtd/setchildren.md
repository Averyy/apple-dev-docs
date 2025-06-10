# setChildren(_:)

**Framework**: Foundation  
**Kind**: method

Removes all existing children of the receiver and replaces them with an array of new child nodes.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func setChildren(_ children: [XMLNode]?)
```

#### Discussion

Replaced or removed child nodes are released.

## Parameters

- `children`: An array of   objects. To remove all existing children, pass in  .

## See Also

- [func addChild(XMLNode)](xmldtd/addchild(_:).md)
  Adds a child node to the end of the list of existing children.
- [func insertChild(XMLNode, at: Int)](xmldtd/insertchild(_:at:).md)
  Inserts a child node in the receiver’s list of children at a specific location in the list.
- [func insertChildren([XMLNode], at: Int)](xmldtd/insertchildren(_:at:).md)
  Inserts an array of child nodes at a specified location in the receiver’s list of children.
- [func removeChild(at: Int)](xmldtd/removechild(at:).md)
  Removes the child node at a particular location in the receiver’s list of children.
- [func replaceChild(at: Int, with: XMLNode)](xmldtd/replacechild(at:with:).md)
  Replaces a child at a particular index with another child.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldtd/setchildren(_:))*