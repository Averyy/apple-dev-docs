# LowLevelBufferResource

**Framework**: RealityKit  
**Kind**: class

A GPU-managed buffer for arbitrary per-draw data such as uniforms and custom parameters.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class LowLevelBufferResource
```

#### Overview

Buffer contents can be read and written synchronously on the CPU via span-based accessors, or on the GPU by writing to a `MTLBuffer` returned by `replace(commandBuffer:)`.

## Topics

### Inspecting the descriptor
- [var descriptor: LowLevelBufferResource.Descriptor](lowlevelbufferresource/descriptor-swift.property.md)
  The descriptor used to create this buffer resource.
- [LowLevelBufferResource.Descriptor](lowlevelbufferresource/descriptor-swift.struct.md)
  The capacity and alignment requirements for a buffer resource.
### Reading buffer contents
- [func read(commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](lowlevelbufferresource/read(commandbuffer:).md)
  Retrieves the Metal buffer for GPU reading.
- [func read<R, E>((RawSpan) throws(E) -> R) throws(E) -> R](lowlevelbufferresource/read(_:).md)
  Reads the buffer synchronously on the CPU. The buffer is only valid for the lifetime of the callback.
### Replacing buffer contents
- [func replace(commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](lowlevelbufferresource/replace(commandbuffer:).md)
  Retrieves a Metal buffer for GPU replacement. The buffer’s contents are in an uninitialized state. The renderer waits for the command buffer to complete before using the buffer for rendering.
- [func replace<R, E>((inout MutableRawSpan) throws(E) -> R) throws(E) -> R](lowlevelbufferresource/replace(_:).md)
  Replaces the buffer synchronously on the CPU. The buffer’s contents are unspecified; you must populate the buffer with valid data.
### Instance Methods
- [func update<R, E>((inout MutableRawSpan) throws(E) -> R) throws(E) -> R](lowlevelbufferresource/update(_:).md)
  Updates the buffer synchronously on the CPU. The buffer is only valid for the lifetime of the callback.

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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelbufferresource)*