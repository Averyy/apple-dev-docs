# nodes

**Framework**: GameplayKit  
**Kind**: property

The list of nodes in the graph.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var nodes: [GKGraphNode]? { get }
```

#### Discussion

This array can contain nodes that are not connected to other nodes in the graph.

## See Also

- [func add([GKGraphNode])](gkgraph/add(_:).md)
  Adds the specified nodes to the graph.
- [func connectToLowestCostNode(node: GKGraphNode, bidirectional: Bool)](gkgraph/connecttolowestcostnode(node:bidirectional:).md)
  Adds a node to the graph, connecting it to the node already in the graph for which the connection has the lowest cost.
- [func remove([GKGraphNode])](gkgraph/remove(_:).md)
  Removes the specified nodes from the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgraph/nodes)*