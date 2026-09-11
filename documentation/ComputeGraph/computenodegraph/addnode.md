# addNode(_:)

**Framework**: Compute Graph  
**Kind**: method

Adds a node to the graph.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- Reality Composer Pro ?+

## Declaration

```swift
mutating func addNode(_ node: ComputeNodeGraph.Node) throws -> ComputeNodeGraph.NodeID
```

#### Return Value

The key assigned to the newly added node.

#### Discussion

> **Note**: A `NodeError` if the node cannot be added.

## Parameters

- `node`: The node to add.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/addnode(_:))*