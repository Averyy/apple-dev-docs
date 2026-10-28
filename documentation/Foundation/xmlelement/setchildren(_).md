# setChildren(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets all child nodes of the receiver at once, replacing any existing children.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func setChildren(_ children: [XMLNode]?)
```

```objc
- (void) setChildren:(NSArray<NSXMLNode *> *) children;
```

## Discussion

Send this message with `children` as `nil` to remove all child nodes.

## Parameters

- `children`: An array of `NSXMLElement` objects or [`XMLNode`](../xmlnode.md) objects of kinds [`XMLNode.Kind.element`](../xmlnode/kind-swift.enum/element.md), [`XMLNode.Kind.processingInstruction`](../xmlnode/kind-swift.enum/processinginstruction.md), [`XMLNode.Kind.text`](../xmlnode/kind-swift.enum/text.md), or [`XMLNode.Kind.comment`](../xmlnode/kind-swift.enum/comment.md).

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
- [func normalizeAdjacentTextNodesPreservingCDATA(Bool)](./normalizeadjacenttextnodespreservingcdata%28_%29.md)
  Coalesces adjacent text nodes of the receiver that you have explicitly added, optionally including CDATA sections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/setchildren(_:))*