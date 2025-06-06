# Buffers

**Framework**: Metal

Create and manage untyped data your app uses to exchange information with its shader functions.

#### Overview

Each [`MTLBuffer`](mtlbuffer.md) instance represents a general purpose, typeless memory allocation that your app uses to send and retrieve data from a shader. Your app decides how to use and interpret the buffer’s underlying bytes.

You create buffers from either an [`MTLDevice`](mtldevice.md) or [`MTLHeap`](mtlheap.md) instance.

Buffers inherently support the [`MTLResource`](mtlresource.md) protocol’s properties and methods, including [`storageMode`](mtlresource/storagemode.md), which controls how the GPU handles its memory (see [`Resource Fundamentals`](resource-fundamentals.md)).

## Topics

### General Purpose Buffers
- [protocol MTLBuffer](mtlbuffer.md)
  A resource that stores data in a format defined by your app.
### Argument Buffers
- [Improving CPU Performance by Using Argument Buffers](improving-cpu-performance-by-using-argument-buffers.md)
  Optimize your app’s performance by grouping your resources into argument buffers.
- [Managing groups of resources with argument buffers](managing-groups-of-resources-with-argument-buffers.md)
  Create argument buffers to organize related resources.
- [Tracking the Resource Residency of Argument Buffers](tracking-the-resource-residency-of-argument-buffers.md)
  Optimize resource performance within an argument buffer.
- [Indexing Argument Buffers](indexing-argument-buffers.md)
  Assign resource indices within an argument buffer.
- [Rendering Terrain Dynamically with Argument Buffers](rendering-terrain-dynamically-with-argument-buffers.md)
  Use argument buffers to render terrain in real time with a GPU-driven pipeline.
- [Encoding Argument Buffers on the GPU](encoding-argument-buffers-on-the-gpu.md)
  Use a compute pass to encode an argument buffer and access its arguments in a subsequent render pass.
- [Using Argument Buffers with Resource Heaps](using-argument-buffers-with-resource-heaps.md)
  Reduce CPU overhead by using arrays inside argument buffers and combining them with resource heaps.
- [class MTLArgumentDescriptor](mtlargumentdescriptor.md)
  A representation of an argument within an argument buffer.
- [protocol MTLArgumentEncoder](mtlargumentencoder.md)
  An object used to encode data into an argument buffer.
- [let MTLAttributeStrideStatic: Int](mtlattributestridestatic.md)
### Model I/O Interoperability
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
- [func MTKMetalVertexFormatFromModelIO(_ vertexFormat: MDLVertexFormat) -> MTLVertexFormat](../MetalKit/MTKMetalVertexFormatFromModelIO(_:).md)
  Returns a converted Metal vertex format.
- [func MTKModelIOVertexFormatFromMetal(_ vertexFormat: MTLVertexFormat) -> MDLVertexFormat](../MetalKit/MTKModelIOVertexFormatFromMetal(_:).md)
  Returns a converted Model I/O vertex format.
- [func MTKMetalVertexDescriptorFromModelIO(_ modelIODescriptor: MDLVertexDescriptor) -> MTLVertexDescriptor?](../MetalKit/MTKMetalVertexDescriptorFromModelIO(_:).md)
  Returns a partially converted Metal vertex descriptor.
- [func MTKModelIOVertexDescriptorFromMetal(_ metalDescriptor: MTLVertexDescriptor) -> MDLVertexDescriptor](../MetalKit/MTKModelIOVertexDescriptorFromMetal(_:).md)
  Returns a partially converted Model I/O vertex descriptor.

## See Also

- [Resource Fundamentals](resource-fundamentals.md)
  Learn the common attributes of all Metal memory resources, including buffers and textures, and how to manage the underlying memory.
- [Textures](textures.md)
  Create and manage typed data your app uses to exchange information with its shader functions.
- [Memory Heaps](memory-heaps.md)
  Take control of your app’s GPU memory management by creating a large memory allocation for various buffers, textures, and other resources.
- [Resource Loading](resource-loading.md)
  Load assets in your games and apps quickly by running a dedicated input/output queue alongside your GPU tasks.
- [Resource Synchronization](resource-synchronization.md)
  Coordinate the contents of data buffers, textures, and other resources that CPUs and GPUs share access to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/buffers)*