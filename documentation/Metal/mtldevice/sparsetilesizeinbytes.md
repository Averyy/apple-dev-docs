# sparseTileSizeInBytes

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

Returns the size, in bytes, of a sparse tile the GPU device creates using a default page size.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var sparseTileSizeInBytes: Int { get }
```

## Mentions

- [Creating sparse heaps and sparse textures](creating-sparse-heaps-and-sparse-textures.md)

## See Also

- [func sparseTileSize(textureType: MTLTextureType, pixelFormat: MTLPixelFormat, sampleCount: Int, sparsePageSize: MTLSparsePageSize) -> MTLSize](mtldevice/sparsetilesize(texturetype:pixelformat:samplecount:sparsepagesize:).md)
  Returns the dimensions of a sparse tile for a texture that has a specific sparse page size.
- [func sparseTileSize(with: MTLTextureType, pixelFormat: MTLPixelFormat, sampleCount: Int) -> MTLSize](mtldevice/sparsetilesize(with:pixelformat:samplecount:).md)
  Returns the dimensions of a sparse tile for a texture.
- [func sparseTileSizeInBytes(sparsePageSize: MTLSparsePageSize) -> Int](mtldevice/sparsetilesizeinbytes(sparsepagesize:).md)
  Returns the size, in bytes, of a sparse tile the GPU device creates with a specific page size.
- [func convertSparsePixelRegions(UnsafePointer<MTLRegion>, toTileRegions: UnsafeMutablePointer<MTLRegion>, withTileSize: MTLSize, alignmentMode: MTLSparseTextureRegionAlignmentMode, numRegions: Int)](mtldevice/convertsparsepixelregions(_:totileregions:withtilesize:alignmentmode:numregions:).md)
  Converts a list of sparse pixel regions to tile regions.
- [func convertSparseTileRegions(UnsafePointer<MTLRegion>, toPixelRegions: UnsafeMutablePointer<MTLRegion>, withTileSize: MTLSize, numRegions: Int)](mtldevice/convertsparsetileregions(_:topixelregions:withtilesize:numregions:).md)
  Converts a list of sparse tile regions to pixel regions.
- [enum MTLSparsePageSize](mtlsparsepagesize.md)
  The page size options, in kilobytes, for sparse textures.
- [enum MTLSparseTextureRegionAlignmentMode](mtlsparsetextureregionalignmentmode.md)
  Options used when converting between a pixel-based region within a texture to a tile-based region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/sparsetilesizeinbytes)*