# CustomMaterial.Program

**Framework**: RealityKit  
**Kind**: class

An object that represents the backing shader compilation required for custom materials.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+

## Declaration

```swift
final class Program
```

#### Overview

You can use this type to control when RealityKit compiles shaders, and to initialize `CustomMaterial` objects with more predicitable loading performance.

When initializing a `CustomMaterial` this way, a `Program` object is created first asynchronously, which is used to cache the material’s shader program so the `CustomMaterial` can be loaded immediately later.

For example:

```swift
// Initialize descriptor with desired properties
var descriptor = CustomMaterial.Descriptor()
descriptor.lightingModel = .unlit

// Create program object
let program = await CustomMaterial.Program(surfaceShader: surfaceShader,
                                           descriptor: descriptor)

// Create material (returns immediately)
let material = CustomMaterial(program: program)
```

## Topics

### Structures
- [CustomMaterial.Program.Descriptor](custommaterial/program-swift.class/descriptor-swift.struct.md)
  An object that specifies all parameters necessary to initialize `CustomMaterial` programs
### Initializers
- [init(surfaceShader: CustomMaterial.SurfaceShader, geometryModifier: CustomMaterial.GeometryModifier?, descriptor: CustomMaterial.Program.Descriptor) async throws](custommaterial/program-swift.class/init(surfaceshader:geometrymodifier:descriptor:).md)
### Instance Properties
- [let descriptor: CustomMaterial.Program.Descriptor](custommaterial/program-swift.class/descriptor-swift.property.md)
- [let geometryModifier: CustomMaterial.GeometryModifier?](custommaterial/program-swift.class/geometrymodifier.md)
- [let surfaceShader: CustomMaterial.SurfaceShader](custommaterial/program-swift.class/surfaceshader.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ShaderGraphMaterial](shadergraphmaterial.md)
  A material that comes from a shader graph in a Reality Composer Pro project, or a MaterialX shader.
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
- [CustomMaterial.Program.Descriptor](custommaterial/program-swift.class/descriptor-swift.struct.md)
  An object that specifies all parameters necessary to initialize `CustomMaterial` programs
- [enum CustomShaderStage](customshaderstage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/program-swift.class)*