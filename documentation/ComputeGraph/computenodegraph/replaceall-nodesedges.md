# replaceAll(nodes:edges:)

**Framework**: Compute Graph  
**Kind**: method

Replaces all nodes and edges in the graph with the provided collections.

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
mutating func replaceAll(nodes: [ComputeNodeGraph.NodeID : ComputeNodeGraph.Node], edges: [ComputeNodeGraph.Edge]) throws
```

#### Discussion

This bulk operation allows for efficient wholesale replacement of the graph’s structure.

> **Note**: An error if the replacement operation fails.

## Parameters

- `nodes`: A sequence of nodes and their keys to add to the graph.
- `edges`: A sequence of edges to add to the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/replaceall(nodes:edges:))*