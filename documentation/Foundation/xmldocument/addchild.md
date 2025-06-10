# addChild(_:)

**Framework**: Foundation  
**Kind**: method

Adds a child node after the last of the receiver’s existing children.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func addChild(_ child: XMLNode)
```

## Parameters

- `child`: The   object to be added.

## See Also

- [func insertChild(XMLNode, at: Int)](xmldocument/insertchild(_:at:).md)
  Inserts a node object at specified position in the receiver’s array of children.
- [func insertChildren([XMLNode], at: Int)](xmldocument/insertchildren(_:at:).md)
  Inserts an array of children at a specified position in the receiver’s array of children.
- [func removeChild(at: Int)](xmldocument/removechild(at:).md)
  Removes the child node of the receiver located at a specified position in its array of children.
- [func replaceChild(at: Int, with: XMLNode)](xmldocument/replacechild(at:with:).md)
  Replaces the child node of the receiver located at a specified position in its array of children with another node.
- [func setChildren([XMLNode]?)](xmldocument/setchildren(_:).md)
  Sets the child nodes of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/addchild(_:))*