# LowLevelBufferSlice

**Framework**: RealityKit  
**Kind**: struct

A reference to a sub-range of a buffer resource, used to bind a region of a buffer to an argument table slot.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct LowLevelBufferSlice
```

## Topics

### Creating a buffer slice
- [init(buffer: LowLevelBufferResource, offset: Int, size: Int) throws(LowLevelRenderContextError)](lowlevelbufferslice/init(buffer:offset:size:).md)
  Creates a slice referencing a sub-range of the given buffer.
### Accessing the buffer region
- [var buffer: LowLevelBufferResource](lowlevelbufferslice/buffer.md)
  The buffer this slice references.
- [var size: Int](lowlevelbufferslice/size.md)
  The size of this slice, in bytes.
### Adjusting the offset
- [func setOffset(Int) throws(LowLevelRenderContextError)](lowlevelbufferslice/setoffset(_:).md)
  Updates the byte offset of this slice.
### Instance Properties
- [var offset: Int](lowlevelbufferslice/offset.md)
  The byte offset into `buffer` at which this slice begins.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

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
- [class LowLevelTextureResource](lowleveltextureresource.md)
  A container for texture data in a custom format.
- [class LowLevelMaterialResource](lowlevelmaterialresource.md)
  A compiled material composed of three independently-replaceable shader stages.
- [class LowLevelDeviceResource](lowleveldeviceresource.md)
  Encapsulates a GPU device resource created by the application. On visionOS, resources must be allocated in shared memory that can be used by the renderer process. Once a device resource is in use by the renderer, changing its contents is unsafe and undefined.
- [struct BoundingSphereBox](boundingspherebox.md)
  A combined bounding volume consisting of a bounding sphere and an optional axis-aligned bounding box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelbufferslice)*