# MTLResourceStateCommandEncoder

**Framework**: Metal  
**Kind**: protocol

An encoder that encodes commands that modify resource configurations.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol MTLResourceStateCommandEncoder : MTLCommandEncoder
```

## Mentions

- [Assigning Memory to Sparse Textures](assigning-memory-to-sparse-textures.md)

#### Overview

Use a resource state command encoder to manage memory mappings for sparse textures.

Your app does not define classes that implement this protocol. To create a [`MTLResourceStateCommandEncoder`](mtlresourcestatecommandencoder.md) object, call the [`makeResourceStateCommandEncoder()`](mtlcommandbuffer/makeresourcestatecommandencoder().md) method of the [`MTLCommandBuffer`](mtlcommandbuffer.md) object into which you want to encode blit commands. Next, call methods on the [`MTLResourceStateCommandEncoder`](mtlresourcestatecommandencoder.md) object to enqueue state updates. Finally, call [`endEncoding()`](mtlcommandencoder/endencoding().md) to finish the encoding process.

## Topics

### Updating Texture Memory Assignments
- [func updateTextureMapping(any MTLTexture, mode: MTLSparseTextureMappingMode, region: MTLRegion, mipLevel: Int, slice: Int)](mtlresourcestatecommandencoder/updatetexturemapping(_:mode:region:miplevel:slice:).md)
  Encodes a command to update the texture mappings for a region in a single texture mipmap.
- [func updateTextureMappings(any MTLTexture, mode: MTLSparseTextureMappingMode, regions: UnsafePointer<MTLRegion>, mipLevels: UnsafePointer<Int>, slices: UnsafePointer<Int>, numRegions: Int)](mtlresourcestatecommandencoder/updatetexturemappings(_:mode:regions:miplevels:slices:numregions:).md)
  Encodes a command to update memory mappings for multiple regions inside a texture.
- [enum MTLSparseTextureMappingMode](mtlsparsetexturemappingmode.md)
  Options for sparse texture mapping.
### Updating Texture Memory Assignments Indirectly
- [func updateTextureMapping(any MTLTexture, mode: MTLSparseTextureMappingMode, indirectBuffer: any MTLBuffer, indirectBufferOffset: Int)](mtlresourcestatecommandencoder/updatetexturemapping(_:mode:indirectbuffer:indirectbufferoffset:).md)
  Encodes a command to update a texture’s memory mappings, specifying the parameters indirectly.
### Performing Fence Operations
- [func update(any MTLFence)](mtlresourcestatecommandencoder/update(_:).md)
  Encodes a command that instructs the GPU to update a fence, which signals passes waiting on the fence.
- [func wait(for: any MTLFence)](mtlresourcestatecommandencoder/wait(for:).md)
  Encodes a command that instructs the GPU to pause before starting the resource state commands until another pass updates a fence.
### Instance Methods
- [func moveTextureMappings(sourceTexture: any MTLTexture, sourceSlice: Int, sourceLevel: Int, sourceOrigin: MTLOrigin, sourceSize: MTLSize, destinationTexture: any MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin)](mtlresourcestatecommandencoder/movetexturemappings(sourcetexture:sourceslice:sourcelevel:sourceorigin:sourcesize:destinationtexture:destinationslice:destinationlevel:destinationorigin:).md)

## Relationships

### Inherits From
- [MTLCommandEncoder](mtlcommandencoder.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

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
- [struct MTLMapIndirectArguments](mtlmapindirectarguments.md)
  The data layout for mapping sparse texture regions when using indirect commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresourcestatecommandencoder)*