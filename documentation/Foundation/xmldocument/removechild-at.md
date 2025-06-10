# removeChild(at:)

**Framework**: Foundation  
**Kind**: method

Removes the child node of the receiver located at a specified position in its array of children.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func removeChild(at index: Int)
```

#### Discussion

Subsequent children have their indexes decreased by one. The removed [`XMLNode`](xmlnode.md) object is autoreleased.

## Parameters

- `index`: An integer identifying the position of an child in the receiver’s array. If   is less than zero or greater than the number of children minus one, an out-of-bounds exception is raised.

## See Also

- [func addChild(XMLNode)](xmldocument/addchild(_:).md)
  Adds a child node after the last of the receiver’s existing children.
- [func insertChild(XMLNode, at: Int)](xmldocument/insertchild(_:at:).md)
  Inserts a node object at specified position in the receiver’s array of children.
- [func insertChildren([XMLNode], at: Int)](xmldocument/insertchildren(_:at:).md)
  Inserts an array of children at a specified position in the receiver’s array of children.
- [func replaceChild(at: Int, with: XMLNode)](xmldocument/replacechild(at:with:).md)
  Replaces the child node of the receiver located at a specified position in its array of children with another node.
- [func setChildren([XMLNode]?)](xmldocument/setchildren(_:).md)
  Sets the child nodes of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/removechild(at:))*