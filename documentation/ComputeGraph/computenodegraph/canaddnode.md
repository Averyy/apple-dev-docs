# canAddNode(_:)

**Framework**: Compute Graph  
**Kind**: method

Returns whether the given node can be added to the graph.

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
func canAddNode(_ node: ComputeNodeGraph.Node) -> Bool
```

#### Return Value

`true` if calling [`addNode(_:)`](computenodegraph/addnode(_:).md) with this node would succeed.

#### Discussion

This is the non-throwing preflight check for [`addNode(_:)`](computenodegraph/addnode(_:).md). Use it to validate a node — for example, to gate UI affordances — without modifying the graph.

## Parameters

- `node`: The node to test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/canaddnode(_:))*