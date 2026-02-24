# vImageConvert_PlanarFtoPlanar8_dithered(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Converts a floating-point 32-bit planar buffer to an 8-bit planar buffer using the specified dithering algorithm.

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
func vImageConvert_PlanarFtoPlanar8_dithered(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ maxFloat: Pixel_F, _ minFloat: Pixel_F, _ dither: Int32, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

This function supports the following dithering algorithms:

- **[`kvImageConvert_DitherNone`](kvimageconvert_dithernone.md)**: Doesn’t apply any dithering. This algorithm rounds the input values to the nearest representable value in the destination format.
- **[`kvImageConvert_DitherOrdered`](kvimageconvert_ditherordered.md)**: Adds precomputed blue noise to the source image before it rounds the input values to the nearest representable value in the destination format. The vImage conversion functions support uniform and Gaussian noise by including [`kvImageConvert_OrderedUniformBlue`](kvimageconvert_ordereduniformblue.md) and [`kvImageConvert_OrderedGaussianBlue`](kvimageconvert_orderedgaussianblue.md), respectively.
- **[`kvImageConvert_DitherOrderedReproducible`](kvimageconvert_ditherorderedreproducible.md)**: Returns the same result as [`kvImageConvert_DitherOrdered`](kvimageconvert_ditherordered.md), but uses the same offset into the blue noise for each call.
- **[`kvImageConvert_DitherFloydSteinberg`](kvimageconvert_ditherfloydsteinberg.md)**: Applies Floyd-Steinberg dithering to the image.
- **[`kvImageConvert_DitherAtkinson`](kvimageconvert_ditheratkinson.md)**: Applies Atkinson dithering to the image.

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the [`height`](vimage_buffer/height.md), [`width`](vimage_buffer/width.md), and [`rowBytes`](vimage_buffer/rowbytes.md) fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `maxFloat`: The maximum source pixel value.
- `minFloat`: The minimum source pixel value.
- `dither`: The dithering algorithm.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](kvimagedonottile.md); otherwise, pass [`kvImageNoFlags`](kvimagenoflags.md).

## See Also

- [Improving the quality of quantized images with dithering](improving-the-quality-of-quantized-images-with-dithering.md)
  Apply dithering to simulate colors that are unavailable in reduced bit depths.
- [func vImageConvert_PlanarFtoPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error](vimageconvert_planarftoplanar8(_:_:_:_:_:).md)
  Converts a floating-point 32-bit planar buffer to an 8-bit planar buffer.
- [func vImageConvert_FTo16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Float, Float, vImage_Flags) -> vImage_Error](vimageconvert_fto16s(_:_:_:_:_:).md)
  Converts a floating-point 32-bit planar buffer to a signed 16-bit planar buffer.
- [func vImageConvert_FTo16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Float, Float, vImage_Flags) -> vImage_Error](vimageconvert_fto16u(_:_:_:_:_:).md)
  Converts a floating-point 32-bit planar buffer to an unsigned 16-bit planar buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_planarftoplanar8_dithered(_:_:_:_:_:_:))*