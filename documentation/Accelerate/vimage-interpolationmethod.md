# vImage_InterpolationMethod

**Framework**: Accelerate  
**Kind**: struct

Constants that represent different interpolation methods.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct vImage_InterpolationMethod
```

## Topics

### Interpolation method constants
- [var kvImageNoInterpolation: vImage_InterpolationMethod](kvimagenointerpolation.md)
  Nearest neighbor interpolation.
- [var kvImageHalfInterpolation: vImage_InterpolationMethod](kvimagehalfinterpolation.md)
  Partial linear interpolation.
- [var kvImageFullInterpolation: vImage_InterpolationMethod](kvimagefullinterpolation.md)
  Full linear interpolation.
### Raw values
- [init(UInt32)](vimage_interpolationmethod/init(_:).md)
  Creates an interpolation method constant with an unsigned-integer value.
- [init(rawValue: UInt32)](vimage_interpolationmethod/init(rawvalue:).md)
  Creates an interpolation method constant with an unsigned-integer value.
- [var rawValue: UInt32](vimage_interpolationmethod/rawvalue.md)
  The raw value that represents the interpolation method constant.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

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
- [func vImageMultidimensionalTable_Release(vImage_MultidimensionalTable!) -> vImage_Error](vimagemultidimensionaltable_release(_:).md)
  Releases a multidimensional table.
- [typealias vImage_MultidimensionalTable](vimage_multidimensionaltable.md)
  An opaque pointer that represents a multidimensional lookup table.
- [struct vImageMDTableUsageHint](vimagemdtableusagehint.md)
  Constants that indicate the use for a multidimensional lookup table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_interpolationmethod)*