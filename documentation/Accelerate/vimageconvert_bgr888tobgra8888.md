# vImageConvert_BGR888toBGRA8888

**Framework**: Accelerate  
**Kind**: macro  
**Role**: Macro

Combines an 8-bit-per-channel, 3-channel BGR buffer and either an 8-bit alpha buffer or constant alpha value to produce a BGRA result.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
#define vImageConvert_BGR888toBGRA8888(_bgrSrc, _aSrc, _alpha, _bgraDest, _premultiply, _flags)
```

#### Return Value

[`kvImageNoError`](./kvimagenoerror.md); otherwise, one of the error codes in [Data Types and Constants](./data-types-and-constants.md).

#### Discussion

If you specify `premultiply` as `true`, the function uses the following calculation to perform the conversion:

```objc
 b = (a * b + 127) / 255
 g = (a * g + 127) / 255
 r = (a * r + 127) / 255
```

## Parameters

- `_bgrSrc`: The source vImage buffer that contains the blue, green, and red channels.
- `_aSrc`: The source vImage buffer that contains the alpha channel. Set this value to `nil` to specify that the function sets the destination alpha as the constant destination alpha value.
- `_alpha`: The constant destination alpha value. The function ignores this paramater if the `aSrc` parameter isn’t `nil`.
- `_bgraDest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the [`height`](./vimage_buffer/height.md), [`width`](./vimage_buffer/width.md), and [`rowBytes`](./vimage_buffer/rowbytes.md) fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `_premultiply`: A Boolean value that specifes whether the function premultiplies the color channels by the alpha channel.
- `_flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](./kvimagedonottile.md); otherwise, pass [`kvImageNoFlags`](./kvimagenoflags.md).

## See Also

### Conversion from 8-bit-per-channel, 3-channel interleaved buffers
- [func vImageConvert_RGB888toARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>!, Pixel_8, UnsafePointer<vImage_Buffer>, Bool, vImage_Flags) -> vImage_Error](./vimageconvert_rgb888toargb8888%28_,_,_,_,_,_%29.md)
  Combines an 8-bit-per-channel, 3-channel RGB buffer and either an 8-bit alpha buffer or constant alpha value to produce an ARGB result.
- [func vImageConvert_RGB888toBGRA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>!, Pixel_8, UnsafePointer<vImage_Buffer>, Bool, vImage_Flags) -> vImage_Error](./vimageconvert_rgb888tobgra8888%28_,_,_,_,_,_%29.md)
  Combines an 8-bit-per-channel, 3-channel RGB buffer and either an 8-bit alpha buffer or constant alpha value to produce a BGRA result.
- [vImageConvert_BGR888toRGBA8888](./vimageconvert_bgr888torgba8888.md)
  Combines an 8-bit-per-channel, 3-channel BGR buffer and either an 8-bit alpha buffer or constant alpha value to produce an RGBA result.
- [func vImageConvert_RGB888toRGBA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>!, Pixel_8, UnsafePointer<vImage_Buffer>, Bool, vImage_Flags) -> vImage_Error](./vimageconvert_rgb888torgba8888%28_,_,_,_,_,_%29.md)
  Combines an 8-bit-per-channel, 3-channel RGB buffer and either an 8-bit alpha buffer or constant alpha value to produce an RGBA result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_bgr888tobgra8888)*