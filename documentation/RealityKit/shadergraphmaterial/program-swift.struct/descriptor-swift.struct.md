# ShaderGraphMaterial.Program.Descriptor

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Descriptor
```

## Topics

### Creating a descriptor
- [init(shaderGraph: ShaderGraph, lightingModel: LightingModel, isColorDitheringEnabled: Bool, blendMode: MaterialParameterTypes.BlendMode?, inputValues: [String : MaterialParameters.Value], constantValues: MTLFunctionConstantValues)](./descriptor-swift.struct/init%28shadergraph,lightingmodel,iscolorditheringenabled,blendmode,inputvalues,constantvalues%29.md)
  Creates a descriptor with explicit configuration.
- [init(inferredFrom: ShaderGraph, inputValues: [String : MaterialParameters.Value], constantValues: MTLFunctionConstantValues) throws](./descriptor-swift.struct/init%28inferredfrom,inputvalues,constantvalues%29.md)
  Creates a descriptor by inferring configuration from a shader graph.
### Specifying the shader graph
- [var shaderGraph: ShaderGraph](./descriptor-swift.struct/shadergraph.md)
  The shader graph that describes the shading logic for this program.
- [var inputValues: [String : MaterialParameters.Value]](./descriptor-swift.struct/inputvalues.md)
  Initial values for the inputs declared in `shaderNodeGraph`.
- [var constantValues: MTLFunctionConstantValues](./descriptor-swift.struct/constantvalues.md)
  Values for the function constant inputs declared in `shaderNodeGraph`.
### Configuring rendering
- [var lightingModel: LightingModel](./descriptor-swift.struct/lightingmodel.md)
  The lighting model to use when rendering this material.
- [var blendMode: MaterialParameterTypes.BlendMode?](./descriptor-swift.struct/blendmode.md)
  How materials using this program blend with content behind them.
- [var isColorDitheringEnabled: Bool](./descriptor-swift.struct/iscolorditheringenabled.md)
  Whether to dither color values before writing to the frame buffer.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)

## See Also

### Accessing the descriptor
- [var descriptor: ShaderGraphMaterial.Program.Descriptor](./descriptor-swift.property.md)
  The descriptor used to create this program.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraphmaterial/program-swift.struct/descriptor-swift.struct)*