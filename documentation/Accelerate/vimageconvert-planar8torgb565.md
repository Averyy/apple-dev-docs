# vImageConvert_Planar8toRGB565(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Interleaves three 8-bit planar buffers into an RGB565 3-channel interleaved buffer.

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
func vImageConvert_Planar8toRGB565(_ srcR: UnsafePointer<vImage_Buffer>, _ srcG: UnsafePointer<vImage_Buffer>, _ srcB: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The function uses the following calculation to perform the conversion:

```objc
    uint32_t red   = (8bitRedChannel   * (31*2) + 255) / (255*2)
    uint32_t green = (8bitGreenChannel * 63 + 127) / 255
    uint32_t blue  = (8bitBlueChannel  * 31 + 127) / 255
    uint16_t RGB565pixel = (red << 11) | (green <<  5) | blue
```

## Parameters

- `srcR`: The source vImage buffer that contains the red channel.
- `srcG`: The source vImage buffer that contains the green channel.
- `srcB`: The source vImage buffer that contains the blue channel.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageConvert_Planar8toRGB888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planar8torgb888(_:_:_:_:_:).md)
  Interleaves three 8-bit planar buffers into an 8-bit-per-channel, 3-channel interleaved buffer.
- [func vImageConvert_Planar8ToXRGB8888(Pixel_8, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planar8toxrgb8888(_:_:_:_:_:_:).md)
  Interleaves three 8-bit planar buffers into an 8-bit-per-channel, 4-channel interleaved XRGB buffer with the specified constant alpha value.
- [func vImageConvert_Planar8ToBGRX8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_8, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planar8tobgrx8888(_:_:_:_:_:_:).md)
  Interleaves three 8-bit planar buffers into an 8-bit-per-channel, 4-channel interleaved BGRX buffer with the specified constant alpha value.
- [func vImageConvert_Planar8ToXRGBFFFF(Pixel_F, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>!, UnsafePointer<Float>!, vImage_Flags) -> vImage_Error](vimageconvert_planar8toxrgbffff(_:_:_:_:_:_:_:_:).md)
  Interleaves three 8-bit planar buffers into a floating-point 32-bit-per-channel, 4-channel interleaved XRGB buffer with the specified constant alpha value.
- [func vImageConvert_Planar8ToBGRXFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_F, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>!, UnsafePointer<Float>!, vImage_Flags) -> vImage_Error](vimageconvert_planar8tobgrxffff(_:_:_:_:_:_:_:_:).md)
  Interleaves three 8-bit planar buffers into a floating-point 32-bit-per-channel, 4-channel interleaved BGRX buffer with the specified constant alpha value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_planar8torgb565(_:_:_:_:_:))*