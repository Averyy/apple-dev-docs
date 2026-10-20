# ShaderGraph.NodeDefinition.Input

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Input
```

## Topics

### Initializers
- [init(name: String, type: ShaderGraph.DataType, isUniform: Bool, semanticType: ShaderGraph.NodeDefinition.SemanticType?, defaultValue: ShaderGraph.Value?)](./input/init%28name,type,isuniform,semantictype,defaultvalue%29.md)
### Instance Properties
- [let defaultValue: ShaderGraph.Value?](./input/defaultvalue.md)
  The default value for this input, if any exists.
- [let isUniform: Bool](./input/isuniform.md)
  Whether the value is uniform and must be set at compile-time
- [let name: String](./input/name.md)
  The unique name of this input in its definition.
- [let semanticType: ShaderGraph.NodeDefinition.SemanticType?](./input/semantictype.md)
  The original type of this input.
- [let type: ShaderGraph.DataType](./input/type.md)
  The type of the input.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/nodedefinition/input)*