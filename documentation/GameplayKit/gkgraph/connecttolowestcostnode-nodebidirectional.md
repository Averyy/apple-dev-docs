# connectToLowestCostNode(node:bidirectional:)

**Framework**: GameplayKit  
**Kind**: method

Adds a node to the graph, connecting it to the node already in the graph for which the connection has the lowest cost.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func connectToLowestCostNode(node: GKGraphNode, bidirectional: Bool)
```

#### Discussion

This method uses the [`cost(to:)`](gkgraphnode/cost(to:).md) method of the specified node to find the node already in the graph that is most easily reached from the new node. For nodes that contain geometry information ([`GKGraphNode2D`](gkgraphnode2d.md) or [`GKGridGraphNode`](gkgridgraphnode.md) objects), cost is by default based on distance, so this method connects the new node to the geometrically closest node already in the graph. If you create a custom [`GKGraphNode`](gkgraphnode.md) subclass, this method selects the “closest” node according to whatever algorithm you implement in your [`cost(to:)`](gkgraphnode/cost(to:).md) method.

Using this method with an instance of the [`GKGraphNode`](gkgraphnode.md) base class is not recommended.

## Parameters

- `node`: A graph node object.
- `bidirectional`:   to create connections in both directions;   to create just a single connection from the nearest node to the newly added node.

## See Also

- [func add([GKGraphNode])](gkgraph/add(_:).md)
  Adds the specified nodes to the graph.
- [func remove([GKGraphNode])](gkgraph/remove(_:).md)
  Removes the specified nodes from the graph.
- [var nodes: [GKGraphNode]?](gkgraph/nodes.md)
  The list of nodes in the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgraph/connecttolowestcostnode(node:bidirectional:))*