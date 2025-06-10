# vImageAffineWarpCG_ARGB8888(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies a Core Graphics affine transformation to an ARGB8888 source image.

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
func vImageAffineWarpCG_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutableRawPointer!, _ transform: UnsafePointer<vImage_CGAffineTransform>, _ backColor: UnsafePointer<UInt8>!, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes described in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

Core Graphics types use float values in 32-bit and double values in 64-bit. This convenience method takes the Core Graphics affine transform type directly so that you don’t have to use a different function for 64-bit applications.

This function maps each pixel in the source image `[x, y]` to a new position `[x’, y’]` in the destination image, using this formula:

```objc
(x', y') = (x, y) * transform
```

where `transform` is the 3x3 affine transformation matrix.

##### Allocating Temporary Buffer Memory

If you want to allocate the memory for the `tempBuffer` parameter yourself, call this function twice, as follows:

1. To determine the minimum size for the temporary buffer, the first time you call this function, pass the [`kvImageGetTempBufferSize`](kvimagegettempbuffersize.md) flag. Pass the same values for all other parameters that you intend to use for the second call. The function returns the required minimum size, which should be a positive value. (A negative returned value indicates an error.) The `kvImageGetTempBufferSize` flag prevents the function from performing any processing other than to determine the minimum buffer size.
2. After you allocate enough space for a buffer of the returned size, call the function a second time, passing a valid pointer in the `tempBuffer` parameter. This time, don’t pass the [`kvImageGetTempBufferSize`](kvimagegettempbuffersize.md) flag.

## Parameters

- `src`: A pointer to a vImage buffer structure that contains the source image whose data you want to transform.
- `dest`: A pointer to a vImage buffer data structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, you must deallocate the memory.
- `tempBuffer`: If you want to allocate the buffer yourself, see   for information on how to determine the minimum size that you must allocate.
- `transform`: The affine transformation matrix to apply to the source image.
- `backColor`: A background color. Pass a pixel value only if you also set the   flag.
- `flags`: This function ignores the   flag.

## See Also

- [func vImageAffineWarpCG_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_CGAffineTransform>, Pixel_8, vImage_Flags) -> vImage_Error](vimageaffinewarpcg_planar8(_:_:_:_:_:_:).md)
  Applies a Core Graphics affine transformation to a Planar8 source image.
- [func vImageAffineWarpCG_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_CGAffineTransform>, Pixel_F, vImage_Flags) -> vImage_Error](vimageaffinewarpcg_planarf(_:_:_:_:_:_:).md)
  Applies a Core Graphics affine transformation to a PlanarF source image.
- [func vImageAffineWarpCG_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_CGAffineTransform>, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimageaffinewarpcg_argb16u(_:_:_:_:_:_:).md)
  Applies a Core Graphics affine transformation to an ARGB16U source image.
- [func vImageAffineWarpCG_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_CGAffineTransform>, UnsafePointer<Int16>!, vImage_Flags) -> vImage_Error](vimageaffinewarpcg_argb16s(_:_:_:_:_:_:).md)
  Applies a Core Graphics affine transformation to an ARGB16S source image.
- [func vImageAffineWarpCG_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_CGAffineTransform>, UnsafePointer<Float>!, vImage_Flags) -> vImage_Error](vimageaffinewarpcg_argbffff(_:_:_:_:_:_:).md)
  Applies a Core Graphics affine transformation to an ARGBFFFF source image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageaffinewarpcg_argb8888(_:_:_:_:_:_:))*