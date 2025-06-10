# insertChild(_:at:)

**Framework**: Foundation  
**Kind**: method

Inserts a new child node at a specified location in the receiver’s list of child nodes.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func insertChild(_ child: XMLNode, at index: Int)
```

#### Discussion

Insertion of the node increments the indexes of sibling nodes after it.

## Parameters

- `child`: An XML node object to be inserted as a child of the receiver.
- `index`: An integer identifying a position in the receiver’s list of children. An exception is raised if   is out of bounds.

## See Also

- [func addChild(XMLNode)](xmlelement/addchild(_:).md)
  Adds a child node at the end of the receiver’s current list of children.
- [func insertChildren([XMLNode], at: Int)](xmlelement/insertchildren(_:at:).md)
  Inserts an array of child nodes at a specified location in the receiver’s list of children.
- [func removeChild(at: Int)](xmlelement/removechild(at:).md)
  Removes the child node of the receiver identified by a given index.
- [func replaceChild(at: Int, with: XMLNode)](xmlelement/replacechild(at:with:).md)
  Replaces a child node at a specified location with another child node.
- [func setChildren([XMLNode]?)](xmlelement/setchildren(_:).md)
  Sets all child nodes of the receiver at once, replacing any existing children.
- [func normalizeAdjacentTextNodesPreservingCDATA(Bool)](xmlelement/normalizeadjacenttextnodespreservingcdata(_:).md)
  Coalesces adjacent text nodes of the receiver that you have explicitly added, optionally including CDATA sections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/insertchild(_:at:))*