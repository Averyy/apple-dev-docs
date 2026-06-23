# arguments

**Framework**: RealityKit  
**Kind**: property

The virtual node representing this graph’s inputs.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final var arguments: ShaderGraph.Node { get }
```

#### Discussion

Connect edges from this node to internal nodes to route graph-level input values into the graph. Its output ports correspond to the [`inputs`](shadergraph/inputs.md) declared on this graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/arguments)*