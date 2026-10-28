# isConnectionLocked(from:to:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) isConnectionLockedFromNode:(NodeType) startNode toNode:(NodeType) endNode;
```

## Return Value

[`true`](../../Swift/true.md) if the connection between the specified nodes has been locked with the [`lockConnection(from:to:)`](./lockconnection%28from,to%29.md) method; otherwise, [`false`](../../Swift/false.md).

## Discussion

By default, adding obstacles with the [`addObstacles(_:)`](./addobstacles%28_%29.md) method disconnects pairs of nodes if the direct path between them intersects an obstacle. This behavior ensures that using the findPathBetweenNodes:toNode: method does not result in a path through the graph that crosses obstacles. With certain nodes, this behavior might not be desirable—use the [`lockConnection(from:to:)`](./lockconnection%28from,to%29.md) method to protect a connection between nodes from being automatically destroyed and the [`unlockConnection(from:to:)`](./unlockconnection%28from,to%29.md) method to remove such protection.

## Parameters

- `startNode`: A node in the graph.
- `endNode`: Another node in the graph to which the node `startNode` is directly connected.

## See Also

### Locking Node Connections
- [func lockConnection(from: NodeType, to: NodeType)](./lockconnection%28from,to%29.md)
  Prevents the specified nodes from being disconnected due to the addition of obstacles.
- [func unlockConnection(from: NodeType, to: NodeType)](./unlockconnection%28from,to%29.md)
  Allows the specified nodes to be disconnected due to the addition of obstacles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/isconnectionlocked(from:to:))*