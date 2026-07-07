# init(named:inputs:outputs:nodeLibrary:)

**Framework**: RealityKit  
**Kind**: init

Creates a shader graph with the given name, inputs, and outputs.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(named name: String, inputs: [ShaderGraph.NodeDefinition.Input], outputs: [ShaderGraph.NodeDefinition.Output], nodeLibrary: ShaderGraph.NodeLibrary) throws
```

## Parameters

- `name`: The name of the graph.
- `inputs`: The inputs of the graph.
- `outputs`: The outputs of the graph.
- `nodeLibrary`: The node library to use for this graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/init(named:inputs:outputs:nodelibrary:))*