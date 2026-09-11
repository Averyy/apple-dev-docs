# results

**Framework**: RealityKit  
**Kind**: property

The virtual node representing this graph’s outputs.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final var results: ShaderGraph.Node { get }
```

#### Discussion

Connect edges from internal nodes to this node to route values out of the graph. Its input ports correspond to the [`outputs`](shadergraph/outputs.md) declared on this graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/results)*