# init(shaderGraph:lightingModel:isColorDitheringEnabled:blendMode:inputValues:constantValues:)

**Framework**: RealityKit  
**Kind**: init

Creates a descriptor with explicit configuration.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(shaderGraph: ShaderGraph, lightingModel: LightingModel, isColorDitheringEnabled: Bool = false, blendMode: MaterialParameterTypes.BlendMode? = nil, inputValues: [String : MaterialParameters.Value] = [:], constantValues: MTLFunctionConstantValues = .init())
```

## See Also

- [init(inferredFrom: ShaderGraph, inputValues: [String : MaterialParameters.Value], constantValues: MTLFunctionConstantValues) throws](shadergraphmaterial/program-swift.struct/descriptor-swift.struct/init(inferredfrom:inputvalues:constantvalues:).md)
  Creates a descriptor by inferring configuration from a shader graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraphmaterial/program-swift.struct/descriptor-swift.struct/init(shadergraph:lightingmodel:iscolorditheringenabled:blendmode:inputvalues:constantvalues:))*