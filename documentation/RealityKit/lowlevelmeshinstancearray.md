# LowLevelMeshInstanceArray

**Framework**: RealityKit  
**Kind**: class

A fixed-capacity collection of mesh instances submitted to the renderer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class LowLevelMeshInstanceArray
```

#### Overview

Instances are placed by index via `setMeshInstance(_:index:)`. Create arrays using [`makeMeshInstanceArray(renderTargets:count:)`](lowlevelrendercontext/makemeshinstancearray(rendertargets:count:).md) and assign them to the renderer with [`setMeshInstances(_:at:)`](lowlevelrenderer/setmeshinstances(_:at:).md).

## Topics

### Setting mesh instances
- [func setMeshInstance(LowLevelMeshInstanceArray.Element, index: Int) throws(LowLevelRenderContextError)](lowlevelmeshinstancearray/setmeshinstance(_:index:).md)
  Assigns a mesh instance to the slot at the given index, or clears the slot if the instance is nil.
- [var count: Int](lowlevelmeshinstancearray/count.md)
  The number of instance slots in this array.
### Accessing render targets
- [var renderTargets: LowLevelRenderTarget.DescriptorSet](lowlevelmeshinstancearray/rendertargets.md)
  The set of render target descriptors this array is compatible with.
### Iterating over instances
- [LowLevelMeshInstanceArray.Iterator](lowlevelmeshinstancearray/iterator.md)
  An iterator over the mesh instance slots.
### Default Implementations
- [Collection Implementations](lowlevelmeshinstancearray/collection-implementations.md)
- [Sequence Implementations](lowlevelmeshinstancearray/sequence-implementations.md)

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [Escapable](../Swift/Escapable.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [class LowLevelMeshResource](lowlevelmeshresource.md)
  A container for vertex and index data in a custom format.
- [class LowLevelMeshPart](lowlevelmeshpart.md)
  An object that describes a range of primitives to draw from a mesh resource.
- [class LowLevelMeshInstance](lowlevelmeshinstance.md)
  A single drawable object pairing a mesh part with a compiled pipeline state, optional per-draw argument tables, a transform, and a sort category.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshinstancearray)*