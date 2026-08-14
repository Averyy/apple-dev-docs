# ShaderGraphMaterial.Program.Descriptor

**Framework**: RealityKit  
**Kind**: struct

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Descriptor
```

## Topics

### Creating a descriptor
- [init(shaderGraph: ShaderGraph, lightingModel: LightingModel, isColorDitheringEnabled: Bool, blendMode: MaterialParameterTypes.BlendMode?, inputValues: [String : MaterialParameters.Value], constantValues: MTLFunctionConstantValues)](shadergraphmaterial/program-swift.struct/descriptor-swift.struct/init(shadergraph:lightingmodel:iscolorditheringenabled:blendmode:inputvalues:constantvalues:).md)
  Creates a descriptor with explicit configuration.
- [init(inferredFrom: ShaderGraph, inputValues: [String : MaterialParameters.Value], constantValues: MTLFunctionConstantValues) throws](shadergraphmaterial/program-swift.struct/descriptor-swift.struct/init(inferredfrom:inputvalues:constantvalues:).md)
  Creates a descriptor by inferring configuration from a shader graph.
### Specifying the shader graph
- [var shaderGraph: ShaderGraph](shadergraphmaterial/program-swift.struct/descriptor-swift.struct/shadergraph.md)
  The shader graph that describes the shading logic for this program.
- [var inputValues: [String : MaterialParameters.Value]](shadergraphmaterial/program-swift.struct/descriptor-swift.struct/inputvalues.md)
  Initial values for the inputs declared in `shaderNodeGraph`.
- [var constantValues: MTLFunctionConstantValues](shadergraphmaterial/program-swift.struct/descriptor-swift.struct/constantvalues.md)
  Values for the function constant inputs declared in `shaderNodeGraph`.
### Configuring rendering
- [var lightingModel: LightingModel](shadergraphmaterial/program-swift.struct/descriptor-swift.struct/lightingmodel.md)
  The lighting model to use when rendering this material.
- [var blendMode: MaterialParameterTypes.BlendMode?](shadergraphmaterial/program-swift.struct/descriptor-swift.struct/blendmode.md)
  How materials using this program blend with content behind them.
- [var isColorDitheringEnabled: Bool](shadergraphmaterial/program-swift.struct/descriptor-swift.struct/iscolorditheringenabled.md)
  Whether to dither color values before writing to the frame buffer.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)

## See Also

- [var descriptor: ShaderGraphMaterial.Program.Descriptor](shadergraphmaterial/program-swift.struct/descriptor-swift.property.md)
  The descriptor used to create this program.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraphmaterial/program-swift.struct/descriptor-swift.struct)*