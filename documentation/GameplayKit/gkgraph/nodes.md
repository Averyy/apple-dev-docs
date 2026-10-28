# nodes

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, nullable) NSArray<GKGraphNode *> * nodes;
```

## Discussion

This array can contain nodes that are not connected to other nodes in the graph.

## See Also

### Working with Nodes in a Graph
- [func add([GKGraphNode])](./add%28_%29.md)
  Adds the specified nodes to the graph.
- [func connectToLowestCostNode(node: GKGraphNode, bidirectional: Bool)](./connecttolowestcostnode%28node,bidirectional%29.md)
  Adds a node to the graph, connecting it to the node already in the graph for which the connection has the lowest cost.
- [func remove([GKGraphNode])](./remove%28_%29.md)
  Removes the specified nodes from the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgraph/nodes)*