# insertChild(_:at:)

**Framework**: Foundation  
**Kind**: method

Inserts a node object at specified position in the receiver’s array of children.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func insertChild(_ child: XMLNode, at index: Int)
```

## Parameters

- `child`: The   object to be inserted. The added node must be an   object representing a comment, processing instruction, or the root element.
- `index`: An integer specifying the index of the children array to insert  . The indexes of children after the new child are incremented. If   is less than zero or greater than the number of children, an out-of-bounds exception is raised.

## See Also

- [func addChild(XMLNode)](xmldocument/addchild(_:).md)
  Adds a child node after the last of the receiver’s existing children.
- [func insertChildren([XMLNode], at: Int)](xmldocument/insertchildren(_:at:).md)
  Inserts an array of children at a specified position in the receiver’s array of children.
- [func removeChild(at: Int)](xmldocument/removechild(at:).md)
  Removes the child node of the receiver located at a specified position in its array of children.
- [func replaceChild(at: Int, with: XMLNode)](xmldocument/replacechild(at:with:).md)
  Replaces the child node of the receiver located at a specified position in its array of children with another node.
- [func setChildren([XMLNode]?)](xmldocument/setchildren(_:).md)
  Sets the child nodes of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/insertchild(_:at:))*