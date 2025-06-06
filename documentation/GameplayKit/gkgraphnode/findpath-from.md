# findPath(from:)

**Framework**: GameplayKit  
**Kind**: method

Computes and returns a sequence of nodes that represents the lowest-cost graph traversal from the specified node to this node.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func findPath(from startNode: GKGraphNode) -> [GKGraphNode]
```

#### Return Value

An array of nodes representing a path through the graph in start to end order, or an empty array if no path exists between the specified nodes.

#### Discussion

This method is equivalent to the [`findPath(to:)`](gkgraphnode/findpath(to:).md) method, but finds a path from the specified node to this node, rather than the other way around. Connections in a graph are directional—that is, a connection from Node A to Node B indicates only that travel is possible from A to B, and indicating that travel from B to A is also possible requires a separate connection. Therefore, calling the [`findPath(to:)`](gkgraphnode/findpath(to:).md) and [`findPath(from:)`](gkgraphnode/findpath(from:).md) methods with the same pair of nodes might not always return the same paths.

## Parameters

- `startNode`: The origin node from which to attempt traversal of the graph.

## See Also

- [func findPath(to: GKGraphNode) -> [GKGraphNode]](gkgraphnode/findpath(to:).md)
  Computes and returns a sequence of nodes that represents the lowest-cost graph traversal from this node to the specified node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgraphnode/findpath(from:))*