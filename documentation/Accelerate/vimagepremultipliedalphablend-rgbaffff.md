# vImagePremultipliedAlphaBlend_RGBAFFFF

**Framework**: Accelerate  
**Kind**: macro

Performs premultiplied alpha compositing of two 32-bit-per-channel, 4-channel RGBA buffers.

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
#define vImagePremultipliedAlphaBlend_RGBAFFFF(_srcTop, _srcBottom, _dest, _flags)
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

On return of this function, the value of each pixel in the destination buffer is:

```objc
float destColor = srcTopColor  + (1.0 - srcTopAlpha) * srcBottomColor;
float alpha =  srcTopAlpha + (1.0 - srcTopAlpha) * srcBottomAlpha
```

## Parameters

- `_srcTop`: The vImage buffer that provides the source top image.
- `_srcBottom`: The vImage buffer that provides the source bottom image.
- `_dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `_flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [Compositing images with alpha blending](compositing-images-with-alpha-blending.md)
  Combine two images by using alpha blending to create a single output.
- [func vImagePremultipliedAlphaBlend_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultipliedalphablend_planar8(_:_:_:_:_:).md)
  Performs premultiplied alpha compositing of two 8-bit planar buffers.
- [func vImagePremultipliedAlphaBlend_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultipliedalphablend_planarf(_:_:_:_:_:).md)
  Performs premultiplied alpha compositing of two 32-bit planar buffers.
- [func vImagePremultipliedAlphaBlend_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultipliedalphablend_argb8888(_:_:_:_:).md)
  Performs premultiplied alpha compositing of two 8-bit-per-channel, 4-channel ARGB buffers.
- [func vImagePremultipliedAlphaBlend_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultipliedalphablend_argbffff(_:_:_:_:).md)
  Performs premultiplied alpha compositing of two 32-bit-per-channel, 4-channel ARGB buffers.
- [func vImagePremultipliedAlphaBlend_BGRA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultipliedalphablend_bgra8888(_:_:_:_:).md)
  Performs premultiplied alpha compositing of two 8-bit-per-channel, 4-channel BGRA buffers.
- [vImagePremultipliedAlphaBlend_RGBA8888](vimagepremultipliedalphablend_rgba8888.md)
  Performs premultiplied alpha compositing of two 8-bit-per-channel, 4-channel RGBA buffers.
- [func vImagePremultipliedAlphaBlend_BGRAFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultipliedalphablend_bgraffff(_:_:_:_:).md)
  Performs premultiplied alpha compositing of two 32-bit-per-channel, 4-channel BGRA buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagepremultipliedalphablend_rgbaffff)*