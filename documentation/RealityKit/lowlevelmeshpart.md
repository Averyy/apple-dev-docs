# LowLevelMeshPart

**Framework**: RealityKit  
**Kind**: class

An object that describes a range of primitives to draw from a mesh resource.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class LowLevelMeshPart
```

#### Overview

A mesh part selects a contiguous range of indices from the mesh’s index buffer and associates them with a primitive type, winding order, and bounding volume.

## Topics

### Configuring the geometry
- [var primitive: MTLPrimitiveType](lowlevelmeshpart/primitive.md)
  The geometric primitive to use when rendering this part.
- [var windingOrder: MTLWinding](lowlevelmeshpart/windingorder.md)
  The winding order of front-facing polygons.
- [func setIndexRange(indexOffset: Int, indexCount: Int) throws(LowLevelRenderContextError)](lowlevelmeshpart/setindexrange(indexoffset:indexcount:).md)
  Updates the first index and index count for this mesh part.
### Instance Properties
- [var bounds: BoundingSphereBox](lowlevelmeshpart/bounds.md)
  The bounding volume of this mesh part, in model space.
- [var indexCount: Int](lowlevelmeshpart/indexcount.md)
  The number of indices to use for this part.
- [var indexOffset: Int](lowlevelmeshpart/indexoffset.md)
  The byte offset of the first index.
- [var resource: LowLevelMeshResource](lowlevelmeshpart/resource.md)
  The mesh resource whose index and vertex buffers this part draws from.

## See Also

- [class LowLevelMeshResource](lowlevelmeshresource.md)
  A container for vertex and index data in a custom format.
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
- [class LowLevelMaterialResource](lowlevelmaterialresource.md)
  A compiled material composed of three independently-replaceable shader stages.
- [class LowLevelDeviceResource](lowleveldeviceresource.md)
  Encapsulates a GPU device resource created by the application. On visionOS, resources must be allocated in shared memory that can be used by the renderer process. Once a device resource is in use by the renderer, changing its contents is unsafe and undefined.
- [struct BoundingSphereBox](boundingspherebox.md)
  A combined bounding volume consisting of a bounding sphere and an optional axis-aligned bounding box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshpart)*