# vImageMultidimensionalTable_Release(_:)

**Framework**: Accelerate  
**Kind**: func

Releases a multidimensional table.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 7.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageMultidimensionalTable_Release(_ table: vImage_MultidimensionalTable!) -> vImage_Error
```

## Mentions

- [Applying color transforms to images with a multidimensional lookup table](applying-color-transforms-to-images-with-a-multidimensional-lookup-table.md)

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

This function decrements the multidimensional table’s reference count. When the reference count reaches `0`, the system destroys the object.

## Parameters

- `table`: The multidimensional table to release.

## See Also

- [Applying color transforms to images with a multidimensional lookup table](applying-color-transforms-to-images-with-a-multidimensional-lookup-table.md)
  Precompute translation values to optimize color space conversion and other pointwise operations.
- [Cropping to the subject in a chroma-keyed image](cropping-to-the-subject-in-a-chroma-keyed-image.md)
  Convert a chroma-key color to alpha values and trim transparent pixels using Accelerate.
- [Applying transformations to selected colors in an image](applying-transformations-to-selected-colors-in-an-image.md)
  Desaturate a range of colors in an image with a multidimensional lookup table.
- [func vImageMultidimensionalTable_Create(UnsafePointer<UInt16>, UInt32, UInt32, UnsafePointer<UInt8>, vImageMDTableUsageHint, vImage_Flags, UnsafeMutablePointer<vImage_Error>!) -> vImage_MultidimensionalTable!](vimagemultidimensionaltable_create(_:_:_:_:_:_:_:).md)
  Creates a multidimensional lookup table.
- [func vImageMultiDimensionalInterpolatedLookupTable_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImage_MultidimensionalTable, vImage_InterpolationMethod, vImage_Flags) -> vImage_Error](vimagemultidimensionalinterpolatedlookuptable_planarf(_:_:_:_:_:_:).md)
  Uses a multidimensional lookup table to transform a 32-bit planar image.
- [func vImageMultiDimensionalInterpolatedLookupTable_Planar16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImage_MultidimensionalTable, vImage_InterpolationMethod, vImage_Flags) -> vImage_Error](vimagemultidimensionalinterpolatedlookuptable_planar16q12(_:_:_:_:_:_:).md)
  Uses a multidimensional lookup table to transform a 16Q12 planar image.
- [func vImageMultidimensionalTable_Retain(vImage_MultidimensionalTable!) -> vImage_Error](vimagemultidimensionaltable_retain(_:).md)
  Retains a multidimensional table.
- [typealias vImage_MultidimensionalTable](vimage_multidimensionaltable.md)
  An opaque pointer that represents a multidimensional lookup table.
- [struct vImageMDTableUsageHint](vimagemdtableusagehint.md)
  Constants that indicate the use for a multidimensional lookup table.
- [struct vImage_InterpolationMethod](vimage_interpolationmethod.md)
  Constants that represent different interpolation methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagemultidimensionaltable_release(_:))*