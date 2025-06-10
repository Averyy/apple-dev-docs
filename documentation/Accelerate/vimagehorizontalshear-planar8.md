# vImageHorizontalShear_Planar8(_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Performs a single-precision horizontal shear on a region of interest within an 8-bit planar image.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 5.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageHorizontalShear_Planar8(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ xTranslate: Float, _ shearSlope: Float, _ filter: ResamplingFilter!, _ backColor: Pixel_8, _ flags: vImage_Flags) -> vImage_Error
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
- `flags`: This function ignores the   flag.

## See Also

- [Applying geometric transforms to images](applying-geometric-transforms-to-images.md)
  Reflect, shear, rotate, and scale image buffers using vImage.
- [func vImageHorizontalShear_CbCr8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimagehorizontalshear_cbcr8(_:_:_:_:_:_:_:_:_:).md)
  Performs a single-precision horizontal shear on a region of interest within an 8-bit-per-channel, 2-channel interleaved image.
- [func vImageHorizontalShear_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimagehorizontalshear_argb8888(_:_:_:_:_:_:_:_:_:).md)
  Performs a single-precision horizontal shear on a region of interest within an 8-bit-per-channel, 4-channel interleaved image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagehorizontalshear_planar8(_:_:_:_:_:_:_:_:_:))*