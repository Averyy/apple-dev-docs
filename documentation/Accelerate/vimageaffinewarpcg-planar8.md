# vImageAffineWarpCG_Planar8(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies a Core Graphics affine transformation to a Planar8 source image.

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
func vImageAffineWarpCG_Planar8(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutableRawPointer!, _ transform: UnsafePointer<vImage_CGAffineTransform>, _ backColor: Pixel_8, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, a negative value indicates one of the error codes that [`Data Types and Constants`](data-types-and-constants.md) describes, and a positive value indicates the required size for the temporary buffer.

#### Discussion

Core Graphics types use float values in 32-bit and double values in 64-bit. This convenience method takes the Core Graphics affine transform type directly so that you don’t have to use a different function for 64-bit applications.

This function maps each pixel in the source image `[x, y]` to a new position `[x’, y’]` in the destination image, using this formula:

```objc
(x', y') = (x, y) * transform
```

where `transform` is the 3x3 affine transformation matrix.

##### Optimize Performance with Temporary Buffers

This function uses a multiple-pass algorithm that saves intermediate pixel values between passes. In some cases, the destination buffer may not be large enough to store that intermediate data, so the operation requires additional storage.

Pass `nil` to the `tempBuffer` parameter to have vImage create and manage this temporary storage for you.

In cases where your code calls the function frequently (for example, when processing video), create and manage this temporary buffer yourself and reuse it across function calls. Reusing a buffer avoids vImage allocating the temporary storage with each call.

To use your own temporary buffer, first call the function with the same values for all other parameters that you intend to use for subsequent calls. In addition, pass the `kvImageGetTempBufferSize` flag. The `kvImageGetTempBufferSize` instructs the function not to perform any processing, and to return a positive value that represents the minimum size, in bytes, of the temporary buffer. A negative return value represents an error.

After you allocate the memory for the temporary buffer, pass that to the `tempBuffer` parameter for subsequent calls to the function, and don’t pass the `kvImageGetTempBufferSize` flag.

## Parameters

- `src`: A pointer to a vImage buffer structure that contains the source image whose data you want to transform.
- `dest`: A pointer to a vImage buffer data structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, you need to deallocate the memory.
- `tempBuffer`: A pointer to workspace memory the function uses as it operates on an image. Pass   to instruct the function to allocate, use, and then free its own temporary buffer.
- `transform`: The affine transformation matrix to apply to the source image.
- `backColor`: A background color. Pass a pixel value only if you also set the   flag.
- `flags`: This function ignores the   flag.

## See Also

- [func vImageAffineWarpCG_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_CGAffineTransform>, Pixel_F, vImage_Flags) -> vImage_Error](vimageaffinewarpcg_planarf(_:_:_:_:_:_:).md)
  Applies a Core Graphics affine transformation to a PlanarF source image.
- [func vImageAffineWarpCG_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_CGAffineTransform>, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimageaffinewarpcg_argb16u(_:_:_:_:_:_:).md)
  Applies a Core Graphics affine transformation to an ARGB16U source image.
- [func vImageAffineWarpCG_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_CGAffineTransform>, UnsafePointer<Int16>!, vImage_Flags) -> vImage_Error](vimageaffinewarpcg_argb16s(_:_:_:_:_:_:).md)
  Applies a Core Graphics affine transformation to an ARGB16S source image.
- [func vImageAffineWarpCG_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_CGAffineTransform>, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageaffinewarpcg_argb8888(_:_:_:_:_:_:).md)
  Applies a Core Graphics affine transformation to an ARGB8888 source image.
- [func vImageAffineWarpCG_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_CGAffineTransform>, UnsafePointer<Float>!, vImage_Flags) -> vImage_Error](vimageaffinewarpcg_argbffff(_:_:_:_:_:_:).md)
  Applies a Core Graphics affine transformation to an ARGBFFFF source image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageaffinewarpcg_planar8(_:_:_:_:_:_:))*