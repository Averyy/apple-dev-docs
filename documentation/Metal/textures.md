# Textures

**Framework**: Metal

Create and manage typed data your app uses to exchange information with its shader functions.

#### Overview

[`MTLTexture`](mtltexture.md) instances can serve as input and output resources to shader functions, as well as render pass destinations, or . Unlike buffers, textures define the underlying pixel type and structure. Textures can:

- Store 1-, 2-, or 3-dimensional data
- Contain several faces or layers
- Work as an array of texture data

Apps typically use textures to render details onto the surfaces in a scene or a 3D model. You can also use textures for post-processing pipelines, such as adding an advanced visual effect to an image before presenting it to a display.

Although textures can consume large amounts of memory, they also offer strategies, such as texture compression, that can save storage and memory bandwidth. Apple silicon GPUs support memoryless textures for transient render attachments that only need to exist for the duration of a render pass.

## Topics

### Texture Basics
- [Understanding Color-Renderable Pixel Format Sizes](understanding-color-renderable-pixel-format-sizes.md)
  Know the size limits of color render targets in Apple GPUs based on the target’s pixel format.
- [Optimizing Texture Data](optimizing-texture-data.md)
  Optimize a texture’s data to improve GPU or CPU access.
- [protocol MTLTexture](mtltexture.md)
  A resource that holds formatted image data.
- [enum MTLTextureCompressionType](mtltexturecompressiontype.md)
- [class MTLTextureDescriptor](mtltexturedescriptor.md)
  An object that you use to configure new Metal texture objects.
- [class MTKTextureLoader](../MetalKit/MTKTextureLoader.md)
  An object that creates textures from existing data in common image formats.
- [class MTLSharedTextureHandle](mtlsharedtexturehandle.md)
  A texture handle that can be shared across process address space boundaries.
- [enum MTLPixelFormat](mtlpixelformat.md)
  The data formats that describe the organization and characteristics of individual pixels in a texture.
### Texture Samplers
- [Creating and Sampling Textures](creating-and-sampling-textures.md)
  Load image data into a texture and apply it to a quadrangle.
- [protocol MTLSamplerState](mtlsamplerstate.md)
  An object that defines how a texture should be sampled.
- [class MTLSamplerDescriptor](mtlsamplerdescriptor.md)
  An object that you use to configure a texture sampler.
- [struct MTLSamplePosition](mtlsampleposition.md)
  A subpixel sample position for use in multisample antialiasing (MSAA).
### Texture Mipmapping
- [Improving Texture Sampling Quality and Performance with Mipmaps](improving-texture-sampling-quality-and-performance-with-mipmaps.md)
  Avoid texture-rendering artifacts and reduce the GPU’s workload by creating smaller versions of a texture.
- [Creating a Mipmapped Texture](creating-a-mipmapped-texture.md)
  Decide whether a texture that you’re creating needs mipmaps.
- [Copying Data into or out of Mipmaps](copying-data-into-or-out-of-mipmaps.md)
  Specify which mipmaps that the data transfer affects.
- [Generating Mipmap Data](generating-mipmap-data.md)
  Create your mipmaps either when you author content or at runtime.
- [Adding Mipmap Filtering to Samplers](adding-mipmap-filtering-to-samplers.md)
  Specify how the GPU samples mipmaps in your textures.
- [Restricting Access to Specific Mipmaps](restricting-access-to-specific-mipmaps.md)
  Set the range of mipmap levels that a sampler can access.
- [Predicting Which Mips the GPU Samples with Level-of-Detail Queries](predicting-which-mips-the-gpu-samples-with-level-of-detail-queries.md)
  Determine in advance which mipmap levels the GPU requires to sample a texture.
- [Dynamically Adjusting Texture Level of Detail](dynamically-adjusting-texture-level-of-detail.md)
  Defer generating or loading larger mipmaps until that level of detail is needed.
### Sparse Textures
- [Managing Sparse Texture Memory](managing-sparse-texture-memory.md)
  Take direct control of memory allocation for texture data by using sparse textures.
- [Creating Sparse Heaps and Sparse Textures](creating-sparse-heaps-and-sparse-textures.md)
  Allocate memory for sparse textures by creating a sparse heap.
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
### Texture Loading
- [class MTKTextureLoader](../MetalKit/MTKTextureLoader.md)
  An object that creates textures from existing data in common image formats.
- [MTKTextureLoader.Error](../MetalKit/MTKTextureLoader/Error.md)
  Errors returned by the texture loader.
- [MTKTextureLoader.Option](../MetalKit/MTKTextureLoader/Option.md)
  Keys and values used to specify loading options.
- [typealias Callback = ((any MTLTexture)?, (any Error)?) -> Void](../MetalKit/MTKTextureLoader/Callback.md)
  The signature for the block executed after an asynchronous loading operation for a single texture has completed.
- [typealias ArrayCallback = ([any MTLTexture], (any Error)?) -> Void](../MetalKit/MTKTextureLoader/ArrayCallback.md)
  The signature for the block executed after an asynchronous loading operation for multiple textures has completed.

## See Also

- [Resource Fundamentals](resource-fundamentals.md)
  Control the common attributes of all Metal memory resources, including buffers and textures, and how to configure their underlying memory.
- [Buffers](buffers.md)
  Create and manage untyped data your app uses to exchange information with its shader functions.
- [Memory Heaps](memory-heaps.md)
  Take control of your app’s GPU memory management by creating a large memory allocation for various buffers, textures, and other resources.
- [Resource Loading](resource-loading.md)
  Load assets in your games and apps quickly by running a dedicated input/output queue alongside your GPU tasks.
- [Resource Synchronization](resource-synchronization.md)
  Prevent multiple commands that can access the same resources simultaneously by coordinating those accesses with barriers, fences, or events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/textures)*