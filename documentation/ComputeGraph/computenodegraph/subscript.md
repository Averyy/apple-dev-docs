# subscript(_:)

**Framework**: Compute Graph  
**Kind**: subscript

Accesses the node associated with the given key.

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
subscript(node: ComputeNodeGraph.NodeID) -> ComputeNodeGraph.Node? { get }
```

#### Return Value

The node if it exists, or `nil` if no node is associated with the key.

## Parameters

- `node`: The key identifying the node to retrieve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/subscript(_:))*