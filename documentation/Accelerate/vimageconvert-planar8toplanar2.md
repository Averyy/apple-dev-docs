# vImageConvert_Planar8toPlanar2(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Converts an 8-bit planar buffer to a 2-bit planar buffer.

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
func vImageConvert_Planar8toPlanar2(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutableRawPointer!, _ dither: Int32, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, a negative value indicates one of the error codes that [`Data Types and Constants`](data-types-and-constants.md) describes, and a positive value indicates the required size for the temporary buffer.

#### Discussion

This function supports the following dithering algorithms:

##### Optimize Performance with Temporary Buffers

This function uses a multiple-pass algorithm that saves intermediate pixel values between passes. In some cases, the destination buffer may not be large enough to store that intermediate data, so the operation requires additional storage.

Pass `nil` to the `tempBuffer` parameter to have vImage create and manage this temporary storage for you.

In cases where your code calls the function frequently (for example, when processing video), create and manage this temporary buffer yourself and reuse it across function calls. Reusing a buffer avoids vImage allocating the temporary storage with each call.

To use your own temporary buffer, first call the function with the same values for all other parameters that you intend to use for subsequent calls. In addition, pass the `kvImageGetTempBufferSize` flag. The `kvImageGetTempBufferSize` instructs the function not to perform any processing, and to return a positive value that represents the minimum size, in bytes, of the temporary buffer. A negative return value represents an error.

After you allocate the memory for the temporary buffer, pass that to the `tempBuffer` parameter for subsequent calls to the function, and don’t pass the `kvImageGetTempBufferSize` flag.

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `tempBuffer`: A pointer to workspace memory the function uses as it operates on an image. Pass   to instruct the function to allocate, use, and then free its own temporary buffer.
- `dither`: The dithering algorithm.
- `flags`: To instruct the function to return the minimum size of the workspace memory, set the   flag.

## See Also

- [Improving the quality of quantized images with dithering](improving-the-quality-of-quantized-images-with-dithering.md)
  Apply dithering to simulate colors that are unavailable in reduced bit depths.
- [func vImageConvert_Planar8toPlanar1(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Int32, vImage_Flags) -> vImage_Error](vimageconvert_planar8toplanar1(_:_:_:_:_:).md)
  Converts an 8-bit planar buffer to a 1-bit planar buffer.
- [func vImageConvert_Planar8toPlanar4(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Int32, vImage_Flags) -> vImage_Error](vimageconvert_planar8toplanar4(_:_:_:_:_:).md)
  Converts an 8-bit planar buffer to a 4-bit planar buffer.
- [func vImageConvert_Planar8toIndexed1(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafeMutablePointer<Pixel_8>, Int32, vImage_Flags) -> vImage_Error](vimageconvert_planar8toindexed1(_:_:_:_:_:_:).md)
  Converts an 8-bit planar buffer to an indexed 1-bit planar buffer.
- [func vImageConvert_Planar8toIndexed2(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafeMutablePointer<Pixel_8>, Int32, vImage_Flags) -> vImage_Error](vimageconvert_planar8toindexed2(_:_:_:_:_:_:).md)
  Converts an 8-bit planar buffer to an indexed 2-bit planar buffer.
- [func vImageConvert_Planar8toIndexed4(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafeMutablePointer<Pixel_8>, Int32, vImage_Flags) -> vImage_Error](vimageconvert_planar8toindexed4(_:_:_:_:_:_:).md)
  Converts an 8-bit planar buffer to an indexed 4-bit planar buffer.
- [func vImageConvert_Planar8To16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planar8to16u(_:_:_:).md)
  Converts an 8-bit planar buffer to an unsigned 16-bit planar buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_planar8toplanar2(_:_:_:_:_:))*