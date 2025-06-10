# vImageAlphaBlend_PlanarF(_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Performs nonpremultiplied alpha compositing of two 8-bit planar buffers.

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
func vImageAlphaBlend_PlanarF(_ srcTop: UnsafePointer<vImage_Buffer>, _ srcTopAlpha: UnsafePointer<vImage_Buffer>, _ srcBottom: UnsafePointer<vImage_Buffer>, _ srcBottomAlpha: UnsafePointer<vImage_Buffer>, _ alpha: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

In order to provide the best performance, this function doesn’t calculate the alpha channel for the composite image. Use the following code to calculate the alpha channel for the composite image that you pass to this function as the `alpha` parameter:

```swift
vImagePremultipliedAlphaBlend_PlanarF(srcTopAlpha,
                                      srcTopAlpha,
                                      srcBottomAlpha,
                                      alpha,
                                      vImage_Flags(kvImageNoFlags))
```

On return of [`vImagePremultipliedAlphaBlend_Planar8(_:_:_:_:_:)`](vimagepremultipliedalphablend_planar8(_:_:_:_:_:).md), the value of each pixel in the alpha buffer is:

```objc
float alpha = srcTopAlpha + (1.0 - srcTopAlpha) * srcBottomAlpha
```

If you’re performing an alpha blend on multiple-channel data, such as an RGB image, use the same alpha channel buffer for each call to this function.

On return of this function, the value of each pixel in the destination buffer is:

```objc
float destColor = (  srcTopColor * srcTopAlpha + (1.0 - srcTopAlpha) * srcBottomAlpha * srcBottomColor ) / alpha
```

## Parameters

- `srcTop`: The vImage buffer that provides the source top image.
- `srcTopAlpha`: The vImage buffer that provides the source top alpha.
- `srcBottom`: The vImage buffer that provides the source bottom image.
- `srcBottomAlpha`: The vImage buffer that provides the source bottom alpha.
- `alpha`: The source vImage buffer that provides the precalculated alpha values of the composite image. Precalculate these values by calling the function  .
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [Compositing images with alpha blending](compositing-images-with-alpha-blending.md)
  Combine two images by using alpha blending to create a single output.
- [func vImageAlphaBlend_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagealphablend_planar8(_:_:_:_:_:_:_:).md)
  Performs nonpremultiplied alpha compositing of two 8-bit planar buffers.
- [func vImageAlphaBlend_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagealphablend_argb8888(_:_:_:_:).md)
  Performs nonpremultiplied alpha compositing of two 8-bit-per-channel, 4-channel ARGB buffers.
- [func vImageAlphaBlend_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagealphablend_argbffff(_:_:_:_:).md)
  Performs nonpremultiplied alpha compositing of two 32-bit-per-channel, 4-channel ARGB buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagealphablend_planarf(_:_:_:_:_:_:_:))*