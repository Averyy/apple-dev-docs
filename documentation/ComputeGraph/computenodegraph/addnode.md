# addNode(_:)

**Framework**: ComputeGraph  
**Kind**: method

Adds a node to the graph.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

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