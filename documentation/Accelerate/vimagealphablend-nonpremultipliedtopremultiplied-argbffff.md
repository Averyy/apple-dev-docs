# vImageAlphaBlend_NonpremultipliedToPremultiplied_ARGBFFFF(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Composites a nonpremultiplied 32-bit-per-channel, ARGB buffer over a premultiplied ARGB buffer and generates a premultiplied result.

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
func vImageAlphaBlend_NonpremultipliedToPremultiplied_ARGBFFFF(_ srcTop: UnsafePointer<vImage_Buffer>, _ srcBottom: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

On return of this function, the value of each pixel in the destination buffer is:

```objc
result = srcTop * srcTopAlpha + (1 - srcTopAlpha) * srcBottom;
```

## Parameters

- `srcTop`: The vImage buffer that provides the nonpremultiplied source top image.
- `srcBottom`: The vImage buffer that provides the premultiplied source bottom image.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [Compositing images with alpha blending](compositing-images-with-alpha-blending.md)
  Combine two images by using alpha blending to create a single output.
- [func vImageAlphaBlend_NonpremultipliedToPremultiplied_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagealphablend_nonpremultipliedtopremultiplied_planar8(_:_:_:_:_:).md)
  Composites a nonpremultiplied 8-bit planar buffer over a premultiplied 8-bit planar buffer and generates a premultiplied result.
- [func vImageAlphaBlend_NonpremultipliedToPremultiplied_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagealphablend_nonpremultipliedtopremultiplied_planarf(_:_:_:_:_:).md)
  Composites a nonpremultiplied 32-bit planar buffer over a premultiplied 32-bit planar buffer and generates a premultiplied result.
- [func vImageAlphaBlend_NonpremultipliedToPremultiplied_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagealphablend_nonpremultipliedtopremultiplied_argb8888(_:_:_:_:).md)
  Composites a nonpremultiplied 8-bit-per-channel, ARGB buffer over a premultiplied ARGB buffer and generates a premultiplied result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagealphablend_nonpremultipliedtopremultiplied_argbffff(_:_:_:_:))*