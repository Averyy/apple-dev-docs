# vImagePremultipliedAlphaBlend_Planar8(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Performs premultiplied alpha compositing of two 8-bit planar buffers.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 5.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImagePremultipliedAlphaBlend_Planar8(_ srcTop: UnsafePointer<vImage_Buffer>, _ srcTopAlpha: UnsafePointer<vImage_Buffer>, _ srcBottom: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

On return of this function, the value of each pixel in the destination buffer is:

```objc
float destColor = srcTopColor  + (1.0 - srcTopAlpha) * srcBottomColor;
```

## Parameters

- `srcTop`: The vImage buffer that provides the source top image.
- `srcTopAlpha`: The vImage buffer that provides the source top alpha.
- `srcBottom`: The vImage buffer that provides the source bottom image.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [Compositing images with alpha blending](compositing-images-with-alpha-blending.md)
  Combine two images by using alpha blending to create a single output.
- [func vImagePremultipliedAlphaBlend_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultipliedalphablend_planarf(_:_:_:_:_:).md)
  Performs premultiplied alpha compositing of two 32-bit planar buffers.
- [func vImagePremultipliedAlphaBlend_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultipliedalphablend_argb8888(_:_:_:_:).md)
  Performs premultiplied alpha compositing of two 8-bit-per-channel, 4-channel ARGB buffers.
- [func vImagePremultipliedAlphaBlend_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultipliedalphablend_argbffff(_:_:_:_:).md)
  Performs premultiplied alpha compositing of two 32-bit-per-channel, 4-channel ARGB buffers.
- [func vImagePremultipliedAlphaBlend_BGRA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultipliedalphablend_bgra8888(_:_:_:_:).md)
  Performs premultiplied alpha compositing of two 8-bit-per-channel, 4-channel BGRA buffers.
- [func vImagePremultipliedAlphaBlend_BGRAFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultipliedalphablend_bgraffff(_:_:_:_:).md)
  Performs premultiplied alpha compositing of two 32-bit-per-channel, 4-channel BGRA buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagepremultipliedalphablend_planar8(_:_:_:_:_:))*