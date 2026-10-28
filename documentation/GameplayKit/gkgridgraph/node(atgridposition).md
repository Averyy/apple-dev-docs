# node(atGridPosition:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

Returns the node in the graph at the specified grid coordinates.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func node(atGridPosition position: vector_int2) -> NodeType?
```

```objc
- (NodeType) nodeAtGridPosition:(vector_int2) position;
```

## Return Value

The grid node at the specified location, or `nil` if there is no node at that location.

## Discussion

This method finds nodes that are part of the grid created by the graph. You can attach other nodes to the graph (for example, to represent the positions of game entities in the grid) with the [`connectToAdjacentNodes(node:)`](./connecttoadjacentnodes%28node%29.md) method, but such nodes are not part of the grid itself.

## Parameters

- `position`: The grid location to query.

## See Also

### Working with Nodes
- [func connectToAdjacentNodes(node: GKGridGraphNode)](./connecttoadjacentnodes%28node%29.md)
  Adds the specified node to the graph, connecting it to its nearest neighbors in the grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgridgraph/node(atgridposition:))*