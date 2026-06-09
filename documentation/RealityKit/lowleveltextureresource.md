# LowLevelTextureResource

**Framework**: RealityKit  
**Kind**: class

A container for texture data in a custom format.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class LowLevelTextureResource
```

#### Overview

Use `LowLevelTextureResource` when you want to bring your own texture data to the renderer or update your data frequently. Textures are updated on the GPU by writing to a `MTLTexture` returned by `replace(commandBuffer:)`. The descriptor is analogous to `MTLTextureDescriptor`.

## Topics

### Accessing the descriptor
- [var descriptor: LowLevelTextureResource.Descriptor](lowleveltextureresource/descriptor-swift.property.md)
  The descriptor used to create this texture resource.
- [LowLevelTextureResource.Descriptor](lowleveltextureresource/descriptor-swift.struct.md)
  The configuration for a new low-level texture resource.
### Reading and writing texture data
- [func read(commandBuffer: (any MTLCommandBuffer)?) -> any MTLTexture](lowleveltextureresource/read(commandbuffer:).md)
  Retrieves the Metal texture for GPU reading.
- [func replace(commandBuffer: (any MTLCommandBuffer)?) -> any MTLTexture](lowleveltextureresource/replace(commandbuffer:).md)
  Retrieves a Metal texture that shaders can write to on the GPU. The texture’s contents are in an uninitialized state. The renderer waits for the command buffer to complete before using the texture for rendering.

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
- [class LowLevelMaterialResource](lowlevelmaterialresource.md)
  A compiled material composed of three independently-replaceable shader stages.
- [class LowLevelDeviceResource](lowleveldeviceresource.md)
  Encapsulates a GPU device resource created by the application. On visionOS, resources must be allocated in shared memory that can be used by the renderer process. Once a device resource is in use by the renderer, changing its contents is unsafe and undefined.
- [struct BoundingSphereBox](boundingspherebox.md)
  A combined bounding volume consisting of a bounding sphere and an optional axis-aligned bounding box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveltextureresource)*