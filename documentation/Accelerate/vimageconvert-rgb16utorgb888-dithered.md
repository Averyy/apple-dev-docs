# vImageConvert_RGB16UtoRGB888_dithered(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Converts an unsigned 16-bit-per-channel, 3-channel interleaved buffer to an 8-bit-per-channel, 3-channel interleaved buffer using the specified dithering algorithm.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func vImageConvert_RGB16UtoRGB888_dithered(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ dither: Int32, _ flags: vImage_Flags) -> vImage_Error
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
- `dither`: The dithering algorithm.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](kvimagedonottile.md); otherwise, pass [`kvImageNoFlags`](kvimagenoflags.md).

## See Also

- [Improving the quality of quantized images with dithering](improving-the-quality-of-quantized-images-with-dithering.md)
  Apply dithering to simulate colors that are unavailable in reduced bit depths.
- [func vImageConvert_ARGB16UToARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, UInt8, UnsafePointer<UInt8>, vImage_Flags) -> vImage_Error](vimageconvert_argb16utoargb8888(_:_:_:_:_:_:).md)
  Converts an unsigned 16-bit-per-channel, 4-channel interleaved buffer to an 8-bit-per-channel, 4-channel interleaved buffer.
- [func vImageConvert_ARGB16UtoARGB8888_dithered(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Int32, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb16utoargb8888_dithered(_:_:_:_:_:).md)
  Converts an unsigned 16-bit-per-channel, 4-channel interleaved buffer to an 8-bit-per-channel, 4-channel interleaved buffer using the specified dithering algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_rgb16utorgb888_dithered(_:_:_:_:))*