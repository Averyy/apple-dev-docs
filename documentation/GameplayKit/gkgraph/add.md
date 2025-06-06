# add(_:)

**Framework**: GameplayKit  
**Kind**: method

Adds the specified nodes to the graph.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func add(_ nodes: [GKGraphNode])
```

#### Discussion

Calling this method does not connect the newly added nodes to others in the graph.

## Parameters

- `nodes`: An array of graph node objects—instances of   or of one of its subclasses that adds geometry information.

## See Also

- [func connectToLowestCostNode(node: GKGraphNode, bidirectional: Bool)](gkgraph/connecttolowestcostnode(node:bidirectional:).md)
  Adds a node to the graph, connecting it to the node already in the graph for which the connection has the lowest cost.
- [func remove([GKGraphNode])](gkgraph/remove(_:).md)
  Removes the specified nodes from the graph.
- [var nodes: [GKGraphNode]?](gkgraph/nodes.md)
  The list of nodes in the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgraph/add(_:))*