# results

**Framework**: RealityKit  
**Kind**: property

The virtual node representing this graph’s outputs.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final var results: ShaderGraph.Node { get }
```

#### Discussion

Connect edges from internal nodes to this node to route values out of the graph. Its input ports correspond to the [`outputs`](shadergraph/outputs.md) declared on this graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/results)*