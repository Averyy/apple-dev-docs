# Buffers

**Framework**: Metal

Create and manage untyped data your app uses to exchange information with its shader functions.

#### Overview

Each [`MTLBuffer`](mtlbuffer.md) instance represents a general purpose, typeless memory allocation that your app uses to send and retrieve data from a shader. Your app decides how to use and interpret the buffer’s underlying bytes.

You create buffers from either an [`MTLDevice`](mtldevice.md) or [`MTLHeap`](mtlheap.md) instance.

Buffers inherently support the [`MTLResource`](mtlresource.md) protocol’s properties and methods, including [`storageMode`](mtlresource/storagemode.md), which controls how the GPU handles its memory (see [`Resource fundamentals`](resource-fundamentals.md)).

## Topics

### General purpose buffers
- [protocol MTLBuffer](mtlbuffer.md)
  A resource that stores data in a format defined by your app.
### Argument buffers
- [Improving CPU performance by using argument buffers](improving-cpu-performance-by-using-argument-buffers.md)
  Optimize your app’s performance by grouping your resources into argument buffers.
- [Managing groups of resources with argument buffers](managing-groups-of-resources-with-argument-buffers.md)
  Create argument buffers to organize related resources.
- [Tracking the resource residency of argument buffers](tracking-the-resource-residency-of-argument-buffers.md)
  Optimize resource performance within an argument buffer.
- [Indexing argument buffers](indexing-argument-buffers.md)
  Assign resource indices within an argument buffer.
- [Rendering terrain dynamically with argument buffers](rendering-terrain-dynamically-with-argument-buffers.md)
  Use argument buffers to render terrain in real time with a GPU-driven pipeline.
- [Encoding argument buffers on the GPU](encoding-argument-buffers-on-the-gpu.md)
  Use a compute pass to encode an argument buffer and access its arguments in a subsequent render pass.
- [Using argument buffers with resource heaps](using-argument-buffers-with-resource-heaps.md)
  Reduce CPU overhead by using arrays inside argument buffers and combining them with resource heaps.
- [class MTLArgumentDescriptor](mtlargumentdescriptor.md)
  A representation of an argument within an argument buffer.
- [protocol MTLArgumentEncoder](mtlargumentencoder.md)
  An interface you can use to encode argument data into an argument buffer.
- [let MTLAttributeStrideStatic: Int](mtlattributestridestatic.md)
### Model I/O interoperability
- [class MTKMesh](../MetalKit/MTKMesh.md)
  A container for the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [class MTKMeshBuffer](../MetalKit/MTKMeshBuffer.md)
  A buffer that backs the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [class MTKMeshBufferAllocator](../MetalKit/MTKMeshBufferAllocator.md)
  An interface for allocating a MetalKit buffer that backs the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [class MTKSubmesh](../MetalKit/MTKSubmesh.md)
  A container for the index data of a Model I/O submesh, suitable for use in a Metal app.
- [struct MTKModelError](../MetalKit/MTKModelError.md)
  Constants used to declare Model Errors.
- [func MTKMetalVertexFormatFromModelIO(MDLVertexFormat) -> MTLVertexFormat](../MetalKit/MTKMetalVertexFormatFromModelIO(_:).md)
  Returns a converted Metal vertex format.
- [func MTKModelIOVertexFormatFromMetal(MTLVertexFormat) -> MDLVertexFormat](../MetalKit/MTKModelIOVertexFormatFromMetal(_:).md)
  Returns a converted Model I/O vertex format.
- [func MTKMetalVertexDescriptorFromModelIO(MDLVertexDescriptor) -> MTLVertexDescriptor?](../MetalKit/MTKMetalVertexDescriptorFromModelIO(_:).md)
  Returns a partially converted Metal vertex descriptor.
- [func MTKModelIOVertexDescriptorFromMetal(MTLVertexDescriptor) -> MDLVertexDescriptor](../MetalKit/MTKModelIOVertexDescriptorFromMetal(_:).md)
  Returns a partially converted Model I/O vertex descriptor.

## See Also

- [Resource fundamentals](resource-fundamentals.md)
  Control the common attributes of all Metal memory resources, including buffers and textures, and how to configure their underlying memory.
- [Textures](textures.md)
  Create and manage typed data your app uses to exchange information with its shader functions.
- [Memory heaps](memory-heaps.md)
  Take control of your app’s GPU memory management by creating a large memory allocation for various buffers, textures, and other resources.
- [Resource loading](resource-loading.md)
  Load assets in your games and apps quickly by running a dedicated input/output queue alongside your GPU tasks.
- [Resource synchronization](resource-synchronization.md)
  Prevent multiple commands that can access the same resources simultaneously by coordinating those reads and writes with barriers, fences, or events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/buffers)*