# LowLevelMaterialResource

**Framework**: RealityKit  
**Kind**: class

A compiled material composed of three independently-replaceable shader stages.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class LowLevelMaterialResource
```

#### Overview

A `LowLevelMaterialResource` combines a `GeometryModifier` (vertex stage), a `SurfaceShader` (fragment stage), and a `LightingFunction` (lighting evaluation). Each stage can receive per-draw parameters through its own `LowLevelArgumentTable`, described by `argumentTableDescriptor`.

## Topics

### Describing the material
- [LowLevelMaterialResource.Descriptor](lowlevelmaterialresource/descriptor.md)
  The geometry modifier, surface shader, and lighting function for a material.
- [LowLevelMaterialResource.SimpleSurfaceDescriptor](lowlevelmaterialresource/simplesurfacedescriptor.md)
  The configuration for a built-in surface shader that applies a tint color, a texture, or both.
### Configuring the shaders
- [var surface: LowLevelMaterialResource.SurfaceShader](lowlevelmaterialresource/surface.md)
  The compiled fragment-stage surface shader.
- [LowLevelMaterialResource.SurfaceShader](lowlevelmaterialresource/surfaceshader.md)
  A compiled Metal function that implements the fragment surface shader stage.
- [var geometry: LowLevelMaterialResource.GeometryModifier](lowlevelmaterialresource/geometry.md)
  The compiled vertex-stage geometry modifier.
- [LowLevelMaterialResource.GeometryModifier](lowlevelmaterialresource/geometrymodifier.md)
  A compiled Metal function that implements the vertex geometry modifier stage.
- [LowLevelMaterialResource.LightingFunction](lowlevelmaterialresource/lightingfunction.md)
  A compiled function that evaluates lighting for a surface shader stage.
- [LowLevelMaterialResource.Function](lowlevelmaterialresource/function.md)
  A compiled shader stage function that can receive per-draw parameters via an argument table.
### Reading shader graph output
- [LowLevelMaterialResource.ShaderGraphOutput](lowlevelmaterialresource/shadergraphoutput.md)
  The compiled shader functions produced by a ShaderGraph compilation.
### Instance Properties
- [var lighting: LowLevelMaterialResource.LightingFunction](lowlevelmaterialresource/lighting.md)
  The compiled lighting evaluation function.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class LowLevelMeshResource](lowlevelmeshresource.md)
  A container for vertex and index data in a custom format.
- [class LowLevelMeshPart](lowlevelmeshpart.md)
  An object that describes a range of primitives to draw from a mesh resource.
- [class LowLevelMeshInstance](lowlevelmeshinstance.md)
  A single drawable object pairing a mesh part with a compiled pipeline state, optional per-draw argument tables, a transform, and a sort category.
- [class LowLevelMeshInstanceArray](lowlevelmeshinstancearray.md)
  A fixed-capacity collection of mesh instances submitted to the renderer.
- [class LowLevelInstanceTransformResource](lowlevelinstancetransformresource.md)
  A GPU-managed buffer that stores an array of per-instance transforms for GPU instancing.
- [class LowLevelBufferResource](lowlevelbufferresource.md)
  A GPU-managed buffer for arbitrary per-draw data such as uniforms and custom parameters.
- [struct LowLevelBufferSlice](lowlevelbufferslice.md)
  A reference to a sub-range of a buffer resource, used to bind a region of a buffer to an argument table slot.
- [class LowLevelTextureResource](lowleveltextureresource.md)
  A container for texture data in a custom format.
- [class LowLevelDeviceResource](lowleveldeviceresource.md)
  Encapsulates a GPU device resource created by the application. On visionOS, resources must be allocated in shared memory that can be used by the renderer process. Once a device resource is in use by the renderer, changing its contents is unsafe and undefined.
- [struct BoundingSphereBox](boundingspherebox.md)
  A combined bounding volume consisting of a bounding sphere and an optional axis-aligned bounding box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialresource)*