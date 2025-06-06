# Creating Sparse Heaps and Sparse Textures

**Framework**: Metal

Allocate memory for sparse textures by creating a sparse heap.

#### Overview

 are [`MTLHeap`](mtlheap.md) objects that create sparse textures and provide memory for them. Unlike with a standard heap, you use a sparse heap only to create sparse textures and allocate storage for texture data. You allocate memory when you create the heap, and later, as needed, map or unmap portions of the heap’s memory to textures. Memory is mapped in larger chunks called . The size of sparse tiles (in bytes) is determined by the device object.

##### Create a Sparse Heap

Create a [`MTLHeapDescriptor`](mtlheapdescriptor.md) object and set its type to [`MTLHeapType.sparse`](mtlheaptype/sparse.md). You must allocate sparse heaps with the [`MTLStorageMode.private`](mtlstoragemode/private.md) storage mode. Specify the heap’s size as a multiple of the sparse tile size. To get the tile size, read the [`sparseTileSizeInBytes`](mtldevice/sparsetilesizeinbytes.md) property on the [`MTLDevice`](mtldevice.md) object that you’re using to create the heap.

The code below creates a new sparse heap, rounding the heap size up to the tile size.

Specify a heap size that’s appropriate for your app, based on how many textures you’ve, how large those textures are, and your image-quality goals. You may need to experiment to determine the best size. The heap should be large enough that your app doesn’t need to unmap sparse tiles frequently and doesn’t suffer from image-quality problems. Unless you need finer-grained control of how different collections of textures are allocated in memory, allocate a single sparse heap and use it to manage all of your app’s texture memory.

##### Create a Sparse Texture

All textures that you create on a sparse heap are sparse textures. When you create textures on heaps, you must use the same storage mode as you used to create the sparse heap, as shown in the code below:

When you create a sparse texture, no memory is allocated for it. It can’t store any pixel data until you map sparse tiles on the heap to regions inside the texture. For more information about mapping and unmapping sparse tiles, see [`Assigning Memory to Sparse Textures`](assigning-memory-to-sparse-textures.md). For more information about how sparse textures behave when you access them, see [`Reading and Writing to Sparse Textures`](reading-and-writing-to-sparse-textures.md).

## See Also

- [Managing Sparse Texture Memory](managing-sparse-texture-memory.md)
  Take direct control of memory allocation for texture data by using sparse textures.
- [Converting Between Pixel Regions and Sparse Tile Regions](converting-between-pixel-regions-and-sparse-tile-regions.md)
  Learn how a sparse texture’s contents are organized in memory.
- [Assigning Memory to Sparse Textures](assigning-memory-to-sparse-textures.md)
  Use a resource state encoder to allocate and deallocate sparse tiles for a sparse texture.
- [Reading and Writing to Sparse Textures](reading-and-writing-to-sparse-textures.md)
  Decide how to handle access to unmapped texture regions.
- [Estimating How Often a Texture Region Is Accessed](estimating-how-often-a-texture-region-is-accessed.md)
  Use texture access patterns to determine when you need to map a texture region.
- [class MTLResourceStatePassDescriptor](mtlresourcestatepassdescriptor.md)
  A configuration for a resource state pass, used to create a resource state command encoder.
- [class MTLResourceStatePassSampleBufferAttachmentDescriptor](mtlresourcestatepasssamplebufferattachmentdescriptor.md)
  A description of where to store GPU counter information at the start and end of a resource state pass.
- [class MTLResourceStatePassSampleBufferAttachmentDescriptorArray](mtlresourcestatepasssamplebufferattachmentdescriptorarray.md)
  An array of sample buffer attachments for a resource state pass.
- [protocol MTLResourceStateCommandEncoder](mtlresourcestatecommandencoder.md)
  An encoder that encodes commands that modify resource configurations.
- [struct MTLMapIndirectArguments](mtlmapindirectarguments.md)
  The data layout for mapping sparse texture regions when using indirect commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/creating-sparse-heaps-and-sparse-textures)*