# isConnectionLocked(from:to:)

**Framework**: GameplayKit  
**Kind**: method

Returns a Boolean value indicating whether the specified nodes are protected from disconnection due to the addition of obstacles.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func isConnectionLocked(from startNode: NodeType, to endNode: NodeType) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the connection between the specified nodes has been locked with the [`lockConnection(from:to:)`](gkobstaclegraph/lockconnection(from:to:).md) method; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

By default, adding obstacles with the [`addObstacles(_:)`](gkobstaclegraph/addobstacles(_:).md) method disconnects pairs of nodes if the direct path between them intersects an obstacle. This behavior ensures that using the findPathBetweenNodes:toNode: method does not result in a path through the graph that crosses obstacles. With certain nodes, this behavior might not be desirable—use the [`lockConnection(from:to:)`](gkobstaclegraph/lockconnection(from:to:).md) method to protect a connection between nodes from being automatically destroyed and the [`unlockConnection(from:to:)`](gkobstaclegraph/unlockconnection(from:to:).md) method to remove such protection.

## Parameters

- `startNode`: A node in the graph.
- `endNode`: Another node in the graph to which the node   is directly connected.

## See Also

- [func lockConnection(from: NodeType, to: NodeType)](gkobstaclegraph/lockconnection(from:to:).md)
  Prevents the specified nodes from being disconnected due to the addition of obstacles.
- [func unlockConnection(from: NodeType, to: NodeType)](gkobstaclegraph/unlockconnection(from:to:).md)
  Allows the specified nodes to be disconnected due to the addition of obstacles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/isconnectionlocked(from:to:))*