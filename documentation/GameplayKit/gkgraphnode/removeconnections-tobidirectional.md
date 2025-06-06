# removeConnections(to:bidirectional:)

**Framework**: GameplayKit  
**Kind**: method

Removes the connections from this node to the specified nodes.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func removeConnections(to nodes: [GKGraphNode], bidirectional: Bool)
```

#### Discussion

In GameplayKit, the connections between nodes in a graph are directional. For example, if the [`connectedNodes`](gkgraphnode/connectednodes.md) list of Node A contains Node B, then a traveler on the graph can move directly from Node A to Node B. For the reverse to also be true, the [`connectedNodes`](gkgraphnode/connectednodes.md) list of Node B must contain Node A. When calling this method to remove a connection from one node to another, use the `bidirectional` parameter to choose whether to automatically remove the reverse connection as well.

## Parameters

- `nodes`: The nodes connected to this node whose connections are to be removed.
- `bidirectional`:   to remove connections in both directions if they exist;   to remove only connections from this node to each of the specified nodes.

## See Also

- [var connectedNodes: [GKGraphNode]](gkgraphnode/connectednodes.md)
  The list of other nodes connected to this node.
- [func addConnections(to: [GKGraphNode], bidirectional: Bool)](gkgraphnode/addconnections(to:bidirectional:).md)
  Connects this node to all nodes in the specified list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgraphnode/removeconnections(to:bidirectional:))*