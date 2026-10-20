# init(named:inputs:outputs:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a shader graph with the given name, inputs, and outputs.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

> **Deprecated**: Create a `ShaderGraph` instance with a NodeLibrary value instead.

## Declaration

```swift
init(named name: String, inputs: [ShaderGraph.NodeDefinition.Input], outputs: [ShaderGraph.NodeDefinition.Output]) throws
```

#### Discussion

> **Throws**: If any input or output name is empty or duplicated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/init(named:inputs:outputs:))*