# ShaderGraph.NodeDefinition.Input

**Framework**: RealityKit  
**Kind**: struct

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Input
```

## Topics

### Initializers
- [init(name: String, type: ShaderGraph.DataType, isUniform: Bool, semanticType: ShaderGraph.NodeDefinition.SemanticType?, defaultValue: ShaderGraph.Value?)](shadergraph/nodedefinition/input/init(name:type:isuniform:semantictype:defaultvalue:).md)
### Instance Properties
- [let defaultValue: ShaderGraph.Value?](shadergraph/nodedefinition/input/defaultvalue.md)
  The default value for this input, if any exists.
- [let isUniform: Bool](shadergraph/nodedefinition/input/isuniform.md)
  Whether the value is uniform and must be set at compile-time
- [let name: String](shadergraph/nodedefinition/input/name.md)
  The unique name of this input in its definition.
- [let semanticType: ShaderGraph.NodeDefinition.SemanticType?](shadergraph/nodedefinition/input/semantictype.md)
  The original type of this input.
- [let type: ShaderGraph.DataType](shadergraph/nodedefinition/input/type.md)
  The type of the input.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/nodedefinition/input)*