# vImageHorizontalShearD_CbCr16S(_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func vImageHorizontalShearD_CbCr16S(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ xTranslate: Double, _ shearSlope: Double, _ filter: ResamplingFilter!, _ backColor: UnsafePointer<Int16>!, _ flags: vImage_Flags) -> vImage_Error
```

## See Also

- [func vImageHorizontalShearD_Planar16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, Pixel_16F, vImage_Flags) -> vImage_Error](vimagehorizontalsheard_planar16f(_:_:_:_:_:_:_:_:_:).md)
  Performs a double-precision horizontal shear on a region of interest within a floating-point 16-bit planar image.
- [func vImageHorizontalShearD_CbCr16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimagehorizontalsheard_cbcr16f(_:_:_:_:_:_:_:_:_:).md)
  Performs a double-precision horizontal shear on a region of interest within a floating-point 16-bit-per-channel, 2-channel interleaved image.
- [func vImageHorizontalShearD_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimagehorizontalsheard_argb16u(_:_:_:_:_:_:_:_:_:).md)
  Performs a double-precision horizontal shear on a region of interest within an unsigned 16-bit-per-channel, 4-channel interleaved image.
- [func vImageHorizontalShearD_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<Int16>!, vImage_Flags) -> vImage_Error](vimagehorizontalsheard_argb16s(_:_:_:_:_:_:_:_:_:).md)
  Performs a double-precision horizontal shear on a region of interest within a signed 16-bit-per-channel, 4-channel interleaved image.
- [func vImageHorizontalShearD_ARGB16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimagehorizontalsheard_argb16f(_:_:_:_:_:_:_:_:_:).md)
  Performs a double-precision horizontal shear on a region of interest within a floating-point 16-bit-per-channel, 4-channel interleaved image.
- [func vImageHorizontalShearD_CbCr16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimagehorizontalsheard_cbcr16u(_:_:_:_:_:_:_:_:_:).md)
- [func vImageHorizontalShear_CbCr16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, UnsafePointer<Int16>!, vImage_Flags) -> vImage_Error](vimagehorizontalshear_cbcr16s(_:_:_:_:_:_:_:_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagehorizontalsheard_cbcr16s(_:_:_:_:_:_:_:_:_:))*