# definitions(function:inputs:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Returns all definitions that implement the given function with the specified input types, in order.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final func definitions(function: String, inputs inputTypes: [ShaderGraph.DataType]) -> [ShaderGraph.NodeDefinition]
```

**Other overloads**:

```swift
final func definitions(function: String, inputs inputTypes: ShaderGraph.DataType...) -> [ShaderGraph.NodeDefinition]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/nodelibrary/definitions(function:inputs:)-t4cy)*