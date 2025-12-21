# Estimating how often a texture region is accessed

**Framework**: Metal

Use texture access patterns to determine when you need to map a texture region.

#### Overview

When you use sparse textures, you need to decide when to map or unmap texture regions. For example, one option is to map entire mipmaps, using existing techniques for determining which mipmaps are accessed. (For more information, see [`Dynamically adjusting texture level of detail`](dynamically-adjusting-texture-level-of-detail.md)). You may also want to go further, and only map subregions within individual mipmaps. To help you do that, Metal provides a mechanism to estimate how often you access each region. When you detect a sufficient number of requests to a given region, you can map a sparse tile to it.

When the GPU attempts to sample a pixel in texture memory:

1. If the pixel is already in the GPU’s memory caches, it returns the cached pixel to your shader. Otherwise, it executes the remaining steps.
2. The GPU increments its access counters and requests pixel data from the texture.
3. If the sparse tile is mapped, after the request completes, the GPU puts the pixel data into the cache and returns it to your shader.
4. If the sparse tile is unmapped, the GPU loads zeroed data into the cache and returns it to your shader.

The texture access count estimation comes from the number of cache misses, and isn’t an exact count of the number of memory operations to a specific region. If your app accesses the same regions frequently, because they’re more likely to be in the cache, the counts you receive from Metal might be smaller than the number of memory operations you actually made.

To take advantage of spatial locality, memory subsystems retrieve memory in larger chunks, called . A cache line is usually large enough to store multiple pixels of data, but the exact number of pixels depends on the pixel format.

To normalize the access counts, Metal increments the count as if you accessed all of the pixels in the cache line. For example, if a cache line is `64` bytes and a pixel is `4` bytes, the counter value increases by `16` `(64/4)`. This abstraction means you can focus on the number of memory operations recorded, without needing to know the details of the underlying memory architecture.

Determine your own heuristics to decide how many pixel memory operations is sufficient to start mapping a sparse tile for that region.

##### Request the Estimated Texture Access Counts

To get the current access counts for a sparse texture, create a blit command encoder and encode commands to copy the GPU’s internal counters to an [`MTLBuffer`](mtlbuffer.md) instance. The following example code takes a tile region in the texture’s top-level mipmap, creates an [`MTLBuffer`](mtlbuffer.md) instance large enough to accommodate all of the region’s tiles, and encodes a command to copy the counters.

The counters are organized as a 3D array of [`uint32_t`](https://developer.apple.com/documentation/kernel/uint32_t) values, stored in row-major order. You tell the GPU whether to reset the access counters.

If you want information about more than one mipmap in the same texture or information about multiple textures, encode a separate command for each mipmap/texture combination. Don’t allocate a buffer for each request; allocate larger [`MTLBuffer`](mtlbuffer.md) instances and specify offsets within those buffers for each request.

## See Also

- [Managing sparse texture memory](managing-sparse-texture-memory.md)
  Take direct control of memory allocation for texture data by using sparse textures.
- [Creating sparse heaps and sparse textures](creating-sparse-heaps-and-sparse-textures.md)
  Allocate memory for sparse textures by creating a sparse heap.
- [Converting between pixel regions and sparse tile regions](converting-between-pixel-regions-and-sparse-tile-regions.md)
  Learn how a sparse texture’s contents are organized in memory.
- [Assigning memory to sparse textures](assigning-memory-to-sparse-textures.md)
  Use a resource state encoder to allocate and deallocate sparse tiles for a sparse texture.
- [Reading and writing to sparse textures](reading-and-writing-to-sparse-textures.md)
  Decide how to handle access to unmapped texture regions.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/estimating-how-often-a-texture-region-is-accessed)*