# vImageConvert_BGRA8888toRGB565_dithered(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Removes the alpha channel from an 8-bit-per-channel BGRA buffer using the specified dithering algorithm to produce an RGB565 result.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 7.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageConvert_BGRA8888toRGB565_dithered(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutableRawPointer!, _ dither: Int32, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, a negative value indicates one of the error codes that [`Data Types and Constants`](data-types-and-constants.md) describes, and a positive value indicates the required size for the temporary buffer.

#### Discussion

This function supports the following dithering algorithms:

- **[`kvImageConvert_DitherOrdered`](kvimageconvert_ditherordered.md)**: Adds precomputed blue noise to the source image before it rounds the input values to the nearest representable value in the destination format. The vImage conversion functions support uniform and Gaussian noise by including [`kvImageConvert_OrderedUniformBlue`](kvimageconvert_ordereduniformblue.md) and [`kvImageConvert_OrderedGaussianBlue`](kvimageconvert_orderedgaussianblue.md), respectively.
- **[`kvImageConvert_DitherOrderedReproducible`](kvimageconvert_ditherorderedreproducible.md)**: Returns the same result as [`kvImageConvert_DitherOrdered`](kvimageconvert_ditherordered.md), but uses the same offset into the blue noise for each call.

##### Optimize Performance with Temporary Buffers

This function uses a multiple-pass algorithm that saves intermediate pixel values between passes. In some cases, the destination buffer may not be large enough to store that intermediate data, so the operation requires additional storage.

Pass `nil` to the `tempBuffer` parameter to have vImage create and manage this temporary storage for you.

In cases where your code calls the function frequently (for example, when processing video), create and manage this temporary buffer yourself and reuse it across function calls. Reusing a buffer avoids vImage allocating the temporary storage with each call.

To use your own temporary buffer, first call the function with the same values for all other parameters that you intend to use for subsequent calls. In addition, pass the `kvImageGetTempBufferSize` flag. The `kvImageGetTempBufferSize` instructs the function not to perform any processing, and to return a positive value that represents the minimum size, in bytes, of the temporary buffer. A negative return value represents an error.

After you allocate the memory for the temporary buffer, pass that to the `tempBuffer` parameter for subsequent calls to the function, and don’t pass the `kvImageGetTempBufferSize` flag.

You can use the same workspace memory for a group of images that are different sizes. To do this, create a vImage buffer structure with a size that shares the maximum width and maximum height of the images that you’re working with. For example, to create a workspace memory that’s suitable for 4x4, 5x4, and 4x5 images, pass a buffer with the size 5x5.

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the [`height`](vimage_buffer/height.md), [`width`](vimage_buffer/width.md), and [`rowBytes`](vimage_buffer/rowbytes.md) fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `tempBuffer`: A pointer to workspace memory the function uses as it operates on an image. Pass `nil` to instruct the function to allocate, use, and then free its own temporary buffer.
- `dither`: The dithering algorithm.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](kvimagedonottile.md); otherwise, pass [`kvImageNoFlags`](kvimagenoflags.md). To instruct the function to return the minimum size of the workspace memory, set the [`kvImageGetTempBufferSize`](kvimagegettempbuffersize.md) flag.

## See Also

- [Improving the quality of quantized images with dithering](improving-the-quality-of-quantized-images-with-dithering.md)
  Apply dithering to simulate colors that are unavailable in reduced bit depths.
- [func vImageConvert_ARGB8888toRGB888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_argb8888torgb888(_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel ARGB buffer to produce an 8-bit-per-channel RGB result.
- [func vImageConvert_RGBA8888toRGB888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_rgba8888torgb888(_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel RGBA buffer to produce an 8-bit-per-channel RGB result.
- [func vImageConvert_BGRA8888toRGB888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_bgra8888torgb888(_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel BGRA buffer to produce an 8-bit-per-channel RGB result.
- [func vImageConvert_ARGB8888toRGB565(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_argb8888torgb565(_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel ARGB buffer to produce an RGB565 result.
- [func vImageConvert_ARGB8888toRGB565_dithered(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Int32, vImage_Flags) -> vImage_Error](vimageconvert_argb8888torgb565_dithered(_:_:_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel ARGB buffer using the specified dithering algorithm to produce an RGB565 result.
- [func vImageConvert_BGRA8888toRGB565(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_bgra8888torgb565(_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel RGBA buffer to produce an RGB565 result.
- [func vImageConvert_RGBA8888toRGB565_dithered(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Int32, vImage_Flags) -> vImage_Error](vimageconvert_rgba8888torgb565_dithered(_:_:_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel RGBA buffer using the specified dithering algorithm to produce an RGB565 result.
- [func vImageConvert_RGBA8888toRGB565(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_rgba8888torgb565(_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel RGBA buffer to produce an RGB565 result.
- [func vImageConvert_ARGB8888ToRGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, UInt8, UnsafePointer<Pixel_16U>, vImage_Flags) -> vImage_Error](vimageconvert_argb8888torgb16u(_:_:_:_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel ARGB buffer to produce an unsigned 16-bit-per-channel RGB result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_bgra8888torgb565_dithered(_:_:_:_:_:))*