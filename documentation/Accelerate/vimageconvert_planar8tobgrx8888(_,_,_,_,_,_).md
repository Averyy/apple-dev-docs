# vImageConvert_Planar8ToBGRX8888(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Interleaves three 8-bit planar buffers into an 8-bit-per-channel, 4-channel interleaved BGRX buffer with the specified constant alpha value.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 5.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageConvert_Planar8ToBGRX8888(_ blue: UnsafePointer<vImage_Buffer>, _ green: UnsafePointer<vImage_Buffer>, _ red: UnsafePointer<vImage_Buffer>, _ alpha: Pixel_8, _ dest: UnsafePointer<vImage_Buffer>, _ flags: vImage_Flags) -> vImage_Error
```

```c
vImage_Error vImageConvert_Planar8ToBGRX8888(const vImage_Buffer *blue, const vImage_Buffer *green, const vImage_Buffer *red, Pixel_8 alpha, const vImage_Buffer *dest, vImage_Flags flags);
```

## Return Value

[`kvImageNoError`](./kvimagenoerror.md); otherwise, one of the error codes in [Data Types and Constants](./data-types-and-constants.md).

## Discussion

The source and destination buffers need to have the same height and width.

## Parameters

- `blue`: The source vImage buffer that contains the blue channel.
- `green`: The source vImage buffer that contains the green channel.
- `red`: The source vImage buffer that contains the red channel.
- `alpha`: The constant destination alpha value.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the [`height`](./vimage_buffer/height.md), [`width`](./vimage_buffer/width.md), and [`rowBytes`](./vimage_buffer/rowbytes.md) fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](./kvimagedonottile.md); otherwise, pass [`kvImageNoFlags`](./kvimagenoflags.md).

## See Also

### Interleaving three unsigned 8-bit planar buffers
- [func vImageConvert_Planar8toRGB565(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](./vimageconvert_planar8torgb565%28_,_,_,_,_%29.md)
  Interleaves three 8-bit planar buffers into an RGB565 3-channel interleaved buffer.
- [func vImageConvert_Planar8toRGB888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](./vimageconvert_planar8torgb888%28_,_,_,_,_%29.md)
  Interleaves three 8-bit planar buffers into an 8-bit-per-channel, 3-channel interleaved buffer.
- [func vImageConvert_Planar8ToXRGB8888(Pixel_8, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](./vimageconvert_planar8toxrgb8888%28_,_,_,_,_,_%29.md)
  Interleaves three 8-bit planar buffers into an 8-bit-per-channel, 4-channel interleaved XRGB buffer with the specified constant alpha value.
- [func vImageConvert_Planar8ToXRGBFFFF(Pixel_F, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>!, UnsafePointer<Float>!, vImage_Flags) -> vImage_Error](./vimageconvert_planar8toxrgbffff%28_,_,_,_,_,_,_,_%29.md)
  Interleaves three 8-bit planar buffers into a floating-point 32-bit-per-channel, 4-channel interleaved XRGB buffer with the specified constant alpha value.
- [func vImageConvert_Planar8ToBGRXFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_F, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>!, UnsafePointer<Float>!, vImage_Flags) -> vImage_Error](./vimageconvert_planar8tobgrxffff%28_,_,_,_,_,_,_,_%29.md)
  Interleaves three 8-bit planar buffers into a floating-point 32-bit-per-channel, 4-channel interleaved BGRX buffer with the specified constant alpha value.
- [vImageConvert_Planar8ToRGBX8888](./vimageconvert_planar8torgbx8888.md)
  Interleaves three 8-bit planar buffers into an 8-bit-per-channel, 4-channel interleaved RGBX buffer with the specified constant alpha value.
- [vImageConvert_Planar8ToRGBXFFFF](./vimageconvert_planar8torgbxffff.md)
  Interleaves three 8-bit planar buffers into a floating-point 32-bit-per-channel, 4-channel interleaved RGBX buffer with the specified constant alpha value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_planar8tobgrx8888(_:_:_:_:_:_:))*