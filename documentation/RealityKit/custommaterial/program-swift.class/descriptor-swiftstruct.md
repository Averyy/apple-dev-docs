# CustomMaterial.Program.Descriptor

**Framework**: RealityKit  
**Kind**: struct

An object that specifies all parameters necessary to initialize `CustomMaterial` programs

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)

## Declaration

```swift
struct Descriptor
```

## Topics

### Initializers
- [init()](custommaterial/program-swift.class/descriptor-swift.struct/init.md)
### Instance Properties
- [var blendMode: MaterialParameterTypes.BlendMode?](custommaterial/program-swift.class/descriptor-swift.struct/blendmode.md)
  Modes that describe how materials using the created `CustomMaterial.Program` will be blended with content behind them.
- [var lightingModel: CustomMaterial.LightingModel](custommaterial/program-swift.class/descriptor-swift.struct/lightingmodel.md)
  Modes that describe how materials using created `CustomMaterial.Program` will interact with light within the RealityKit scene.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ShaderGraphMaterial](shadergraphmaterial.md)
  Create dynamic materials without Metal.
- [ShaderGraphMaterial.FaceCulling](shadergraphmaterial/faceculling-swift.typealias.md)
  An alias for the cull mode object that’s appropriate for this material class.
- [ShaderGraphMaterial.TriangleFillMode](shadergraphmaterial/trianglefillmode-swift.typealias.md)
  An alias for the triangle fill mode object that’s appropriate for this material class.
- [Modifying RealityKit rendering using custom materials](modifying-realitykit-rendering-using-custom-materials.md)
  Write Metal shader functions to implement custom rendering effects.
- [struct CustomMaterial](custommaterial.md)
  A material that works with custom Metal shader functions.
- [CustomMaterial.SurfaceShader](custommaterial/surfaceshader.md)
  The custom material’s surface shader function.
- [CustomMaterial.GeometryModifier](custommaterial/geometrymodifier.md)
  The custom material’s optional shader function that can manipulate an entity’s vertex data.
- [protocol MaterialFunction](materialfunction.md)
  The abstract superclass for objects representing compute functions for RealityKit custom materials .
- [CustomMaterial.Program](custommaterial/program-swift.class.md)
  An object that represents the backing shader compilation required for custom materials.
- [enum CustomShaderStage](customshaderstage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/program-swift.class/descriptor-swift.struct)*