# normalizeAdjacentTextNodesPreservingCDATA(_:)

**Framework**: Foundation  
**Kind**: method

Coalesces adjacent text nodes of the receiver that you have explicitly added, optionally including CDATA sections.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func normalizeAdjacentTextNodesPreservingCDATA(_ preserve: Bool)
```

#### Discussion

A text node with a value of an empty string is removed. When you process an input source of XML, adjacent text nodes are automatically normalized. You should invoke this method (with `preserve` as [`false`](https://developer.apple.com/documentation/Swift/false)) before using the [`XMLNode`](xmlnode.md) methods [`objects(forXQuery:constants:)`](xmlnode/objects(forxquery:constants:).md) or [`nodes(forXPath:)`](xmlnode/nodes(forxpath:).md).

## Parameters

- `preserve`:   if CDATA sections are left alone as text nodes,   otherwise.

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
- [func setChildren([XMLNode]?)](xmlelement/setchildren(_:).md)
  Sets all child nodes of the receiver at once, replacing any existing children.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/normalizeadjacenttextnodespreservingcdata(_:))*