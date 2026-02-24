# vImageVerticalShear_Planar16S(_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Performs a single-precision vertical shear on a region of interest within a signed 16-bit planar image.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 8.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageVerticalShear_Planar16S(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ yTranslate: Float, _ shearSlope: Float, _ filter: ResamplingFilter!, _ backColor: Pixel_16S, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes that [`Data Types and Constants`](data-types-and-constants.md) describes.

#### Discussion

This function uses a resampling filter that you specify to shear, resize, and translate an image in one dimension. Use the resampling filter’s scale property to resize the image and the translate parameter to adjust the position of the destination image. The function transforms as much of the source image as it needs to fill the destination buffer. Therefore, it can transform pixels outside the region of interest.

This function doesn’t work in place — that is, the source and destination buffers need to point to different memory.

## Parameters

- `src`: A pointer to a vImage buffer structure that contains the source image.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the `height`, `width`, and `rowBytes` fields of this structure and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks. This parameter also specifies the size of the region of interest within the source image. The region of interest has the same height and width as the destination image buffer.
- `srcOffsetToROI_X`: The horizontal offset, in pixels, from the upper-left pixel of the region of interest within the source image.
- `srcOffsetToROI_Y`: The vertical offset, in pixels, from the upper-left pixel of the region of interest within the source image.
- `yTranslate`: A translation value for the vertical direction.
- `shearSlope`: The slope of the front edge of the sheared image, measured in a clockwise direction.
- `filter`: The resampling filter that the function uses. For more information, see [`Reducing artifacts with custom resampling filters`](reducing-artifacts-with-custom-resampling-filters.md).
- `backColor`: A background color. If you set the `kvImageBackgroundColorFill` flag, pass a pixel value.
- `flags`: The options to use when applying the transform. To specify how vImage handles pixel locations beyond the edge of the source image, set one of the following flags: [`kvImageBackgroundColorFill`](kvimagebackgroundcolorfill.md) or [`kvImageEdgeExtend`](kvimageedgeextend.md). If you want vImage to use a higher quality but a slower resampling filter, set the [`kvImageHighQualityResampling`](kvimagehighqualityresampling.md) flag. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](kvimagedonottile.md). This function ignores the [`kvImageLeaveAlphaUnchanged`](kvimageleavealphaunchanged.md) flag.

## See Also

- [Applying geometric transforms to images](applying-geometric-transforms-to-images.md)
  Reflect, shear, rotate, and scale image buffers using vImage.
- [func vImageVerticalShear_Planar16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, Pixel_16U, vImage_Flags) -> vImage_Error](vimageverticalshear_planar16u(_:_:_:_:_:_:_:_:_:).md)
  Performs a single-precision vertical shear on a region of interest within an unsigned 16-bit planar image.
- [func vImageVerticalShear_Planar16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, Pixel_16F, vImage_Flags) -> vImage_Error](vimageverticalshear_planar16f(_:_:_:_:_:_:_:_:_:).md)
  Performs a single-precision vertical shear on a region of interest within a floating-point 16-bit planar image.
- [func vImageVerticalShear_CbCr16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimageverticalshear_cbcr16u(_:_:_:_:_:_:_:_:_:).md)
  Performs a single-precision vertical shear on a region of interest within an unsigned 16-bit-per-channel, 2-channel interleaved image.
- [func vImageVerticalShear_CbCr16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimageverticalshear_cbcr16f(_:_:_:_:_:_:_:_:_:).md)
  Performs a single-precision vertical shear on a region of interest within a floating-point 16-bit-per-channel, 2-channel interleaved image.
- [func vImageVerticalShear_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimageverticalshear_argb16u(_:_:_:_:_:_:_:_:_:).md)
  Performs a single-precision vertical shear on a region of interest within an unsigned 16-bit-per-channel, 4-channel interleaved image.
- [func vImageVerticalShear_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, UnsafePointer<Int16>!, vImage_Flags) -> vImage_Error](vimageverticalshear_argb16s(_:_:_:_:_:_:_:_:_:).md)
  Performs a single-precision vertical shear on a region of interest within a signed 16-bit-per-channel, 4-channel interleaved image.
- [func vImageVerticalShear_ARGB16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Float, Float, ResamplingFilter!, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimageverticalshear_argb16f(_:_:_:_:_:_:_:_:_:).md)
  Performs a single-precision vertical shear on a region of interest within a floating-point 16-bit-per-channel, 4-channel interleaved image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageverticalshear_planar16s(_:_:_:_:_:_:_:_:_:))*