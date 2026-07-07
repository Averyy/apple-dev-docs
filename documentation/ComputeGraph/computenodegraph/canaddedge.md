# canAddEdge(_:)

**Framework**: Compute Graph  
**Kind**: method

Returns whether the given edge can be added to the graph.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro ?+

## Declaration

```swift
func canAddEdge(_ edge: ComputeNodeGraph.Edge) -> Bool
```

#### Return Value

`true` if calling [`addEdge(_:)`](computenodegraph/addedge(_:).md) with this edge would succeed.

#### Discussion

This is the non-throwing preflight check for [`addEdge(_:)`](computenodegraph/addedge(_:).md). Use it to validate a connection — for example, to highlight compatible ports during drag-and-drop — without modifying the graph.

## Parameters

- `edge`: The edge to test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/canaddedge(_:))*