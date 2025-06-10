# Transforming with lookup tables

**Framework**: Accelerate

Use lookup tables to apply color transformations to images.

#### Overview

Lookup table functions use the value of a source pixel as an index into a lookup table of colors that defines the corresponding destination pixel. You can use lookup table functions to perform tasks, such as color grading, converting between color spaces, or generating false-color images.

## Topics

### Transforming planar-to-planar with a lookup table
- [func vImageTableLookUp_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_8>, vImage_Flags) -> vImage_Error](vimagetablelookup_planar8(_:_:_:_:).md)
  Uses a lookup table to transform an 8-bit planar image to an 8-bit planar image.
- [func vImageLookupTable_PlanarFtoPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_8>, vImage_Flags) -> vImage_Error](vimagelookuptable_planarftoplanar8(_:_:_:_:).md)
  Uses a lookup table to transform a 32-bit planar image to an 8-bit planar image.
- [func vImageLookupTable_Planar8toPlanar16(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_16U>, vImage_Flags) -> vImage_Error](vimagelookuptable_planar8toplanar16(_:_:_:_:).md)
  Uses a lookup table to transform an 8-bit planar image to an unsigned 16-bit planar image.
- [func vImageLookupTable_Planar8toPlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_F>, vImage_Flags) -> vImage_Error](vimagelookuptable_planar8toplanarf(_:_:_:_:).md)
  Uses a lookup table to transform an 8-bit planar image to a 32-bit planar image.
- [func vImageLookupTable_8to64U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt64>, vImage_Flags) -> vImage_Error](vimagelookuptable_8to64u(_:_:_:_:).md)
  Uses a lookup table to transform an 8-bit planar image to a 64-bit planar image.
- [func vImageLookupTable_Planar16(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_16U>, vImage_Flags) -> vImage_Error](vimagelookuptable_planar16(_:_:_:_:).md)
  Uses a lookup table to transform a 16-bit planar image.
- [func vImageInterpolatedLookupTable_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_F>, vImagePixelCount, Float, Float, vImage_Flags) -> vImage_Error](vimageinterpolatedlookuptable_planarf(_:_:_:_:_:_:_:).md)
  Uses an interpolated lookup table to transform a 32-bit planar image.
### Transforming planar-to-interleaved with a lookup table
- [func vImageLookupTable_Planar8toPlanar24(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt32>, vImage_Flags) -> vImage_Error](vimagelookuptable_planar8toplanar24(_:_:_:_:).md)
  Uses a lookup table to transform an 8-bit planar image to an 8-bit-per-channel, three-channel interleaved image.
- [func vImageLookupTable_Planar8toPlanar48(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt64>, vImage_Flags) -> vImage_Error](vimagelookuptable_planar8toplanar48(_:_:_:_:).md)
  Uses a lookup table to transform an 8-bit planar image to a 16-bit-per-channel, three-channel interleaved image.
- [func vImageLookupTable_Planar8toPlanar96(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_FFFF>, vImage_Flags) -> vImage_Error](vimagelookuptable_planar8toplanar96(_:_:_:_:).md)
  Uses a lookup table to transform an 8-bit planar image to a 32-bit-per-channel, three-channel interleaved image.
- [func vImageLookupTable_Planar8toPlanar128(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_FFFF>, vImage_Flags) -> vImage_Error](vimagelookuptable_planar8toplanar128(_:_:_:_:).md)
  Uses a lookup table to transform an 8-bit planar image to a 32-bit-per-channel, four-channel interleaved image.
### Transforming interleaved-to-interleaved with a lookup table
- [func vImageTableLookUp_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_8>!, UnsafePointer<Pixel_8>!, UnsafePointer<Pixel_8>!, UnsafePointer<Pixel_8>!, vImage_Flags) -> vImage_Error](vimagetablelookup_argb8888(_:_:_:_:_:_:_:).md)
  Uses a lookup table to transform an interleaved, four-channel 8-bit planar image to an interleaved, four-channel 8-bit planar image.
### Transforming with a multidimensional lookup table
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
- [func vImageMultidimensionalTable_Release(vImage_MultidimensionalTable!) -> vImage_Error](vimagemultidimensionaltable_release(_:).md)
  Releases a multidimensional table.
- [typealias vImage_MultidimensionalTable](vimage_multidimensionaltable.md)
  An opaque pointer that represents a multidimensional lookup table.
- [struct vImageMDTableUsageHint](vimagemdtableusagehint.md)
  Constants that indicate the use for a multidimensional lookup table.
- [struct vImage_InterpolationMethod](vimage_interpolationmethod.md)
  Constants that represent different interpolation methods.

## See Also

- [Transforming with polynomials](transforming-with-polynomials.md)
  Use polynomials to apply color transformations to images.
- [Transforming with matrix multiplication](transforming-with-matrix-multiplication.md)
  Use matrix multiplication to apply color transformations to images.
- [Transforming with a gamma function](transforming-with-a-gamma-function.md)
  Use gamma functions to apply color transformations to images.
- [Applying a flood fill to an image](applying-a-flood-fill-to-an-image.md)
  Fill connected components of an image with a new color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/transforming-with-lookup-tables)*