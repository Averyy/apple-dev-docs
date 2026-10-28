# remove(_:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) removeNodes:(NSArray<GKGraphNode *> *) nodes;
```

## Discussion

This method has no effect on nodes in the array that are not in the graph.

## Parameters

- `nodes`: A node in the graph.

## See Also

### Working with Nodes in a Graph
- [func add([GKGraphNode])](./add%28_%29.md)
  Adds the specified nodes to the graph.
- [func connectToLowestCostNode(node: GKGraphNode, bidirectional: Bool)](./connecttolowestcostnode%28node,bidirectional%29.md)
  Adds a node to the graph, connecting it to the node already in the graph for which the connection has the lowest cost.
- [var nodes: [GKGraphNode]?](./nodes.md)
  The list of nodes in the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgraph/remove(_:))*