# Resource creation

**Framework**: Metal

Load assets with input/output queues and make various resource instances, such as buffers, textures, acceleration structures, and memory heaps.

## Topics

### Working with resource heaps
- [func makeHeap(descriptor: MTLHeapDescriptor) -> (any MTLHeap)?](mtldevice/makeheap(descriptor:).md)
  Creates a new GPU heap instance.
- [func heapBufferSizeAndAlign(length: Int, options: MTLResourceOptions) -> MTLSizeAndAlign](mtldevice/heapbuffersizeandalign(length:options:).md)
  Returns the size and alignment, in bytes, of a buffer if you create it from a heap.
- [func heapTextureSizeAndAlign(descriptor: MTLTextureDescriptor) -> MTLSizeAndAlign](mtldevice/heaptexturesizeandalign(descriptor:).md)
  Returns the size and alignment, in bytes, of a texture if you create it from a heap.
- [func heapAccelerationStructureSizeAndAlign(size: Int) -> MTLSizeAndAlign](mtldevice/heapaccelerationstructuresizeandalign(size:).md)
  Returns the size and alignment, in bytes, of an acceleration structure if you create it from a heap.
- [func heapAccelerationStructureSizeAndAlign(descriptor: MTLAccelerationStructureDescriptor) -> MTLSizeAndAlign](mtldevice/heapaccelerationstructuresizeandalign(descriptor:).md)
  Returns the size and alignment, in bytes, of an acceleration structure if you create it from a heap with a descriptor.
- [struct MTLSizeAndAlign](mtlsizeandalign.md)
  The size and alignment of a resource, in bytes.
### Creating buffers
- [var maxBufferLength: Int](mtldevice/maxbufferlength.md)
  The largest amount of memory, in bytes, that a GPU device can allocate to a buffer instance.
- [func makeBuffer(length: Int, options: MTLResourceOptions) -> (any MTLBuffer)?](mtldevice/makebuffer(length:options:).md)
  Creates a buffer the method clears with zero values.
- [func makeBuffer(bytes: UnsafeRawPointer, length: Int, options: MTLResourceOptions) -> (any MTLBuffer)?](mtldevice/makebuffer(bytes:length:options:).md)
  Allocates a new buffer of a given length and initializes its contents by copying existing data into it.
- [func makeBuffer(bytesNoCopy: UnsafeMutableRawPointer, length: Int, options: MTLResourceOptions, deallocator: ((UnsafeMutableRawPointer, Int) -> Void)?) -> (any MTLBuffer)?](mtldevice/makebuffer(bytesnocopy:length:options:deallocator:).md)
  Creates a buffer that wraps an existing contiguous memory allocation.
### Creating textures
- [func makeTexture(descriptor: MTLTextureDescriptor) -> (any MTLTexture)?](mtldevice/maketexture(descriptor:).md)
  Creates a new texture instance.
- [func makeTexture(descriptor: MTLTextureDescriptor, iosurface: IOSurfaceRef, plane: Int) -> (any MTLTexture)?](mtldevice/maketexture(descriptor:iosurface:plane:).md)
  Creates a texture instance that uses I/O surface to store its underlying data.
- [func makeSharedTexture(descriptor: MTLTextureDescriptor) -> (any MTLTexture)?](mtldevice/makesharedtexture(descriptor:).md)
  Creates a texture that you can share across process boundaries.
- [func makeSharedTexture(handle: MTLSharedTextureHandle) -> (any MTLTexture)?](mtldevice/makesharedtexture(handle:).md)
  Creates a texture that references a shared texture.
- [func minimumLinearTextureAlignment(for: MTLPixelFormat) -> Int](mtldevice/minimumlineartexturealignment(for:).md)
  Returns the minimum alignment the GPU device requires to create a linear texture from a buffer.
- [func minimumTextureBufferAlignment(for: MTLPixelFormat) -> Int](mtldevice/minimumtexturebufferalignment(for:).md)
  Returns the minimum alignment the GPU device requires to create a texture buffer from a buffer.
### Creating samplers
- [func supportsTextureSampleCount(Int) -> Bool](mtldevice/supportstexturesamplecount(_:).md)
  Returns a Boolean value that indicates whether the GPU can sample a texture with a specific number of sample points.
- [func makeSamplerState(descriptor: MTLSamplerDescriptor) -> (any MTLSamplerState)?](mtldevice/makesamplerstate(descriptor:).md)
  Creates a sampler state instance.
- [func getDefaultSamplePositions(sampleCount: Int) -> [MTLSamplePosition]](mtldevice/getdefaultsamplepositions(samplecount:).md)
  Returns the default sample locations based on the number of samples.
### Working with sparse textures
- [func sparseTileSize(textureType: MTLTextureType, pixelFormat: MTLPixelFormat, sampleCount: Int, sparsePageSize: MTLSparsePageSize) -> MTLSize](mtldevice/sparsetilesize(texturetype:pixelformat:samplecount:sparsepagesize:).md)
  Returns the dimensions of a sparse tile for a texture that has a specific sparse page size.
- [func sparseTileSize(with: MTLTextureType, pixelFormat: MTLPixelFormat, sampleCount: Int) -> MTLSize](mtldevice/sparsetilesize(with:pixelformat:samplecount:).md)
  Returns the dimensions of a sparse tile for a texture.
