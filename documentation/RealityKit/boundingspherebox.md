# BoundingSphereBox

**Framework**: RealityKit  
**Kind**: struct

A combined bounding volume consisting of a bounding sphere and an optional axis-aligned bounding box.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@frozen
struct BoundingSphereBox
```

#### Overview

`BoundingSphereBox` represents the culling bounds of a [`LowLevelMeshInstance`](lowlevelmeshinstance.md). When `halfExtents` is set, the renderer uses the tighter box bounds for culling; otherwise it falls back to the bounding sphere.

## Topics

### Creating a bounding volume
- [init(center: SIMD3<Float>, radius: Float)](boundingspherebox/init(center:radius:).md)
  Creates a bounding sphere with the given center and radius.
- [init(center: SIMD3<Float>, halfExtents: SIMD3<Float>)](boundingspherebox/init(center:halfextents:).md)
  Creates a bounding box with the given center and half-extents, with a circumscribed sphere.
- [init(center: SIMD3<Float>, fullExtents: SIMD3<Float>)](boundingspherebox/init(center:fullextents:).md)
  Creates a bounding box with the given center and full extents, with a circumscribed sphere.
- [init(boxMin: SIMD3<Float>, boxMax: SIMD3<Float>)](boundingspherebox/init(boxmin:boxmax:).md)
  Creates a bounding box from minimum and maximum corner positions, with a circumscribed sphere.
### Accessing the dimensions
- [var center: SIMD3<Float>](boundingspherebox/center.md)
  The center of the bounding volume in model space.
- [var halfExtents: SIMD3<Float>?](boundingspherebox/halfextents.md)
  The half-extents of the optional axis-aligned bounding box.
- [var fullExtents: SIMD3<Float>?](boundingspherebox/fullextents.md)
  The full extents of the optional axis-aligned bounding box.
### Instance Properties
- [var radius: Float](boundingspherebox/radius.md)
  The bounding sphere radius.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

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
- [class LowLevelMaterialResource](lowlevelmaterialresource.md)
  A compiled material composed of three independently-replaceable shader functions.
- [class LowLevelDeviceResource](lowleveldeviceresource.md)
  Encapsulates a GPU device resource created by the application. On visionOS, resources must be allocated in shared memory that can be used by the renderer process. Once a device resource is in use by the renderer, changing its contents is unsafe and undefined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/boundingspherebox)*