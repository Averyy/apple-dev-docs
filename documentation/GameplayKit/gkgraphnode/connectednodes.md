# connectedNodes

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

The list of other nodes connected to this node.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var connectedNodes: [GKGraphNode] { get }
```

```objc
@property (nonatomic, readonly) NSArray<GKGraphNode *> * connectedNodes;
```

#### Discussion

In GameplayKit, the connections between nodes in a graph are directional. For example, if the [`connectedNodes`](./connectednodes.md) list of Node A contains Node B, then a traveler on the graph can move directly from Node A to Node B. For the reverse to also be true, the [`connectedNodes`](./connectednodes.md) list of Node B must contain Node A. To conveniently create connections in both directions, use the `bidirectional` parameter of the [`addConnections(to:bidirectional:)`](./addconnections%28to,bidirectional%29.md) method.

For more information, see [GameplayKit Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## See Also

### Working with Connections
- [func addConnections(to: [GKGraphNode], bidirectional: Bool)](./addconnections%28to,bidirectional%29.md)
  Connects this node to all nodes in the specified list.
- [func removeConnections(to: [GKGraphNode], bidirectional: Bool)](./removeconnections%28to,bidirectional%29.md)
  Removes the connections from this node to the specified nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgraphnode/connectednodes)*