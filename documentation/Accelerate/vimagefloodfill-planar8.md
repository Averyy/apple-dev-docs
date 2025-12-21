# vImageFloodFill_Planar8(_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies a flood-fill operation to an 8-bit planar image.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func vImageFloodFill_Planar8(_ srcDest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutableRawPointer!, _ seedX: vImagePixelCount, _ seedY: vImagePixelCount, _ newValue: Pixel_8, _ connectivity: Int32, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, a negative value indicates one of the error codes that [`Data Types and Constants`](data-types-and-constants.md) describes, and a positive value indicates the required size for the temporary buffer.

#### Discussion

The flood-fill function sets all pixels that are neighboring and identical to the seed pixel to a new color. The operation continues until it reaches the image boundary or until it sets all pixels within the connected component to the new value.

##### Optimize Performance with Temporary Buffers

This function uses a multiple-pass algorithm that saves intermediate pixel values between passes. In some cases, the destination buffer may not be large enough to store that intermediate data, so the operation requires additional storage.

Pass `nil` to the `tempBuffer` parameter to have vImage create and manage this temporary storage for you.

In cases where your code calls the function frequently (for example, when processing video), create and manage this temporary buffer yourself and reuse it across function calls. Reusing a buffer avoids vImage allocating the temporary storage with each call.

To use your own temporary buffer, first call the function with the same values for all other parameters that you intend to use for subsequent calls. In addition, pass the `kvImageGetTempBufferSize` flag. The `kvImageGetTempBufferSize` instructs the function not to perform any processing, and to return a positive value that represents the minimum size, in bytes, of the temporary buffer. A negative return value represents an error.

After you allocate the memory for the temporary buffer, pass that to the `tempBuffer` parameter for subsequent calls to the function, and don’t pass the `kvImageGetTempBufferSize` flag.

## Parameters

- `srcDest`: A pointer to a vImage buffer structure that contains the source image and receives the destination image. This function always works in place, that is, the input and the output point to the same memory.
- `tempBuffer`: A pointer to workspace memory the function uses as it operates on an image. Pass   to instruct the function to allocate, use, and then free its own temporary buffer.
- `seedX`: The x-coordinate that defines the position of the seed pixel inside the connected component.
- `seedY`: The y-coordinate that defines the position of the seed pixel inside the connected component.
- `newValue`: The new pixel value that overwrites the pixels in the connected component.
- `connectivity`: An integer that specifies which pixels the operation includes as neighbors. Pass either   or  . The four-connected neighborhood of a pixel are the pixels to the left and right, and those above and below. The eight-connected neighborhood also includes the pixels on the four diagonals.
- `flags`: To instruct the function to return the minimum size of the workspace memory, set the   flag.

## See Also

- [Applying flood fills to an image](applying-flood-fills-to-an-image.md)
  Fill consistently colored connected parts of an image with a new color.
- [func vImageFloodFill_Planar16U(UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, Pixel_16U, Int32, vImage_Flags) -> vImage_Error](vimagefloodfill_planar16u(_:_:_:_:_:_:_:).md)
  Applies a flood fill-operation to an unsigned 16-bit planar image.
- [func vImageFloodFill_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, UnsafeMutablePointer<UInt8>!, Int32, vImage_Flags) -> vImage_Error](vimagefloodfill_argb8888(_:_:_:_:_:_:_:).md)
  Applies a flood-fill operation to an 8-bit-per-channel, four-channel interleaved image.
- [func vImageFloodFill_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, UnsafeMutablePointer<UInt16>!, Int32, vImage_Flags) -> vImage_Error](vimagefloodfill_argb16u(_:_:_:_:_:_:_:).md)
  Applies a flood-fill operation to an unsigned 16-bit-per-channel, four-channel interleaved image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagefloodfill_planar8(_:_:_:_:_:_:_:))*