# LowLevelMeshInstance

**Framework**: RealityKit  
**Kind**: class

A single drawable object pairing a mesh part with a compiled pipeline state, optional per-draw argument tables, a transform, and a sort category.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class LowLevelMeshInstance
```

#### Overview

Transform, bounds, and sort category can be updated after creation; the renderer picks up changes automatically before the next `render(using:_:)` call.

To draw multiple copies of the mesh in a single draw call, assign a [`LowLevelInstanceTransformResource`](lowlevelinstancetransformresource.md) via [`setInstanceTransforms(_:)`](lowlevelmeshinstance/setinstancetransforms(_:).md).

## Topics

### Configuring the geometry and pipeline
- [var meshPart: LowLevelMeshPart](lowlevelmeshinstance/meshpart.md)
  The mesh part this instance draws.
- [var pipeline: LowLevelRenderPipelineState](lowlevelmeshinstance/pipeline.md)
  The compiled pipeline state used to render this instance.
### Positioning instances
- [var instanceTransforms: LowLevelInstanceTransformResource?](lowlevelmeshinstance/instancetransforms.md)
  The transform buffer for GPU instancing, or `nil` for single-instance rendering.
- [func setInstanceTransforms(LowLevelInstanceTransformResource?) throws(LowLevelRenderContextError)](lowlevelmeshinstance/setinstancetransforms(_:).md)
  Assigns or clears the transform buffer for GPU instancing.
### Providing shader arguments
- [var surfaceArguments: LowLevelArgumentTable?](lowlevelmeshinstance/surfacearguments.md)
  The optional argument table for the surface shader stage.
- [var geometryArguments: LowLevelArgumentTable?](lowlevelmeshinstance/geometryarguments.md)
  The optional argument table for the geometry modifier stage.
- [var lightingArguments: LowLevelArgumentTable?](lowlevelmeshinstance/lightingarguments.md)
  The optional argument table for the lighting function stage.
### Sorting instances
- [var sortCategory: LowLevelMeshInstance.SortCategory](lowlevelmeshinstance/sortcategory-swift.property.md)
  The sort category of this mesh instance.
- [LowLevelMeshInstance.SortCategory](lowlevelmeshinstance/sortcategory-swift.enum.md)
  The sort category of this mesh instance.
### Instance Properties
- [var bounds: BoundingSphereBox?](lowlevelmeshinstance/bounds.md)
  The bounds of this mesh instance, in model space, or `nil` to derive bounds from the mesh part.
- [var transform: simd_float4x4](lowlevelmeshinstance/transform.md)
  The local-to-world transform applied to this mesh instance.
- [var triangleFillMode: MTLTriangleFillMode](lowlevelmeshinstance/trianglefillmode.md)

## See Also

- [class LowLevelMeshResource](lowlevelmeshresource.md)
  A container for vertex and index data in a custom format.
- [class LowLevelMeshPart](lowlevelmeshpart.md)
  An object that describes a range of primitives to draw from a mesh resource.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshinstance)*