# replaceChild(at:with:)

**Framework**: Foundation  
**Kind**: method

Replaces the child node of the receiver located at a specified position in its array of children with another node.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func replaceChild(at index: Int, with node: XMLNode)
```

#### Discussion

The removed `NSXMLNode` object is autoreleased.

## Parameters

- `index`: An integer identifying a position in the receiver’s array of children. If   is less than zero or greater than the number of children minus one, an out-of-bounds exception is raised.
- `node`: An   object to replace the one at  ; it must represent a comment, a processing instruction, or the root element.

## See Also

- [func addChild(XMLNode)](xmldocument/addchild(_:).md)
  Adds a child node after the last of the receiver’s existing children.
- [func insertChild(XMLNode, at: Int)](xmldocument/insertchild(_:at:).md)
  Inserts a node object at specified position in the receiver’s array of children.
- [func insertChildren([XMLNode], at: Int)](xmldocument/insertchildren(_:at:).md)
  Inserts an array of children at a specified position in the receiver’s array of children.
- [func removeChild(at: Int)](xmldocument/removechild(at:).md)
  Removes the child node of the receiver located at a specified position in its array of children.
- [func setChildren([XMLNode]?)](xmldocument/setchildren(_:).md)
  Sets the child nodes of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/replacechild(at:with:))*