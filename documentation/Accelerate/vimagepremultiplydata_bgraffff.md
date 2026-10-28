# vImagePremultiplyData_BGRAFFFF

**Framework**: Accelerate  
**Kind**: macro  
**Role**: Macro

Transforms a floating-point 32-bit-per-channel, 4-channel BGRA buffer from nonpremultiplied alpha format to premultiplied alpha format.

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
#define vImagePremultiplyData_BGRAFFFF(_src, _dest, _flags)
```

## Return Value

[`kvImageNoError`](./kvimagenoerror.md); otherwise, one of the error codes in [Data Types and Constants](./data-types-and-constants.md).

## Discussion

This function multiplies color channels by the alpha channel using the following code:

```swift
float destColor = src * alpha;
float destAlpha = alpha;
```

## Parameters

- `_src`: The source vImage buffer.
- `_dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the [`height`](./vimage_buffer/height.md), [`width`](./vimage_buffer/width.md), and [`rowBytes`](./vimage_buffer/rowbytes.md) fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `_flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](./kvimagedonottile.md); otherwise, pass [`kvImageNoFlags`](./kvimagenoflags.md).

## See Also

### Related Documentation
- [Compositing images with alpha blending](./compositing-images-with-alpha-blending.md)
  Combine two images by using alpha blending to create a single output.
### Converting from unpremultiplied to premultiplied format
- [func vImagePremultiplyData_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](./vimagepremultiplydata_planar8%28_,_,_,_%29.md)
  Transforms an 8-bit planar buffer from nonpremultiplied alpha format to premultiplied alpha format.
- [func vImagePremultiplyData_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](./vimagepremultiplydata_planarf%28_,_,_,_%29.md)
  Transforms a 32-bit planar buffer from nonpremultiplied alpha format to premultiplied alpha format.
- [func vImagePremultiplyData_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](./vimagepremultiplydata_argb8888%28_,_,_%29.md)
  Transforms an 8-bit-per-channel, 4-channel ARGB buffer from nonpremultiplied alpha format to premultiplied alpha format.
- [func vImagePremultiplyData_RGBA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](./vimagepremultiplydata_rgba8888%28_,_,_%29.md)
  Transforms an 8-bit-per-channel, 4-channel RGBA buffer from nonpremultiplied alpha format to premultiplied alpha format.
- [vImagePremultiplyData_BGRA8888](./vimagepremultiplydata_bgra8888.md)
  Transforms an 8-bit-per-channel, 4-channel BGRA buffer from nonpremultiplied alpha format to premultiplied alpha format.
- [func vImagePremultiplyData_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](./vimagepremultiplydata_argb16u%28_,_,_%29.md)
  Transforms an unsigned 16-bit-per-channel, 4-channel ARGB buffer from nonpremultiplied alpha format to premultiplied alpha format.
- [func vImagePremultiplyData_RGBA16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](./vimagepremultiplydata_rgba16u%28_,_,_%29.md)
  Transforms an unsigned 16-bit-per-channel, 4-channel RGBA buffer from nonpremultiplied alpha format to premultiplied alpha format.
- [func vImagePremultiplyData_RGBA16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](./vimagepremultiplydata_rgba16f%28_,_,_%29.md)
  Transforms a floating-point 16-bit-per-channel, 4-channel RGBA buffer from nonpremultiplied alpha format to premultiplied alpha format.
- [func vImagePremultiplyData_ARGB16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](./vimagepremultiplydata_argb16q12%28_,_,_%29.md)
  Transforms a fixed-point 16-bit-per-channel, 4-channel ARGB buffer from nonpremultiplied alpha format to premultiplied alpha format.
- [func vImagePremultiplyData_RGBA16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](./vimagepremultiplydata_rgba16q12%28_,_,_%29.md)
  Transforms a fixed-point 16-bit-per-channel, 4-channel RGBA buffer from nonpremultiplied alpha format to premultiplied alpha format.
- [func vImagePremultiplyData_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](./vimagepremultiplydata_argbffff%28_,_,_%29.md)
  Transforms a floating-point 32-bit-per-channel, 4-channel ARGB buffer from nonpremultiplied alpha format to premultiplied alpha format.
- [func vImagePremultiplyData_RGBAFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](./vimagepremultiplydata_rgbaffff%28_,_,_%29.md)
  Transforms a floating-point 32-bit-per-channel, 4-channel ARGB buffer from nonpremultiplied alpha format to premultiplied alpha format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagepremultiplydata_bgraffff)*