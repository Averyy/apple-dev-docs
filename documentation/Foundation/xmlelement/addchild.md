# addChild(_:)

**Framework**: Foundation  
**Kind**: method

Adds a child node at the end of the receiver’s current list of children.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func addChild(_ child: XMLNode)
```

#### Discussion

The new node has an index value that is one greater than the last of the current children.

## Parameters

- `child`: An XML node object to add to the receiver’s children.

## See Also

- [func insertChild(XMLNode, at: Int)](xmlelement/insertchild(_:at:).md)
  Inserts a new child node at a specified location in the receiver’s list of child nodes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/addchild(_:))*