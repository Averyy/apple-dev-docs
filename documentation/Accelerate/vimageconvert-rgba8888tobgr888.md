# vImageConvert_RGBA8888toBGR888

**Framework**: Accelerate  
**Kind**: macro

Removes the alpha channel from an 8-bit-per-channel RGBA buffer to produce an 8-bit-per-channel BGR result.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
#define vImageConvert_RGBA8888toBGR888(_rgbaSrc, _bgrDest, _flags)
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

This function copies the red, green, and blue source channels to the destination buffer.

## Parameters

- `_rgbaSrc`: The source vImage buffer.
- `_bgrDest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `_flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageConvert_ARGB8888toRGB888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_argb8888torgb888(_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel ARGB buffer to produce an 8-bit-per-channel RGB result.
- [func vImageConvert_RGBA8888toRGB888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_rgba8888torgb888(_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel RGBA buffer to produce an 8-bit-per-channel RGB result.
- [func vImageConvert_BGRA8888toRGB888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_bgra8888torgb888(_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel BGRA buffer to produce an 8-bit-per-channel RGB result.
- [vImageConvert_BGRA8888toBGR888](vimageconvert_bgra8888tobgr888.md)
  Removes the alpha channel from an 8-bit-per-channel BGRA buffer to produce an 8-bit-per-channel BGR result.
- [func vImageConvert_ARGB8888toRGB565(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_argb8888torgb565(_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel ARGB buffer to produce an RGB565 result.
- [func vImageConvert_ARGB8888toRGB565_dithered(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Int32, vImage_Flags) -> vImage_Error](vimageconvert_argb8888torgb565_dithered(_:_:_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel ARGB buffer using the specified dithering algorithm to produce an RGB565 result.
- [func vImageConvert_BGRA8888toRGB565(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_bgra8888torgb565(_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel RGBA buffer to produce an RGB565 result.
- [func vImageConvert_BGRA8888toRGB565_dithered(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Int32, vImage_Flags) -> vImage_Error](vimageconvert_bgra8888torgb565_dithered(_:_:_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel BGRA buffer using the specified dithering algorithm to produce an RGB565 result.
- [func vImageConvert_RGBA8888toRGB565_dithered(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Int32, vImage_Flags) -> vImage_Error](vimageconvert_rgba8888torgb565_dithered(_:_:_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel RGBA buffer using the specified dithering algorithm to produce an RGB565 result.
- [func vImageConvert_RGBA8888toRGB565(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_rgba8888torgb565(_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel RGBA buffer to produce an RGB565 result.
- [func vImageConvert_ARGB8888ToRGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, UInt8, UnsafePointer<Pixel_16U>, vImage_Flags) -> vImage_Error](vimageconvert_argb8888torgb16u(_:_:_:_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel ARGB buffer to produce an unsigned 16-bit-per-channel RGB result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_rgba8888tobgr888)*