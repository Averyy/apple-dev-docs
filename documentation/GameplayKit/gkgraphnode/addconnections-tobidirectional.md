# addConnections(to:bidirectional:)

**Framework**: GameplayKit  
**Kind**: method

Connects this node to all nodes in the specified list.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func addConnections(to nodes: [GKGraphNode], bidirectional: Bool)
```

#### Discussion

In GameplayKit, the connections between nodes in a graph are directional. For example, if the [`connectedNodes`](gkgraphnode/connectednodes.md) list of Node A contains Node B, then a traveler on the graph can move directly from Node A to Node B. For the reverse to also be true, the [`connectedNodes`](gkgraphnode/connectednodes.md) list of Node B must contain Node A. Use the `bidirectional` parameter to choose whether to automatically create connections in both directions or create only one-way connections.

## Parameters

- `nodes`: The list of nodes to which to form connections.
- `bidirectional`:   to create a connection in both directions;   to create only connections from this node to each of the specified nodes.

## See Also

- [var connectedNodes: [GKGraphNode]](gkgraphnode/connectednodes.md)
  The list of other nodes connected to this node.
- [func removeConnections(to: [GKGraphNode], bidirectional: Bool)](gkgraphnode/removeconnections(to:bidirectional:).md)
  Removes the connections from this node to the specified nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgraphnode/addconnections(to:bidirectional:))*