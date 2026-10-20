# MTLSparseTextureRegionAlignmentMode

**Framework**: Metal  
**Kind**: enum  
**Role**: Enumeration

Options used when converting between a pixel-based region within a texture to a tile-based region.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum MTLSparseTextureRegionAlignmentMode
```

```c
enum MTLSparseTextureRegionAlignmentMode : NSUInteger;
```

## Topics

### Specifying the alignment mode
- [MTLSparseTextureRegionAlignmentMode.outward](./mtlsparsetextureregionalignmentmode/outward.md)
  The tile region includes any partially covered tiles.
- [MTLSparseTextureRegionAlignmentMode.inward](./mtlsparsetextureregionalignmentmode/inward.md)
  The tile region ignores partially covered tiles.
### Initializers
- [init?(rawValue: UInt)](./mtlsparsetextureregionalignmentmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Working with sparse textures
- [func sparseTileSize(textureType: MTLTextureType, pixelFormat: MTLPixelFormat, sampleCount: Int, sparsePageSize: MTLSparsePageSize) -> MTLSize](./mtldevice/sparsetilesize%28texturetype,pixelformat,samplecount,sparsepagesize%29.md)
  Returns the dimensions of a sparse tile for a texture that has a specific sparse page size.
- [func sparseTileSize(with: MTLTextureType, pixelFormat: MTLPixelFormat, sampleCount: Int) -> MTLSize](./mtldevice/sparsetilesize%28with,pixelformat,samplecount%29.md)
  Returns the dimensions of a sparse tile for a texture.
- [func sparseTileSizeInBytes(sparsePageSize: MTLSparsePageSize) -> Int](./mtldevice/sparsetilesizeinbytes%28sparsepagesize%29.md)
  Returns the size, in bytes, of a sparse tile the GPU device creates with a specific page size.
- [var sparseTileSizeInBytes: Int](./mtldevice/sparsetilesizeinbytes.md)
  Returns the size, in bytes, of a sparse tile the GPU device creates using a default page size.
- [func convertSparsePixelRegions(UnsafePointer<MTLRegion>, toTileRegions: UnsafeMutablePointer<MTLRegion>, withTileSize: MTLSize, alignmentMode: MTLSparseTextureRegionAlignmentMode, numRegions: Int)](./mtldevice/convertsparsepixelregions%28_,totileregions,withtilesize,alignmentmode,numregions%29.md)
  Converts a list of sparse pixel regions to tile regions.
- [func convertSparseTileRegions(UnsafePointer<MTLRegion>, toPixelRegions: UnsafeMutablePointer<MTLRegion>, withTileSize: MTLSize, numRegions: Int)](./mtldevice/convertsparsetileregions%28_,topixelregions,withtilesize,numregions%29.md)
  Converts a list of sparse tile regions to pixel regions.
- [enum MTLSparsePageSize](./mtlsparsepagesize.md)
  The page size options, in kilobytes, for sparse textures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsparsetextureregionalignmentmode)*