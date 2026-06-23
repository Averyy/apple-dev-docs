# outputs

**Framework**: RealityKit  
**Kind**: property

The declared output ports of this graph.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final var outputs: [ShaderGraph.NodeDefinition.Output] { get }
```

#### Discussion

These ports are exposed as inputs on the [`results`](shadergraph/results.md) node, and define what values the graph produces for the renderer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/outputs)*