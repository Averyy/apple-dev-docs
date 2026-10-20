# insertChildren(_:at:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Inserts an array of child nodes at a specified location in the receiver’s list of children.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func insertChildren(_ children: [XMLNode], at index: Int)
```

```objc
- (void) insertChildren:(NSArray<NSXMLNode *> *) children atIndex:(NSUInteger) index;
```

#### Discussion

Insertion of the node increases the indexes of sibling nodes after it by the count of `children`.

## Parameters

- `children`: An array of XML node objects to add as children of the receiver.
- `index`: An integer identifying a position in the receiver’s list of children. An exception is raised if `index` is out of bounds.

## See Also

### Manipulating Child Elements
- [func addChild(XMLNode)](./addchild%28_%29.md)
  Adds a child node at the end of the receiver’s current list of children.
- [func insertChild(XMLNode, at: Int)](./insertchild%28_,at%29.md)
  Inserts a new child node at a specified location in the receiver’s list of child nodes.
- [func removeChild(at: Int)](./removechild%28at%29.md)
  Removes the child node of the receiver identified by a given index.
- [func replaceChild(at: Int, with: XMLNode)](./replacechild%28at,with%29.md)
  Replaces a child node at a specified location with another child node.
- [func setChildren([XMLNode]?)](./setchildren%28_%29.md)
  Sets all child nodes of the receiver at once, replacing any existing children.
- [func normalizeAdjacentTextNodesPreservingCDATA(Bool)](./normalizeadjacenttextnodespreservingcdata%28_%29.md)
  Coalesces adjacent text nodes of the receiver that you have explicitly added, optionally including CDATA sections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/insertchildren(_:at:))*