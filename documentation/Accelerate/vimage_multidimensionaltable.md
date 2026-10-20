# vImage_MultidimensionalTable

**Framework**: Accelerate  
**Kind**: typealias  
**Role**: Type Alias

An opaque pointer that represents a multidimensional lookup table.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias vImage_MultidimensionalTable = OpaquePointer
```

```c
typedef struct vImage_MultidimensionalTableData * vImage_MultidimensionalTable;
```

## Mentions

- [Applying color transforms to images with a multidimensional lookup table](./applying-color-transforms-to-images-with-a-multidimensional-lookup-table.md)

## See Also

### Transforming with a multidimensional lookup table
- [Applying color transforms to images with a multidimensional lookup table](./applying-color-transforms-to-images-with-a-multidimensional-lookup-table.md)
  Precompute translation values to optimize color space conversion and other pointwise operations.
- [Cropping to the subject in a chroma-keyed image](./cropping-to-the-subject-in-a-chroma-keyed-image.md)
  Convert a chroma-key color to alpha values and trim transparent pixels using Accelerate.
- [Applying transformations to selected colors in an image](./applying-transformations-to-selected-colors-in-an-image.md)
  Desaturate a range of colors in an image with a multidimensional lookup table.
- [func vImageMultidimensionalTable_Create(UnsafePointer<UInt16>, UInt32, UInt32, UnsafePointer<UInt8>, vImageMDTableUsageHint, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> vImage_MultidimensionalTable!](./vimagemultidimensionaltable_create%28_,_,_,_,_,_,_%29.md)
  Creates a multidimensional lookup table.
- [func vImageMultiDimensionalInterpolatedLookupTable_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImage_MultidimensionalTable, vImage_InterpolationMethod, vImage_Flags) -> vImage_Error](./vimagemultidimensionalinterpolatedlookuptable_planarf%28_,_,_,_,_,_%29.md)
  Uses a multidimensional lookup table to transform a 32-bit planar image.
- [func vImageMultiDimensionalInterpolatedLookupTable_Planar16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImage_MultidimensionalTable, vImage_InterpolationMethod, vImage_Flags) -> vImage_Error](./vimagemultidimensionalinterpolatedlookuptable_planar16q12%28_,_,_,_,_,_%29.md)
  Uses a multidimensional lookup table to transform a 16Q12 planar image.
- [func vImageMultidimensionalTable_Retain(vImage_MultidimensionalTable!) -> vImage_Error](./vimagemultidimensionaltable_retain%28_%29.md)
  Retains a multidimensional table.
- [func vImageMultidimensionalTable_Release(vImage_MultidimensionalTable!) -> vImage_Error](./vimagemultidimensionaltable_release%28_%29.md)
  Releases a multidimensional table.
- [struct vImageMDTableUsageHint](./vimagemdtableusagehint.md)
  Constants that indicate the use for a multidimensional lookup table.
- [struct vImage_InterpolationMethod](./vimage_interpolationmethod.md)
  Constants that represent different interpolation methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_multidimensionaltable)*