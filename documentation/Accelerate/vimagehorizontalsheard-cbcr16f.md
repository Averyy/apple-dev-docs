# vImageHorizontalShearD_CbCr16F(_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Performs a double-precision horizontal shear on a region of interest within a floating-point 16-bit-per-channel, 2-channel interleaved image.

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
func vImageHorizontalShearD_CbCr16F(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ xTranslate: Double, _ shearSlope: Double, _ filter: ResamplingFilter!, _ backColor: UnsafePointer<UInt16>!, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes described in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

This function uses a resampling filter that you specify to shear, resize, and translate an image in one dimension. Use the resampling filter’s scale property to resize the image and the translate parameter to adjust the position of the destination image. The function transforms as much of the source image as it needs to fill the destination buffer. Therefore, it can transform pixels outside the region of interest.

This function doesn’t work in place — that is, the source and destination buffers must point to different memory.

## Parameters

- `src`: A pointer to a vImage buffer structure that contains the source image.
- `dest`: This parameter also specifies the size of the region of interest within the source image. The region of interest has the same height and width as the destination image buffer.
- `srcOffsetToROI_X`: The horizontal offset, in pixels, from the upper-left pixel of the region of interest within the source image.
- `srcOffsetToROI_Y`: The vertical offset, in pixels, from the upper-left pixel of the region of interest within the source image.
- `xTranslate`: A translation value for the horizontal direction.
- `shearSlope`: The slope of the front edge of the sheared image, measured in a clockwise direction.
- `filter`: The resampling filter that the function uses. For more information, see  .
- `backColor`: A background color. If you set the   flag, pass a pixel value.
- `flags`: If you want vImage to use faster but lower-precision internal arithmetic, set the   flag.

## See Also

- [Applying geometric transforms to images](applying-geometric-transforms-to-images.md)
  Reflect, shear, rotate, and scale image buffers using vImage.
- [func vImageHorizontalShearD_Planar16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, Pixel_16F, vImage_Flags) -> vImage_Error](vimagehorizontalsheard_planar16f(_:_:_:_:_:_:_:_:_:).md)
  Performs a double-precision horizontal shear on a region of interest within a floating-point 16-bit planar image.
- [func vImageHorizontalShearD_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimagehorizontalsheard_argb16u(_:_:_:_:_:_:_:_:_:).md)
  Performs a double-precision horizontal shear on a region of interest within an unsigned 16-bit-per-channel, 4-channel interleaved image.
- [func vImageHorizontalShearD_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<Int16>!, vImage_Flags) -> vImage_Error](vimagehorizontalsheard_argb16s(_:_:_:_:_:_:_:_:_:).md)
  Performs a double-precision horizontal shear on a region of interest within a signed 16-bit-per-channel, 4-channel interleaved image.
- [func vImageHorizontalShearD_ARGB16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimagehorizontalsheard_argb16f(_:_:_:_:_:_:_:_:_:).md)
  Performs a double-precision horizontal shear on a region of interest within a floating-point 16-bit-per-channel, 4-channel interleaved image.
- [func vImageHorizontalShearD_CbCr16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<Int16>!, vImage_Flags) -> vImage_Error](vimagehorizontalsheard_cbcr16s(_:_:_:_:_:_:_:_:_:).md)
- [func vImageHorizontalShearD_CbCr16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimagehorizontalsheard_cbcr16u(_:_:_:_:_:_:_:_:_:).md)
- [func vImageHorizontalShear_CbCr16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, UnsafePointer<Int16>!, vImage_Flags) -> vImage_Error](vimagehorizontalshear_cbcr16s(_:_:_:_:_:_:_:_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagehorizontalsheard_cbcr16f(_:_:_:_:_:_:_:_:_:))*