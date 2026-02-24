# vImageHorizontalShearD_Planar8(_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Performs a double-precision horizontal shear on a region of interest within an 8-bit planar image.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 6.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageHorizontalShearD_Planar8(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ xTranslate: Double, _ shearSlope: Double, _ filter: ResamplingFilter!, _ backColor: Pixel_8, _ flags: vImage_Flags) -> vImage_Error
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
- `xTranslate`: A translation value for the horizontal direction.
- `shearSlope`: The slope of the front edge of the sheared image, measured in a clockwise direction.
- `filter`: The resampling filter that the function uses. For more information, see [`Reducing artifacts with custom resampling filters`](reducing-artifacts-with-custom-resampling-filters.md).
- `backColor`: A background color. If you set the `kvImageBackgroundColorFill` flag, pass a pixel value.
- `flags`: The options to use when applying the transform. To specify how vImage handles pixel locations beyond the edge of the source image, set one of the following flags: [`kvImageBackgroundColorFill`](kvimagebackgroundcolorfill.md) or [`kvImageEdgeExtend`](kvimageedgeextend.md). If you want vImage to use a higher quality but a slower resampling filter, set the [`kvImageHighQualityResampling`](kvimagehighqualityresampling.md) flag. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](kvimagedonottile.md). This function ignores the [`kvImageLeaveAlphaUnchanged`](kvimageleavealphaunchanged.md) flag.

## See Also

- [Applying geometric transforms to images](applying-geometric-transforms-to-images.md)
  Reflect, shear, rotate, and scale image buffers using vImage.
- [func vImageHorizontalShearD_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, Double, Double, ResamplingFilter!, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimagehorizontalsheard_argb8888(_:_:_:_:_:_:_:_:_:).md)
  Performs a double-precision horizontal shear on a region of interest within an 8-bit-per-channel, 4-channel interleaved image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagehorizontalsheard_planar8(_:_:_:_:_:_:_:_:_:))*