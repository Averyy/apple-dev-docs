# setChildren(_:)

**Framework**: Foundation  
**Kind**: method

Sets all child nodes of the receiver at once, replacing any existing children.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func setChildren(_ children: [XMLNode]?)
```

#### Discussion

Send this message with `children` as `nil` to remove all child nodes.

## Parameters

- `children`: An array of   objects or   objects of kinds  ,  ,  , or  .

## See Also

- [func addChild(XMLNode)](xmlelement/addchild(_:).md)
  Adds a child node at the end of the receiver’s current list of children.
- [func insertChild(XMLNode, at: Int)](xmlelement/insertchild(_:at:).md)
  Inserts a new child node at a specified location in the receiver’s list of child nodes.
- [func insertChildren([XMLNode], at: Int)](xmlelement/insertchildren(_:at:).md)
  Inserts an array of child nodes at a specified location in the receiver’s list of children.
- [func removeChild(at: Int)](xmlelement/removechild(at:).md)
  Removes the child node of the receiver identified by a given index.
- [func replaceChild(at: Int, with: XMLNode)](xmlelement/replacechild(at:with:).md)
  Replaces a child node at a specified location with another child node.
- [func normalizeAdjacentTextNodesPreservingCDATA(Bool)](xmlelement/normalizeadjacenttextnodespreservingcdata(_:).md)
  Coalesces adjacent text nodes of the receiver that you have explicitly added, optionally including CDATA sections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/setchildren(_:))*