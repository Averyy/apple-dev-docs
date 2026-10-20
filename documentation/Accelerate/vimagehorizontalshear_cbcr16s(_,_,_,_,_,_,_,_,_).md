# vImageHorizontalShear_CbCr16S(_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

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
func vImageHorizontalShear_CbCr16S(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ xTranslate: Float, _ shearSlope: Float, _ filter: ResamplingFilter!, _ backColor: UnsafePointer<Int16>!, _ flags: vImage_Flags) -> vImage_Error
```

```c
vImage_Error vImageHorizontalShear_CbCr16S(const vImage_Buffer *src, const vImage_Buffer *dest, vImagePixelCount srcOffsetToROI_X, vImagePixelCount srcOffsetToROI_Y, float xTranslate, float shearSlope, ResamplingFilter filter, const Pixel_16S16S backColor, vImage_Flags flags);
```

## See Also

### Shearing 16-bit-per-channel buffers
- [func vImageHorizontalShearD_Planar16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, Pixel_16F, vImage_Flags) -> vImage_Error](./vimagehorizontalsheard_planar16f%28_,_,_,_,_,_,_,_,_%29.md)
  Performs a double-precision horizontal shear on a region of interest within a floating-point 16-bit planar image.
- [func vImageHorizontalShearD_CbCr16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](./vimagehorizontalsheard_cbcr16f%28_,_,_,_,_,_,_,_,_%29.md)
  Performs a double-precision horizontal shear on a region of interest within a floating-point 16-bit-per-channel, 2-channel interleaved image.
- [func vImageHorizontalShearD_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](./vimagehorizontalsheard_argb16u%28_,_,_,_,_,_,_,_,_%29.md)
  Performs a double-precision horizontal shear on a region of interest within an unsigned 16-bit-per-channel, 4-channel interleaved image.
- [func vImageHorizontalShearD_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<Int16>!, vImage_Flags) -> vImage_Error](./vimagehorizontalsheard_argb16s%28_,_,_,_,_,_,_,_,_%29.md)
  Performs a double-precision horizontal shear on a region of interest within a signed 16-bit-per-channel, 4-channel interleaved image.
- [func vImageHorizontalShearD_ARGB16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](./vimagehorizontalsheard_argb16f%28_,_,_,_,_,_,_,_,_%29.md)
  Performs a double-precision horizontal shear on a region of interest within a floating-point 16-bit-per-channel, 4-channel interleaved image.
- [func vImageHorizontalShearD_CbCr16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<Int16>!, vImage_Flags) -> vImage_Error](./vimagehorizontalsheard_cbcr16s%28_,_,_,_,_,_,_,_,_%29.md)
- [func vImageHorizontalShearD_CbCr16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](./vimagehorizontalsheard_cbcr16u%28_,_,_,_,_,_,_,_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagehorizontalshear_cbcr16s(_:_:_:_:_:_:_:_:_:))*