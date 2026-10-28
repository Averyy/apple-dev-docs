# addChild(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Adds a child node at the end of the receiver’s current list of children.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func addChild(_ child: XMLNode)
```

```objc
- (void) addChild:(NSXMLNode *) child;
```

## Discussion

The new node has an index value that is one greater than the last of the current children.

## Parameters

- `child`: An XML node object to add to the receiver’s children.

## See Also

### Manipulating Child Elements
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
- [func normalizeAdjacentTextNodesPreservingCDATA(Bool)](./normalizeadjacenttextnodespreservingcdata%28_%29.md)
  Coalesces adjacent text nodes of the receiver that you have explicitly added, optionally including CDATA sections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/addchild(_:))*