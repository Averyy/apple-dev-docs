# init(named:inputs:outputs:)

**Framework**: RealityKit  
**Kind**: init

Creates a shader graph with the given name, inputs, and outputs.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(named name: String, inputs: [ShaderGraph.NodeDefinition.Input], outputs: [ShaderGraph.NodeDefinition.Output]) throws
```

#### Discussion

> **Note**: If any input or output name is empty or duplicated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/init(named:inputs:outputs:))*