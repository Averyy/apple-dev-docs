# sparseTileSize(with:pixelFormat:sampleCount:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Returns the dimensions of a sparse tile for a texture.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func sparseTileSize(with textureType: MTLTextureType, pixelFormat: MTLPixelFormat, sampleCount: Int) -> MTLSize
```

## Mentions

- [Converting Between Pixel Regions and Sparse Tile Regions](converting-between-pixel-regions-and-sparse-tile-regions.md)

#### Return Value

A new [`MTLSize`](mtlsize.md) instance.

#### Discussion

The size of a sparse tile, in bytes, is the same for all sparse textures on a GPU device object. Because the size of pixels may vary, the actual dimensions of a sparse tile vary based on the texture and the pixel format. Use this method to get the dimensions of the tile for a particular format. Use these dimensions when converting regions from pixel-based units to sparse tile units and vice versa.

## Parameters

- `textureType`: An   instance.
- `pixelFormat`: An   instance.
- `sampleCount`: The number of samples for each pixel.

## See Also

- [func sparseTileSize(textureType: MTLTextureType, pixelFormat: MTLPixelFormat, sampleCount: Int, sparsePageSize: MTLSparsePageSize) -> MTLSize](mtldevice/sparsetilesize(texturetype:pixelformat:samplecount:sparsepagesize:).md)
  Returns the dimensions of a sparse tile for a texture that has a specific sparse page size.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/sparsetilesize(with:pixelformat:samplecount:))*