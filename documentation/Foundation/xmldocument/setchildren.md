# setChildren(_:)

**Framework**: Foundation  
**Kind**: method

Sets the child nodes of the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func setChildren(_ children: [XMLNode]?)
```

## Parameters

- `children`: An array of   objects. Each of these objects must represent comments, processing instructions, or the root element; otherwise, an exception is raised. Pass in   to remove all children.

## See Also

- [func addChild(XMLNode)](xmldocument/addchild(_:).md)
  Adds a child node after the last of the receiver’s existing children.
- [func insertChild(XMLNode, at: Int)](xmldocument/insertchild(_:at:).md)
  Inserts a node object at specified position in the receiver’s array of children.
- [func insertChildren([XMLNode], at: Int)](xmldocument/insertchildren(_:at:).md)
  Inserts an array of children at a specified position in the receiver’s array of children.
- [func removeChild(at: Int)](xmldocument/removechild(at:).md)
  Removes the child node of the receiver located at a specified position in its array of children.
- [func replaceChild(at: Int, with: XMLNode)](xmldocument/replacechild(at:with:).md)
  Replaces the child node of the receiver located at a specified position in its array of children with another node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/setchildren(_:))*