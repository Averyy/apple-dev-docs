# canAddNode(_:)

**Framework**: ComputeGraph  
**Kind**: method

Returns whether the given node can be added to the graph.

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