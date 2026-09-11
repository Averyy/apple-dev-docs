# removeEdge(_:)

**Framework**: Compute Graph  
**Kind**: method

Removes an edge from the graph.

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
@discardableResult
mutating func removeEdge(_ edge: ComputeNodeGraph.Edge) -> Bool
```

#### Return Value

`true` if the edge was found and removed.

#### Discussion

> **Note**: If the edge cannot be removed.

## Parameters

- `edge`: The edge to remove.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/removeedge(_:))*