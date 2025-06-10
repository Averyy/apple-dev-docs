# vImageConvert_ARGB8888toRGB888(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Removes the alpha channel from an 8-bit-per-channel ARGB buffer to produce an 8-bit-per-channel RGB result.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 5.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageConvert_ARGB8888toRGB888(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

This function copies the red, green, and blue source channels to the destination buffer.

##### Parameters

## See Also

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
- [func vImageConvert_BGRA8888toRGB565_dithered(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Int32, vImage_Flags) -> vImage_Error](vimageconvert_bgra8888torgb565_dithered(_:_:_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel BGRA buffer using the specified dithering algorithm to produce an RGB565 result.
- [func vImageConvert_RGBA8888toRGB565_dithered(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Int32, vImage_Flags) -> vImage_Error](vimageconvert_rgba8888torgb565_dithered(_:_:_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel RGBA buffer using the specified dithering algorithm to produce an RGB565 result.
- [func vImageConvert_RGBA8888toRGB565(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_rgba8888torgb565(_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel RGBA buffer to produce an RGB565 result.
- [func vImageConvert_ARGB8888ToRGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, UInt8, UnsafePointer<Pixel_16U>, vImage_Flags) -> vImage_Error](vimageconvert_argb8888torgb16u(_:_:_:_:_:_:).md)
  Removes the alpha channel from an 8-bit-per-channel ARGB buffer to produce an unsigned 16-bit-per-channel RGB result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_argb8888torgb888(_:_:_:))*