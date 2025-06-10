# vImageAlphaBlend_ARGBFFFF(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Performs nonpremultiplied alpha compositing of two 32-bit-per-channel, 4-channel ARGB buffers.

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
func vImageAlphaBlend_ARGBFFFF(_ srcTop: UnsafePointer<vImage_Buffer>, _ srcBottom: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](kvimagedonottile.md); otherwise, pass [`kvImageNoFlags`](kvimagenoflags.md).

#### Discussion

On return of this function, the value of each pixel in the destination buffer is:

```objc
float alpha =  srcTopAlpha + (1.0 - srcTopAlpha) * srcBottomAlpha
float destColor = (  srcTopColor * srcTopAlpha + (1.0 - srcTopAlpha) * srcBottomAlpha * srcBottomColor ) / alpha
```

## Parameters

- `srcTop`: The vImage buffer that provides the source top image.
- `srcBottom`: The vImage buffer that provides the source bottom image.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  .

## See Also

- [Compositing images with alpha blending](compositing-images-with-alpha-blending.md)
  Combine two images by using alpha blending to create a single output.
- [func vImageAlphaBlend_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagealphablend_planar8(_:_:_:_:_:_:_:).md)
  Performs nonpremultiplied alpha compositing of two 8-bit planar buffers.
- [func vImageAlphaBlend_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagealphablend_planarf(_:_:_:_:_:_:_:).md)
  Performs nonpremultiplied alpha compositing of two 8-bit planar buffers.
- [func vImageAlphaBlend_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagealphablend_argb8888(_:_:_:_:).md)
  Performs nonpremultiplied alpha compositing of two 8-bit-per-channel, 4-channel ARGB buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagealphablend_argbffff(_:_:_:_:))*