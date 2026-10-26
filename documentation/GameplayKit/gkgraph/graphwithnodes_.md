# graphWithNodes:

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Type Method

Creates a graph with the specified list of nodes.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) graphWithNodes:(NSArray<GKGraphNode *> *) nodes;
```

#### Return Value

A new graph object.

#### Discussion

The nodes in the array need not already be connected—you can connect nodes after adding them to the graph using the [`connectToLowestCostNode(node:bidirectional:)`](./connecttolowestcostnode%28node,bidirectional%29.md) method on the graph itself or the addConnection:bidirectional: method on individual nodes. Using the [`findPath(from:to:)`](./findpath%28from,to%29.md) method requires connections between nodes.

## Parameters

- `nodes`: An array of graph node objects—instances of [`GKGraphNode`](../gkgraphnode.md) or of one of its subclasses that adds geometry information.

## See Also

### Creating a Graph
- [init([GKGraphNode])](./init%28_%29.md)
  Initializes a graph with the specified list of nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgraph/graphwithnodes:)*