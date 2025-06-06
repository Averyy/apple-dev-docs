# CustomMaterial.SurfaceShader

**Framework**: RealityKit  
**Kind**: struct

The custom material’s surface shader function.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
struct SurfaceShader
```

#### Overview

Custom materials work together with a surface shader function to render entities. The [`CustomMaterial`](custommaterial.md) properties related to rendering, such as [`baseColor`](custommaterial/basecolor-swift.property.md) and [`normal`](custommaterial/normal-swift.property.md), are available in the surface shader function, but RealityKit doesn’t use them directly.

Instead, the material’s surface shader function allows you to calculate or specify all the material parameters that RealityKit uses to render your entity, such as [`baseColor`](custommaterial/basecolor-swift.property.md), [`normal`](custommaterial/normal-swift.property.md), and [`roughness`](custommaterial/roughness-swift.property.md). RealityKit’s fragment shader calls your surface shader function once for each pixel it renders.

Here’s a simple example of a surface shader that sets the entity’s base color:

```cpp
#include <metal_stdlib>
#include <RealityKit/RealityKit.h>

// Specify the current default namespace as metal so that it's not
// necessary to prefix Metal Standard Library symbols.
using namespace metal;

[[visible]] void mySurfaceShader(realitykit::surface_parameters params)
{
    // Set the base color
    params.surface().set_base_color(half3(1.0, 0.5, 0.5));
}
```

For more information on creating custom materials and writing shader functions, see [`Modifying RealityKit rendering using custom materials`](modifying-realitykit-rendering-using-custom-materials.md).

## Topics

### Creating surface shader objects
- [init(named: String, in: any MTLLibrary)](custommaterial/surfaceshader/init(named:in:).md)
  Creates a surface shader object from a named function in a Metal library.
### Accessing surface shader properties
- [var name: String](custommaterial/surfaceshader/name.md)
  The name of the surface shader function.
- [var library: any MTLLibrary](custommaterial/surfaceshader/library.md)
  The Metal library that contains this surface shader function.
### Initializers
- [init(named: String, in: any MTLLibrary, constantValues: MTLFunctionConstantValues)](custommaterial/surfaceshader/init(named:in:constantvalues:).md)
  Creates a surface shader with the specified function constant values.
### Default Implementations
- [Equatable Implementations](custommaterial/surfaceshader/equatable-implementations.md)
- [Hashable Implementations](custommaterial/surfaceshader/hashable-implementations.md)
- [MaterialFunction Implementations](custommaterial/surfaceshader/materialfunction-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MaterialFunction](materialfunction.md)
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
- [CustomMaterial.GeometryModifier](custommaterial/geometrymodifier.md)
  The custom material’s optional shader function that can manipulate an entity’s vertex data.
- [protocol MaterialFunction](materialfunction.md)
  The abstract superclass for objects representing compute functions for RealityKit custom materials .
- [CustomMaterial.Program](custommaterial/program-swift.class.md)
  An object that represents the backing shader compilation required for custom materials.
- [CustomMaterial.Program.Descriptor](custommaterial/program-swift.class/descriptor-swift.struct.md)
  An object that specifies all parameters necessary to initialize `CustomMaterial` programs
- [enum CustomShaderStage](customshaderstage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/surfaceshader)*