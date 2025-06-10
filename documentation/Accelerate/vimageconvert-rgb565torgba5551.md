# vImageConvert_RGB565toRGBA5551(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Combines an RGB565 3-channel RGB buffer and a constant alpha value to produce a 4-channel RGBA5551 buffer.

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
func vImageConvert_RGB565toRGBA5551(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ dither: Int32, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

This function supports the following dithering algorithms:

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `dither`: The dithering algorithm.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [Improving the quality of quantized images with dithering](improving-the-quality-of-quantized-images-with-dithering.md)
  Apply dithering to simulate colors that are unavailable in reduced bit depths.
- [func vImageConvert_RGB565toARGB8888(Pixel_8, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_rgb565toargb8888(_:_:_:_:).md)
  Combines an RGB565 3-channel RGB buffer and a constant alpha value to produce an 8-bit-per-channel, 4-channel ARGB buffer.
- [func vImageConvert_RGB565toBGRA8888(Pixel_8, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_rgb565tobgra8888(_:_:_:_:).md)
  Combines an RGB565 3-channel RGB buffer and a constant alpha value to produce an 8-bit-per-channel, 4-channel BGRA buffer.
- [func vImageConvert_RGB565toRGBA8888(Pixel_8, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_rgb565torgba8888(_:_:_:_:).md)
  Combines an RGB565 3-channel RGB buffer and a constant alpha value to produce an 8-bit-per-channel, 4-channel RGBA buffer.
- [func vImageConvert_RGB565toARGB1555(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Int32, vImage_Flags) -> vImage_Error](vimageconvert_rgb565toargb1555(_:_:_:_:).md)
  Combines an RGB565 3-channel RGB buffer and a constant alpha value to produce a 4-channel ARGB1555 buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_rgb565torgba5551(_:_:_:_:))*