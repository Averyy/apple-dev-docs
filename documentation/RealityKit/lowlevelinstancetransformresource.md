# LowLevelInstanceTransformResource

**Framework**: RealityKit  
**Kind**: class

A GPU-managed buffer that stores an array of per-instance transforms for GPU instancing.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class LowLevelInstanceTransformResource
```

#### Overview

Assign a `LowLevelInstanceTransformResource` to a [`LowLevelMeshInstance`](lowlevelmeshinstance.md) via [`setInstanceTransforms(_:)`](lowlevelmeshinstance/setinstancetransforms(_:).md) to issue a single instanced draw call that renders multiple copies of the mesh. Each entry in the buffer is a `float4x4` model-to-local transform. The renderer computes the final world transform for each instance as `meshInstance.transform * instanceTransforms[i]`.

Create a `LowLevelInstanceTransformResource` using [`makeInstanceTransformResource(instanceCapacity:)`](lowlevelrendercontext/makeinstancetransformresource(instancecapacity:).md).

## Topics

### Inspecting instance counts
- [var instanceCount: Int](lowlevelinstancetransformresource/instancecount.md)
  The number of active instances to draw.
- [var instanceCapacity: Int](lowlevelinstancetransformresource/instancecapacity.md)
  The maximum number of instances the buffer holds.
### Reading transform data
- [func read<R, E>((consuming Span<float4x4>) throws(E) -> R) throws(E) -> R](lowlevelinstancetransformresource/read(_:).md)
  Provides read-only CPU access to the transform data.
- [func read(commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](lowlevelinstancetransformresource/read(commandbuffer:).md)
  Returns a `MTLBuffer` for GPU-side read access to the transform data.
### Replacing transform data
- [func replace<R, E>((inout MutableSpan<float4x4>) throws(E) -> R) throws(E) -> R](lowlevelinstancetransformresource/replace(_:).md)
  Provides full read-write CPU access, replacing all transform data.
- [func replace(commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](lowlevelinstancetransformresource/replace(commandbuffer:).md)
  Returns a `MTLBuffer` for GPU-side write access to the transform data.
### Instance Methods
- [func update<R, E>((inout MutableSpan<float4x4>) throws(E) -> R) throws(E) -> R](lowlevelinstancetransformresource/update(_:).md)
  Provides partial read-write CPU access to the transform data.

## See Also

- [class LowLevelMeshResource](lowlevelmeshresource.md)
  A container for vertex and index data in a custom format.
- [class LowLevelMeshPart](lowlevelmeshpart.md)
  An object that describes a range of primitives to draw from a mesh resource.
- [class LowLevelMeshInstance](lowlevelmeshinstance.md)
  A single drawable object pairing a mesh part with a compiled pipeline state, optional per-draw argument tables, a transform, and a sort category.
- [class LowLevelMeshInstanceArray](lowlevelmeshinstancearray.md)
  A fixed-capacity collection of mesh instances submitted to the renderer.
- [class LowLevelBufferResource](lowlevelbufferresource.md)
  A GPU-managed buffer for arbitrary per-draw data such as uniforms and custom parameters.
- [struct LowLevelBufferSlice](lowlevelbufferslice.md)
  A reference to a sub-range of a buffer resource, used to bind a region of a buffer to an argument table slot.
- [class LowLevelTextureResource](lowleveltextureresource.md)
  A container for texture data in a custom format.
- [class LowLevelMaterialResource](lowlevelmaterialresource.md)
  A compiled material composed of three independently-replaceable shader stages.
- [class LowLevelDeviceResource](lowleveldeviceresource.md)
  Encapsulates a GPU device resource created by the application. On visionOS, resources must be allocated in shared memory that can be used by the renderer process. Once a device resource is in use by the renderer, changing its contents is unsafe and undefined.
- [struct BoundingSphereBox](boundingspherebox.md)
  A combined bounding volume consisting of a bounding sphere and an optional axis-aligned bounding box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelinstancetransformresource)*