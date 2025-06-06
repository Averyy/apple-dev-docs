# CustomMaterial.Program.Descriptor

**Framework**: RealityKit  
**Kind**: struct

An object that specifies all parameters necessary to initialize `CustomMaterial` programs

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
struct Descriptor
```

## Topics

### Operators
- [static func == (CustomMaterial.Program.Descriptor, CustomMaterial.Program.Descriptor) -> Bool](custommaterial/program-swift.class/descriptor-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init()](custommaterial/program-swift.class/descriptor-swift.struct/init.md)
### Instance Properties
- [var blendMode: MaterialParameterTypes.BlendMode?](custommaterial/program-swift.class/descriptor-swift.struct/blendmode.md)
  Modes that describe how materials using the created `CustomMaterial.Program` will be blended with content behind them.
- [var hashValue: Int](custommaterial/program-swift.class/descriptor-swift.struct/hashvalue.md)
  The hash value.
- [var lightingModel: CustomMaterial.LightingModel](custommaterial/program-swift.class/descriptor-swift.struct/lightingmodel.md)
  Modes that describe how materials using created `CustomMaterial.Program` will interact with light within the RealityKit scene.
### Instance Methods
- [func hash(into: inout Hasher)](custommaterial/program-swift.class/descriptor-swift.struct/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](custommaterial/program-swift.class/descriptor-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct ShaderGraphMaterial](shadergraphmaterial.md)
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