- [func sparseTileSizeInBytes(sparsePageSize: MTLSparsePageSize) -> Int](mtldevice/sparsetilesizeinbytes(sparsepagesize:).md)
  Returns the size, in bytes, of a sparse tile the GPU device creates with a specific page size.
- [var sparseTileSizeInBytes: Int](mtldevice/sparsetilesizeinbytes.md)
  Returns the size, in bytes, of a sparse tile the GPU device creates using a default page size.
- [func convertSparsePixelRegions(UnsafePointer<MTLRegion>, toTileRegions: UnsafeMutablePointer<MTLRegion>, withTileSize: MTLSize, alignmentMode: MTLSparseTextureRegionAlignmentMode, numRegions: Int)](mtldevice/convertsparsepixelregions(_:totileregions:withtilesize:alignmentmode:numregions:).md)
  Converts a list of sparse pixel regions to tile regions.
- [func convertSparseTileRegions(UnsafePointer<MTLRegion>, toPixelRegions: UnsafeMutablePointer<MTLRegion>, withTileSize: MTLSize, numRegions: Int)](mtldevice/convertsparsetileregions(_:topixelregions:withtilesize:numregions:).md)
  Converts a list of sparse tile regions to pixel regions.
- [enum MTLSparsePageSize](mtlsparsepagesize.md)
  The page size options, in kilobytes, for sparse textures.
- [enum MTLSparseTextureRegionAlignmentMode](mtlsparsetextureregionalignmentmode.md)
  Options used when converting between a pixel-based region within a texture to a tile-based region.
### Creating acceleration structures for ray tracing
- [func makeAccelerationStructure(descriptor: MTLAccelerationStructureDescriptor) -> (any MTLAccelerationStructure)?](mtldevice/makeaccelerationstructure(descriptor:).md)
  Creates a new ray-tracing acceleration structure from a descriptor.
- [func makeAccelerationStructure(size: Int) -> (any MTLAccelerationStructure)?](mtldevice/makeaccelerationstructure(size:).md)
  Creates a new acceleration structure with a specific size.
- [func accelerationStructureSizes(descriptor: MTLAccelerationStructureDescriptor) -> MTLAccelerationStructureSizes](mtldevice/accelerationstructuresizes(descriptor:).md)
  Returns the buffer sizes the GPU device needs to build, refit, and store an acceleration structure.
- [struct MTLAccelerationStructureSizes](mtlaccelerationstructuresizes.md)
  The expected sizes for a ray-tracing acceleration structure.
### Creating argument buffer encoders
- [var argumentBuffersSupport: MTLArgumentBuffersTier](mtldevice/argumentbufferssupport.md)
  Returns the GPU device’s support tier for argument buffers.
- [var maxArgumentBufferSamplerCount: Int](mtldevice/maxargumentbuffersamplercount.md)
  The maximum number of unique argument buffer samplers per app.
- [func makeArgumentEncoder(arguments: [MTLArgumentDescriptor]) -> (any MTLArgumentEncoder)?](mtldevice/makeargumentencoder(arguments:).md)
  Creates a new argument encoder for an array of arguments.
- [func makeArgumentEncoder(bufferBinding: any MTLBufferBinding) -> any MTLArgumentEncoder](mtldevice/makeargumentencoder(bufferbinding:).md)
  Creates a new argument encoder for a buffer binding.
### Creating fences and events
- [func makeFence() -> (any MTLFence)?](mtldevice/makefence.md)
  Creates a new memory fence instance.
- [func makeEvent() -> (any MTLEvent)?](mtldevice/makeevent.md)
  Creates a new event instance that you can use to synchronize commands and resources within the same GPU device.
- [func makeSharedEvent() -> (any MTLSharedEvent)?](mtldevice/makesharedevent.md)
  Creates a new shared event instance that you can use to synchronize commands and resources across different GPU devices.
- [func makeSharedEvent(handle: MTLSharedEventHandle) -> (any MTLSharedEvent)?](mtldevice/makesharedevent(handle:).md)
  Recreates a shared event from a handle.
### Creating rasterization rate maps
- [func supportsRasterizationRateMap(layerCount: Int) -> Bool](mtldevice/supportsrasterizationratemap(layercount:).md)
  Returns a Boolean value that indicates whether the GPU can create a rasterization rate map with a specific number of layers.
- [func makeRasterizationRateMap(descriptor: MTLRasterizationRateMapDescriptor) -> (any MTLRasterizationRateMap)?](mtldevice/makerasterizationratemap(descriptor:).md)
  Creates a rasterization rate map instance.

## See Also

- [Device inspection](device-inspection.md)
  Locate and identify a GPU and the features it supports, and sample its counters.
- [Work submission](work-submission.md)
  Create queues that submit work to the GPU or load assets into GPU resources, and indirect command buffers that group your frequent commands together.
- [Pipeline state creation](pipeline-state-creation.md)
  Create pipeline states for render and compute passes, samplers, depth and stencil states, and indirect command buffers.
- [Shader library and archive creation](shader-library-and-archive-creation.md)
  Create static and dynamic shader libraries, and binary shader archives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/resource-creation)*