# outputs

**Framework**: RealityKit  
**Kind**: property

The declared output ports of this graph.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final var outputs: [ShaderGraph.NodeDefinition.Output] { get }
```

#### Discussion

These ports are exposed as inputs on the [`results`](shadergraph/results.md) node, and define what values the graph produces for the renderer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/outputs)*