# connectToAdjacentNodes(node:)

**Framework**: GameplayKit  
**Kind**: method

Adds the specified node to the graph, connecting it to its nearest neighbors in the grid.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func connectToAdjacentNodes(node: GKGridGraphNode)
```

#### Discussion

Nodes attached through this method do not become part of the grid itself, but instead can represent positions of game entities in the grid. Use nodes connected in this way to find paths between such positions.

## Parameters

- `node`: A graph node object containing integer grid coordinate information.

## See Also

- [func node(atGridPosition: vector_int2) -> NodeType?](gkgridgraph/node(atgridposition:).md)
  Returns the node in the graph at the specified grid coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgridgraph/connecttoadjacentnodes(node:))*