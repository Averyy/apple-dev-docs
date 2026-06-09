# LowLevelMeshResource

**Framework**: RealityKit  
**Kind**: class

A container for vertex and index data in a custom format.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class LowLevelMeshResource
```

#### Overview

Use `LowLevelMeshResource` when you want to bring your own vertex format to the renderer or update your data frequently. Vertex and index data can be written directly on the CPU through span-based accessors, or on the GPU by writing to a `MTLBuffer` returned by `readVertices(at:commandBuffer:)` / `replaceVertices(at:commandBuffer:)`.

## Topics

### Describing the mesh layout
- [var descriptor: LowLevelMeshResource.Descriptor](lowlevelmeshresource/descriptor-swift.property.md)
  The descriptor used to create this mesh resource.
- [LowLevelMeshResource.Descriptor](lowlevelmeshresource/descriptor-swift.struct.md)
  An object that describes the data format and layout of the buffers in a low-level mesh.
- [LowLevelMeshResource.Layout](lowlevelmeshresource/layout.md)
  An object that describes a set of attributes that share a buffer index, offset, and stride.
- [LowLevelMeshResource.Attribute](lowlevelmeshresource/attribute.md)
  An object that determines how to store vertex attribute data in memory and map it to RealityKit custom shader attributes.
- [LowLevelMeshResource.VertexSemantic](lowlevelmeshresource/vertexsemantic.md)
  The intended usage of a vertex attribute.
### Accessing vertex data
- [func readVertices<R, E>(at: Int, (RawSpan) throws(E) -> R) throws(E) -> R](lowlevelmeshresource/readvertices(at:_:).md)
  Reads a vertex buffer synchronously on the CPU. The buffer is only valid for the lifetime of the callback.
- [func updateVertices<R, E>(at: Int, (inout MutableRawSpan) throws(E) -> R) throws(E) -> R](lowlevelmeshresource/updatevertices(at:_:).md)
  Updates a vertex buffer synchronously on the CPU. The buffer is only valid for the lifetime of the callback.
- [func replaceVertices<R, E>(at: Int, (inout MutableRawSpan) throws(E) -> R) throws(E) -> R](lowlevelmeshresource/replacevertices(at:_:).md)
  Replaces a vertex buffer synchronously on the CPU. The buffer’s contents are unspecified; you must populate the buffer with valid data.
- [func readVertices(at: Int, commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](lowlevelmeshresource/readvertices(at:commandbuffer:).md)
  Retrieves a Metal vertex buffer for GPU reading.
- [func replaceVertices(at: Int, commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](lowlevelmeshresource/replacevertices(at:commandbuffer:).md)
  Retrieves a Metal vertex buffer for GPU replacement. The buffer’s contents are in an uninitialized state. The renderer waits for the command buffer to complete before using the buffer for rendering.
### Accessing index data
- [func readIndices<R, E>((RawSpan) throws(E) -> R) throws(E) -> R](lowlevelmeshresource/readindices(_:).md)
  Reads the index buffer synchronously on the CPU. The buffer is only valid for the lifetime of the callback.
- [func updateIndices<R, E>((inout MutableRawSpan) throws(E) -> R) throws(E) -> R](lowlevelmeshresource/updateindices(_:).md)
  Updates the index buffer synchronously on the CPU. The buffer is only valid for the lifetime of the callback.
- [func replaceIndices<R, E>((inout MutableRawSpan) throws(E) -> R) throws(E) -> R](lowlevelmeshresource/replaceindices(_:).md)
  Replaces the index buffer synchronously on the CPU. The buffer’s contents are unspecified; you must populate the buffer with valid data.
- [func readIndices(commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](lowlevelmeshresource/readindices(commandbuffer:).md)
  Retrieves the Metal index buffer for GPU reading.
- [func replaceIndices(commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](lowlevelmeshresource/replaceindices(commandbuffer:).md)
  Retrieves a Metal index buffer for GPU replacement. The buffer’s contents are in an uninitialized state. The renderer waits for the command buffer to complete before using the buffer for rendering.

## See Also

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
  A compiled material composed of three independently-replaceable shader stages.
- [class LowLevelDeviceResource](lowleveldeviceresource.md)
  Encapsulates a GPU device resource created by the application. On visionOS, resources must be allocated in shared memory that can be used by the renderer process. Once a device resource is in use by the renderer, changing its contents is unsafe and undefined.
- [struct BoundingSphereBox](boundingspherebox.md)
  A combined bounding volume consisting of a bounding sphere and an optional axis-aligned bounding box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshresource)*