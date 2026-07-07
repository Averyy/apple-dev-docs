# inputs

**Framework**: RealityKit  
**Kind**: property

The declared input ports of this graph.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final var inputs: [ShaderGraph.NodeDefinition.Input] { get }
```

#### Discussion

These ports are exposed as outputs on the [`arguments`](shadergraph/arguments.md) node. Initial values for each input must be supplied when creating a [`ShaderGraphMaterial.Program`](shadergraphmaterial/program-swift.struct.md), and can be updated at runtime via `ShaderGraphMaterial/setParameter(_:value:)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/inputs)*