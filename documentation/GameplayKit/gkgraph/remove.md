# remove(_:)

**Framework**: GameplayKit  
**Kind**: method

Removes the specified nodes from the graph.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func remove(_ nodes: [GKGraphNode])
```

#### Discussion

This method has no effect on nodes in the array that are not in the graph.

## Parameters

- `nodes`: A node in the graph.

## See Also

- [func add([GKGraphNode])](gkgraph/add(_:).md)
  Adds the specified nodes to the graph.
- [func connectToLowestCostNode(node: GKGraphNode, bidirectional: Bool)](gkgraph/connecttolowestcostnode(node:bidirectional:).md)
  Adds a node to the graph, connecting it to the node already in the graph for which the connection has the lowest cost.
- [var nodes: [GKGraphNode]?](gkgraph/nodes.md)
  The list of nodes in the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgraph/remove(_:))*