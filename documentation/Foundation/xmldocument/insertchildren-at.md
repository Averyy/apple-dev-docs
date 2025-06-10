# insertChildren(_:at:)

**Framework**: Foundation  
**Kind**: method

Inserts an array of children at a specified position in the receiver’s array of children.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func insertChildren(_ children: [XMLNode], at index: Int)
```

## Parameters

- `children`: An array of   objects representing comments, processing instructions, or the root element.
- `index`: An integer identifying the location in the receiver’s children array for insertion. The indexes of children after the new child are increased by  ]. If   is less than zero or greater than the number of children, an out-of-bounds exception is raised.

## See Also

- [func addChild(XMLNode)](xmldocument/addchild(_:).md)
  Adds a child node after the last of the receiver’s existing children.
- [func insertChild(XMLNode, at: Int)](xmldocument/insertchild(_:at:).md)
  Inserts a node object at specified position in the receiver’s array of children.
- [func removeChild(at: Int)](xmldocument/removechild(at:).md)
  Removes the child node of the receiver located at a specified position in its array of children.
- [func replaceChild(at: Int, with: XMLNode)](xmldocument/replacechild(at:with:).md)
  Replaces the child node of the receiver located at a specified position in its array of children with another node.
- [func setChildren([XMLNode]?)](xmldocument/setchildren(_:).md)
  Sets the child nodes of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/insertchildren(_:at:))*