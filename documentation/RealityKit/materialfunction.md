# MaterialFunction

**Framework**: RealityKit  
**Kind**: protocol

The abstract superclass for objects representing compute functions for RealityKit custom materials .

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
protocol MaterialFunction
```

#### Overview

This class is the parent of, and contains common properties and methods for [`CustomMaterial.GeometryModifier`](custommaterial/geometrymodifier.md) and [`CustomMaterial.SurfaceShader`](custommaterial/surfaceshader.md). Don’t create an instance of this superclass yourself.

## Topics

### Instance Properties
- [var constantValues: MTLFunctionConstantValues](materialfunction/constantvalues.md)
  The constant values to use when RealityKit creates your function. These correspond to constants defined in your metal code.
- [var library: any MTLLibrary](materialfunction/library.md)
  Metal Library containing the given function.
- [var name: String](materialfunction/name.md)
  Name of function found in library

## Relationships

### Conforming Types
- [CustomMaterial.GeometryModifier](custommaterial/geometrymodifier.md)
- [CustomMaterial.SurfaceShader](custommaterial/surfaceshader.md)

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
- [CustomMaterial.Program](custommaterial/program-swift.class.md)
  An object that represents the backing shader compilation required for custom materials.
- [CustomMaterial.Program.Descriptor](custommaterial/program-swift.class/descriptor-swift.struct.md)
  An object that specifies all parameters necessary to initialize `CustomMaterial` programs
- [enum CustomShaderStage](customshaderstage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/materialfunction)*