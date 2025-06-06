# estimatedCost(to:)

**Framework**: GameplayKit  
**Kind**: method

Returns an underestimate of the cost of travel from this node to the specified node.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func estimatedCost(to node: GKGraphNode) -> Float
```

#### Return Value

An underestimate of the travel cost to the specified node; higher values indicate higher cost.

#### Discussion

The [`GKGraph`](gkgraph.md) class uses this method in pathfinding between nodes—the [`findPath(from:to:)`](gkgraph/findpath(from:to:).md) method finds the lowest-cost path between a specified pair of nodes. (See the [`cost(to:)`](gkgraphnode/cost(to:).md) method for further discussion.) The pathfinding algorithm involves successive approximation using a heuristic in order to avoid processing too many nodes. The [`estimatedCost(to:)`](gkgraphnode/estimatedcost(to:).md) method provides that heuristic—a quickly computed estimated cost of travel helps the algorithm choose which nodes to process in order to compute the real cost of travel.

The estimated cost must be an  of the true cost—that is, in order for the pathfinding algorithm to produce correct results, the heuristic value must not exceed the true cost of travel between nodes. For example, in a 2D graph, the straight-line distance between two distant nodes is an admissible heuristic, because the actual path found will at best be along that line, but might be along a longer path. The subclasses [`GKGraphNode2D`](gkgraphnode2d.md), [`GKGraphNode3D`](gkgraphnode3d.md), and [`GKGridGraphNode`](gkgridgraphnode.md) use this approach.

Custom subclasses can implement this method to add game-specific information that might improve the quality of an estimated cost.

## Parameters

- `node`: A node connected (directly or indirectly) to this node.

## See Also

- [func cost(to: GKGraphNode) -> Float](gkgraphnode/cost(to:).md)
  Returns the cost to travel from this node to the specified, directly connected, node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgraphnode/estimatedcost(to:))*