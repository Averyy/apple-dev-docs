# vImageUnpremultiplyData_ARGB16U(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Transforms an unsigned 16-bit-per-channel, 4-channel ARGB buffer from premultiplied alpha format to nonpremultiplied alpha format.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 6.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageUnpremultiplyData_ARGB16U(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

This function divides color channels by the alpha channel using the following code:

```swift
uint16_t destColor = ( MIN(src_color, alpha) * 65535 + alpha/2) / alpha;
uint16_t destAlpha = alpha;
```

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [Compositing images with alpha blending](compositing-images-with-alpha-blending.md)
  Combine two images by using alpha blending to create a single output.
- [func vImageUnpremultiplyData_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageunpremultiplydata_planar8(_:_:_:_:).md)
  Transforms an 8-bit planar buffer from premultiplied alpha format to nonpremultiplied alpha format.
- [func vImageUnpremultiplyData_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageunpremultiplydata_planarf(_:_:_:_:).md)
  Transforms a 32-bit planar buffer from premultiplied alpha format to nonpremultiplied alpha format.
- [func vImageUnpremultiplyData_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageunpremultiplydata_argb8888(_:_:_:).md)
  Transforms an 8-bit-per-channel, 4-channel ARGB buffer from premultiplied alpha format to nonpremultiplied alpha format.
- [func vImageUnpremultiplyData_RGBA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageunpremultiplydata_rgba8888(_:_:_:).md)
  Transforms an 8-bit-per-channel, 4-channel RGBA buffer from premultiplied alpha format to nonpremultiplied alpha format.
- [func vImageUnpremultiplyData_RGBA16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageunpremultiplydata_rgba16u(_:_:_:).md)
  Transforms an unsigned 16-bit-per-channel, 4-channel RGBA buffer from premultiplied alpha format to nonpremultiplied alpha format.
- [func vImageUnpremultiplyData_RGBA16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageunpremultiplydata_rgba16f(_:_:_:).md)
  Transforms a floating-point 16-bit-per-channel, 4-channel RGBA buffer from premultiplied alpha format to nonpremultiplied alpha format.
- [func vImageUnpremultiplyData_ARGB16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageunpremultiplydata_argb16q12(_:_:_:).md)
  Transforms a fixed-point 16-bit-per-channel, 4-channel ARGB buffer from premultiplied alpha format to nonpremultiplied alpha format.
- [func vImageUnpremultiplyData_RGBA16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageunpremultiplydata_rgba16q12(_:_:_:).md)
  Transforms a fixed-point 16-bit-per-channel, 4-channel RGBA buffer from premultiplied alpha format to nonpremultiplied alpha format.
- [func vImageUnpremultiplyData_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageunpremultiplydata_argbffff(_:_:_:).md)
  Transforms a 32-bit-per-channel, 4-channel ARGB buffer from premultiplied alpha format to nonpremultiplied alpha format.
- [func vImageUnpremultiplyData_RGBAFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageunpremultiplydata_rgbaffff(_:_:_:).md)
  Transforms a 32-bit-per-channel, 4-channel RGBA buffer from premultiplied alpha format to nonpremultiplied alpha format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageunpremultiplydata_argb16u(_:_:_:))*