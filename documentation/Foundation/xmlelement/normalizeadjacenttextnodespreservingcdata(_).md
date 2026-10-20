# normalizeAdjacentTextNodesPreservingCDATA(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Coalesces adjacent text nodes of the receiver that you have explicitly added, optionally including CDATA sections.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func normalizeAdjacentTextNodesPreservingCDATA(_ preserve: Bool)
```

```objc
- (void) normalizeAdjacentTextNodesPreservingCDATA:(BOOL) preserve;
```

#### Discussion

A text node with a value of an empty string is removed. When you process an input source of XML, adjacent text nodes are automatically normalized. You should invoke this method (with `preserve` as [`false`](../../Swift/false.md)) before using the [`XMLNode`](../xmlnode.md) methods [`objects(forXQuery:constants:)`](../xmlnode/objects%28forxquery,constants%29.md) or [`nodes(forXPath:)`](../xmlnode/nodes%28forxpath%29.md).

## Parameters

- `preserve`: [`true`](../../Swift/true.md) if CDATA sections are left alone as text nodes, [`false`](../../Swift/false.md) otherwise.

## See Also

### Manipulating Child Elements
- [func addChild(XMLNode)](./addchild%28_%29.md)
  Adds a child node at the end of the receiver’s current list of children.
- [func insertChild(XMLNode, at: Int)](./insertchild%28_,at%29.md)
  Inserts a new child node at a specified location in the receiver’s list of child nodes.
- [func insertChildren([XMLNode], at: Int)](./insertchildren%28_,at%29.md)
  Inserts an array of child nodes at a specified location in the receiver’s list of children.
- [func removeChild(at: Int)](./removechild%28at%29.md)
  Removes the child node of the receiver identified by a given index.
- [func replaceChild(at: Int, with: XMLNode)](./replacechild%28at,with%29.md)
  Replaces a child node at a specified location with another child node.
- [func setChildren([XMLNode]?)](./setchildren%28_%29.md)
  Sets all child nodes of the receiver at once, replacing any existing children.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/normalizeadjacenttextnodespreservingcdata(_:))*