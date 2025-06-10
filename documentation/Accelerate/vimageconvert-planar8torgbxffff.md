# vImageConvert_Planar8ToRGBXFFFF

**Framework**: Accelerate  
**Kind**: macro

Interleaves three 8-bit planar buffers into a floating-point 32-bit-per-channel, 4-channel interleaved RGBX buffer with the specified constant alpha value.

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
#define vImageConvert_Planar8ToRGBXFFFF(_red, _green, _blue, _alpha, _dest, _maxFloat, _minFloat, _flags)
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The source and destination buffers must have the same height and width.

## Parameters

- `_red`: The source vImage buffer that contains the red channel.
- `_green`: The source vImage buffer that contains the green channel.
- `_blue`: The source vImage buffer that contains the blue channel.
- `_alpha`: The constant destination alpha value.
- `_dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `_maxFloat`: The maximum pixel value for the destination image.
- `_minFloat`: The minimum pixel value for the destination image.
- `_flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageConvert_Planar8toRGB565(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planar8torgb565(_:_:_:_:_:).md)
  Interleaves three 8-bit planar buffers into an RGB565 3-channel interleaved buffer.
- [func vImageConvert_Planar8toRGB888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planar8torgb888(_:_:_:_:_:).md)
  Interleaves three 8-bit planar buffers into an 8-bit-per-channel, 3-channel interleaved buffer.
- [func vImageConvert_Planar8ToXRGB8888(Pixel_8, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planar8toxrgb8888(_:_:_:_:_:_:).md)
  Interleaves three 8-bit planar buffers into an 8-bit-per-channel, 4-channel interleaved XRGB buffer with the specified constant alpha value.
- [vImageConvert_Planar8ToRGBX8888](vimageconvert_planar8torgbx8888.md)
  Interleaves three 8-bit planar buffers into an 8-bit-per-channel, 4-channel interleaved RGBX buffer with the specified constant alpha value.
- [func vImageConvert_Planar8ToBGRX8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_8, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planar8tobgrx8888(_:_:_:_:_:_:).md)
  Interleaves three 8-bit planar buffers into an 8-bit-per-channel, 4-channel interleaved BGRX buffer with the specified constant alpha value.
- [func vImageConvert_Planar8ToXRGBFFFF(Pixel_F, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>!, UnsafePointer<Float>!, vImage_Flags) -> vImage_Error](vimageconvert_planar8toxrgbffff(_:_:_:_:_:_:_:_:).md)
  Interleaves three 8-bit planar buffers into a floating-point 32-bit-per-channel, 4-channel interleaved XRGB buffer with the specified constant alpha value.
- [func vImageConvert_Planar8ToBGRXFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_F, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>!, UnsafePointer<Float>!, vImage_Flags) -> vImage_Error](vimageconvert_planar8tobgrxffff(_:_:_:_:_:_:_:_:).md)
  Interleaves three 8-bit planar buffers into a floating-point 32-bit-per-channel, 4-channel interleaved BGRX buffer with the specified constant alpha value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_planar8torgbxffff)*