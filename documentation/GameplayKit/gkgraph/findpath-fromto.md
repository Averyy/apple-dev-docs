# findPath(from:to:)

**Framework**: GameplayKit  
**Kind**: method

Computes and returns a sequence of nodes that represents the shortest traversal of the graph between the specified nodes.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func findPath(from startNode: GKGraphNode, to endNode: GKGraphNode) -> [GKGraphNode]
```

#### Return Value

An array of nodes representing a path through the graph in start to end order, or an empty array if no path exists between the specified nodes.

#### Discussion

The returned array contains the list of nodes one must traverse in order to follow the selected route, starting with the requested `startNode` object, proceeding along the connections between nodes, and ending with the requested `endNode` object. For graphs whose nodes contain geometry information ([`GKGraphNode2D`](gkgraphnode2d.md) or [`GKGridGraphNode`](gkgridgraphnode.md) objects), you can use the information from each node in the array to move a game object along the path (or otherwise present the path to the user). Or, to make an agent (a [`GKAgent`](gkagent.md) object) automatically follow the returned path, create a [`GKPath`](gkpath.md) object with the [`init(graphNodes:radius:)`](gkpath/init(graphnodes:radius:).md) initializer.

Pathfinding need not be limited to nodes that are contained in the same graph. For example, you might use separate [`GKGraph`](gkgraph.md) objects to represent distinct areas of your game world—when the player will soon move into an adjoining area, you can connect one or more nodes in the current area’s graph to nodes in the new area’s graph. To find paths between nodes that aren’t necessarily in the same graph, use the [`findPath(to:)`](gkgraphnode/findpath(to:).md) method of a specific [`GKGraphNode`](gkgraphnode.md) object.

## Parameters

- `startNode`: The node from which to begin traversing the graph.
- `endNode`: The destination node to which to attempt traversal of the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgraph/findpath(from:to:))*