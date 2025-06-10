# replaceChild(at:with:)

**Framework**: Foundation  
**Kind**: method

Replaces a child node at a specified location with another child node.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func replaceChild(at index: Int, with node: XMLNode)
```

#### Discussion

The replaced XML node object is released upon removal.

## Parameters

- `index`: An integer identifying a position in the receiver’s list of children. An exception is raised if   is out of bounds.
- `node`: An XML node object that will replace the current child.

## See Also

- [func addChild(XMLNode)](xmlelement/addchild(_:).md)
  Adds a child node at the end of the receiver’s current list of children.
- [func insertChild(XMLNode, at: Int)](xmlelement/insertchild(_:at:).md)
  Inserts a new child node at a specified location in the receiver’s list of child nodes.
- [func insertChildren([XMLNode], at: Int)](xmlelement/insertchildren(_:at:).md)
  Inserts an array of child nodes at a specified location in the receiver’s list of children.
- [func removeChild(at: Int)](xmlelement/removechild(at:).md)
  Removes the child node of the receiver identified by a given index.
- [func setChildren([XMLNode]?)](xmlelement/setchildren(_:).md)
  Sets all child nodes of the receiver at once, replacing any existing children.
- [func normalizeAdjacentTextNodesPreservingCDATA(Bool)](xmlelement/normalizeadjacenttextnodespreservingcdata(_:).md)
  Coalesces adjacent text nodes of the receiver that you have explicitly added, optionally including CDATA sections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/replacechild(at:with:))*