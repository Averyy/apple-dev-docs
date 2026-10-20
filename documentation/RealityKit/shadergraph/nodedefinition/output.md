# ShaderGraph.NodeDefinition.Output

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
struct Output
```

## Topics

### Initializers
- [init(name: String, type: ShaderGraph.DataType, semanticType: ShaderGraph.NodeDefinition.SemanticType?, defaultValue: ShaderGraph.Value?)](./output/init%28name,type,semantictype,defaultvalue%29.md)
### Instance Properties
- [let defaultValue: ShaderGraph.Value?](./output/defaultvalue.md)
  The default value for this output, if any exists.
- [let name: String](./output/name.md)
  The unique name of this output in its definition.
- [let semanticType: ShaderGraph.NodeDefinition.SemanticType?](./output/semantictype.md)
  The original type of this output.
- [let type: ShaderGraph.DataType](./output/type.md)
  The type of the output.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/nodedefinition/output)*