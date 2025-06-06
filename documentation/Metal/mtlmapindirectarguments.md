# MTLMapIndirectArguments

**Framework**: Metal  
**Kind**: struct

The data layout for mapping sparse texture regions when using indirect commands.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct MTLMapIndirectArguments
```

## Topics

### Creating Indirect Mapping Arguments
- [init()](mtlmapindirectarguments/init.md)
  Returns a default data layout for mapping sparse texture regions.
- [init(regionOriginX: UInt32, regionOriginY: UInt32, regionOriginZ: UInt32, regionSizeWidth: UInt32, regionSizeHeight: UInt32, regionSizeDepth: UInt32, mipMapLevel: UInt32, sliceId: UInt32)](mtlmapindirectarguments/init(regionoriginx:regionoriginy:regionoriginz:regionsizewidth:regionsizeheight:regionsizedepth:mipmaplevel:sliceid:).md)
  Returns a new data layout for mapping sparse texture regions.
### Specifying Region Origin
- [var regionOriginX: UInt32](mtlmapindirectarguments/regionoriginx.md)
  The x coordinate of the region to change, measured in tile coordinates.
- [var regionOriginY: UInt32](mtlmapindirectarguments/regionoriginy.md)
  The y coordinate of the region to change, measured in tile coordinates.
- [var regionOriginZ: UInt32](mtlmapindirectarguments/regionoriginz.md)
  The z coordinate of the region to change, measured in tile coordinates.
### Specifying Region Dimensions
- [var regionSizeWidth: UInt32](mtlmapindirectarguments/regionsizewidth.md)
  The width of the region, measured in tile coordinates.
- [var regionSizeHeight: UInt32](mtlmapindirectarguments/regionsizeheight.md)
  The height of the region, measured in tile coordinates.
- [var regionSizeDepth: UInt32](mtlmapindirectarguments/regionsizedepth.md)
  The depth of the region, measured in tile coordinates.
### Specifying Texture Location
- [var mipMapLevel: UInt32](mtlmapindirectarguments/mipmaplevel.md)
  The mipmap to change.
- [var sliceId: UInt32](mtlmapindirectarguments/sliceid.md)
  The texture slice to change.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

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
- [protocol MTLResourceStateCommandEncoder](mtlresourcestatecommandencoder.md)
  An encoder that encodes commands that modify resource configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlmapindirectarguments)*