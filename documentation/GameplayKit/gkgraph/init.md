# init(_:)

**Framework**: GameplayKit  
**Kind**: init

Initializes a graph with the specified list of nodes.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(_ nodes: [GKGraphNode])
```

#### Return Value

A new graph object.

#### Discussion

The nodes in the array need not already be connected—you can connect nodes after adding them to the graph using the [`connectToLowestCostNode(node:bidirectional:)`](gkgraph/connecttolowestcostnode(node:bidirectional:).md) method on the graph itself or the addConnection:bidirectional: method on individual nodes. Using the [`findPath(from:to:)`](gkgraph/findpath(from:to:).md) method requires connections between nodes.

For more information, see [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Parameters

- `nodes`: An array of graph node objects—instances of   or of one of its subclasses containing geometry information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgraph/init(_:))*