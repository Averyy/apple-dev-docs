# CustomMaterial.GeometryModifier

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The custom material’s optional shader function that can manipulate an entity’s vertex data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+

## Declaration

```swift
struct GeometryModifier
```

#### Overview

A geometry modifier is an optional Metal function that you can use with custom materials. Use a geometry modifier to change vertex data, such as vertex position, color, or texture coordinates. For example, offsetting a vertex’s position changes the size and shape of the entity for rendering only. If your custom material has a geometry modifier, RealityKit’s custom material vertex shader calls it once for each vertex in the entity. Changes that your geometry modifier makes are transient and don’t affect the vertex positions of the original [`ModelEntity`](../modelentity.md).

Here’s a simple example of a geometry modifier that offsets the vertex positions along the z-axis based on the elapsed time:

```cpp
#include <metal_stdlib>
#include <RealityKit/RealityKit.h>
using namespace metal;

[[visible]] void myGeometryModifier(realitykit::geometry_parameters
params) {
    float3 zOffset = float3(0.0, 0.0, params.uniforms().time() / 50.0);
    params.geometry().set_world_position_offset(zOffset);
}
```

For more information on creating custom materials and writing shader functions, see [Modifying RealityKit rendering using custom materials](../modifying-realitykit-rendering-using-custom-materials.md).

## Topics

### Creating geometry modifier objects
- [init(named: String, in: any MTLLibrary)](./geometrymodifier/init%28named,in%29.md)
  Creates a geometry modifier object from a named function in a Metal library.
### Accessing geometry modifier properties
- [var name: String](./geometrymodifier/name.md)
  The name of the geometry modifier function.
- [var library: any MTLLibrary](./geometrymodifier/library.md)
  The Metal library that contains this surface shader function.
### Initializers
- [init(named: String, in: any MTLLibrary, constantValues: MTLFunctionConstantValues)](./geometrymodifier/init%28named,in,constantvalues%29.md)
  Creates a geometry modifier with the specified function constant values.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [MaterialFunction](../materialfunction.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Shaders
- [Implementing adjustable material](../../visionOS/implementing-adjustable-material-in-visionos.md)
  Update the adjustable parameters of a 3D model in visionOS.
- [Displaying a stereoscopic image](../../visionOS/displaying-a-stereoscopic-image-in-visionos.md)
  Build a stereoscopic image by applying textures to the left and right eye in a shader graph material.
- [struct ShaderGraphMaterial](../shadergraphmaterial.md)
  A material that comes from a shader graph in a Reality Composer Pro project, or a MaterialX shader.
- [ShaderGraphMaterial.FaceCulling](../shadergraphmaterial/faceculling-swift.typealias.md)
  An alias for the cull mode object that’s appropriate for this material class.
- [ShaderGraphMaterial.TriangleFillMode](../shadergraphmaterial/trianglefillmode-swift.typealias.md)
  An alias for the triangle fill mode object that’s appropriate for this material class.
- [Modifying RealityKit rendering using custom materials](../modifying-realitykit-rendering-using-custom-materials.md)
  Write Metal shader functions to implement custom rendering effects.
- [struct CustomMaterial](../custommaterial.md)
  A material that works with custom Metal shader functions.
- [CustomMaterial.SurfaceShader](./surfaceshader.md)
  The custom material’s surface shader function.
- [protocol MaterialFunction](../materialfunction.md)
  The abstract superclass for objects representing compute functions for RealityKit custom materials .
- [CustomMaterial.Program](./program-swift.class.md)
  An object that represents the backing shader compilation required for custom materials.
- [CustomMaterial.Program.Descriptor](./program-swift.class/descriptor-swift.struct.md)
  An object that specifies all parameters necessary to initialize `CustomMaterial` programs
- [enum CustomShaderStage](../customshaderstage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/geometrymodifier)*