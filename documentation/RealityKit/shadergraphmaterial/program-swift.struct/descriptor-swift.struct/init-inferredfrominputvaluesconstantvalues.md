# init(inferredFrom:inputValues:constantValues:)

**Framework**: RealityKit  
**Kind**: init

Creates a descriptor by inferring configuration from a shader graph.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(inferredFrom graph: ShaderGraph, inputValues: [String : MaterialParameters.Value] = [:], constantValues: MTLFunctionConstantValues = .init()) throws
```

#### Discussion

Analyzes node connections to determine the appropriate lighting model and settings — for example, enabling clearcoat if the graph connects to the clearcoat output.

This initializer will not infer default values of inputs or function constants.

## See Also

- [init(shaderGraph: ShaderGraph, lightingModel: LightingModel, isColorDitheringEnabled: Bool, blendMode: MaterialParameterTypes.BlendMode?, inputValues: [String : MaterialParameters.Value], constantValues: MTLFunctionConstantValues)](shadergraphmaterial/program-swift.struct/descriptor-swift.struct/init(shadergraph:lightingmodel:iscolorditheringenabled:blendmode:inputvalues:constantvalues:).md)
  Creates a descriptor with explicit configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraphmaterial/program-swift.struct/descriptor-swift.struct/init(inferredfrom:inputvalues:constantvalues:))*