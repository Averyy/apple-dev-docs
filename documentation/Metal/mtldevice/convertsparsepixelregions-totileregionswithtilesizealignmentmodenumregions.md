# convertSparsePixelRegions(_:toTileRegions:withTileSize:alignmentMode:numRegions:)

**Framework**: Metal  
**Kind**: method

Converts a list of sparse pixel regions to tile regions.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
optional func convertSparsePixelRegions(_ pixelRegions: UnsafePointer<MTLRegion>, toTileRegions tileRegions: UnsafeMutablePointer<MTLRegion>, withTileSize tileSize: MTLSize, alignmentMode mode: MTLSparseTextureRegionAlignmentMode, numRegions: Int)
```

## Mentions

- [Converting between pixel regions and sparse tile regions](converting-between-pixel-regions-and-sparse-tile-regions.md)

## Parameters

- `pixelRegions`: A pointer to a C array of pixel   instances.
- `tileRegions`: A pointer to a C array of tile   instances.
- `tileSize`: An   instance that represents a sparse tile’s size, in pixels.
- `mode`: An   instance.
- `numRegions`: The number of regions you want the method to convert.

## See Also

- [func sparseTileSize(textureType: MTLTextureType, pixelFormat: MTLPixelFormat, sampleCount: Int, sparsePageSize: MTLSparsePageSize) -> MTLSize](mtldevice/sparsetilesize(texturetype:pixelformat:samplecount:sparsepagesize:).md)
  Returns the dimensions of a sparse tile for a texture that has a specific sparse page size.
- [func sparseTileSize(with: MTLTextureType, pixelFormat: MTLPixelFormat, sampleCount: Int) -> MTLSize](mtldevice/sparsetilesize(with:pixelformat:samplecount:).md)
  Returns the dimensions of a sparse tile for a texture.
- [func sparseTileSizeInBytes(sparsePageSize: MTLSparsePageSize) -> Int](mtldevice/sparsetilesizeinbytes(sparsepagesize:).md)
  Returns the size, in bytes, of a sparse tile the GPU device creates with a specific page size.
- [var sparseTileSizeInBytes: Int](mtldevice/sparsetilesizeinbytes.md)
  Returns the size, in bytes, of a sparse tile the GPU device creates using a default page size.
- [func convertSparseTileRegions(UnsafePointer<MTLRegion>, toPixelRegions: UnsafeMutablePointer<MTLRegion>, withTileSize: MTLSize, numRegions: Int)](mtldevice/convertsparsetileregions(_:topixelregions:withtilesize:numregions:).md)
  Converts a list of sparse tile regions to pixel regions.
- [enum MTLSparsePageSize](mtlsparsepagesize.md)
  The page size options, in kilobytes, for sparse textures.
- [enum MTLSparseTextureRegionAlignmentMode](mtlsparsetextureregionalignmentmode.md)
  Options used when converting between a pixel-based region within a texture to a tile-based region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/convertsparsepixelregions(_:totileregions:withtilesize:alignmentmode:numregions:))*