# lockConnection(from:to:)

**Framework**: GameplayKit  
**Kind**: method

Prevents the specified nodes from being disconnected due to the addition of obstacles.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func lockConnection(from startNode: NodeType, to endNode: NodeType)
```

#### Discussion

By default, adding obstacles with the [`addObstacles(_:)`](gkobstaclegraph/addobstacles(_:).md) method disconnects pairs of nodes if the direct path between them intersects an obstacle. This behavior ensures that using the findPathBetweenNodes:toNode: method does not result in a path through the graph that crosses obstacles.

With certain nodes, such as those you add with the [`connectUsingObstacles(node:)`](gkobstaclegraph/connectusingobstacles(node:).md) method to represent the position of a game character or objective, this behavior might not be desirable. For example, if you add an obstacle that overlaps a character’s current position, the character should be able to find a path that exits the obstacle. In this case, use the [`unlockConnection(from:to:)`](gkobstaclegraph/unlockconnection(from:to:).md) method to protect the connection between the character’s node and a neighboring node from being automatically destroyed. If you later rearrange nodes so that such protection is no longer necessary, use the [`unlockConnection(from:to:)`](gkobstaclegraph/unlockconnection(from:to:).md) method to remove it.

## Parameters

- `startNode`: A node in the graph.
- `endNode`: Another node in the graph to which the node   is directly connected.

## See Also

- [func unlockConnection(from: NodeType, to: NodeType)](gkobstaclegraph/unlockconnection(from:to:).md)
  Allows the specified nodes to be disconnected due to the addition of obstacles.
- [func isConnectionLocked(from: NodeType, to: NodeType) -> Bool](gkobstaclegraph/isconnectionlocked(from:to:).md)
  Returns a Boolean value indicating whether the specified nodes are protected from disconnection due to the addition of obstacles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/lockconnection(from:to:))*