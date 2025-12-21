# vImageRichardsonLucyDeConvolve_ARGB8888(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Deconvolves an 8-bit-per-channel, 4-channel interleaved image.

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
func vImageRichardsonLucyDeConvolve_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutableRawPointer!, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ kernel: UnsafePointer<Int16>!, _ kernel2: UnsafePointer<Int16>!, _ kernel_height: UInt32, _ kernel_width: UInt32, _ kernel_height2: UInt32, _ kernel_width2: UInt32, _ divisor: Int32, _ divisor2: Int32, _ backgroundColor: UnsafePointer<UInt8>!, _ iterationCount: UInt32, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, a negative value indicates one of the error codes that [`Data Types and Constants`](data-types-and-constants.md) describes, and a positive value indicates the required size for the temporary buffer.

#### Discussion

This function performs a Richardson-Lucy deconvolution of a region of interest within a source image by an M x N kernel, performing a specified number of iterations and placing the result in a destination buffer.

##### Optimize Performance with Temporary Buffers

This function uses a multiple-pass algorithm that saves intermediate pixel values between passes. In some cases, the destination buffer may not be large enough to store that intermediate data, so the operation requires additional storage.

Pass `nil` to the `tempBuffer` parameter to have vImage create and manage this temporary storage for you.

In cases where your code calls the function frequently (for example, when processing video), create and manage this temporary buffer yourself and reuse it across function calls. Reusing a buffer avoids vImage allocating the temporary storage with each call.

To use your own temporary buffer, first call the function with the same values for all other parameters that you intend to use for subsequent calls. In addition, pass the `kvImageGetTempBufferSize` flag. The `kvImageGetTempBufferSize` instructs the function not to perform any processing, and to return a positive value that represents the minimum size, in bytes, of the temporary buffer. A negative return value represents an error.

After you allocate the memory for the temporary buffer, pass that to the `tempBuffer` parameter for subsequent calls to the function, and don’t pass the `kvImageGetTempBufferSize` flag.

## Parameters

- `src`: A pointer to a vImage buffer structure that contains data for the source image.
- `dest`: A pointer to a vImage buffer data structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, you need to deallocate the memory.
- `tempBuffer`: A pointer to workspace memory the function uses as it operates on an image. Pass   to instruct the function to allocate, use, and then free its own temporary buffer.
- `srcOffsetToROI_X`: The horizontal offset, in pixels, to the upper-left pixel of the region of interest within the source image.
- `srcOffsetToROI_Y`: The vertical offset, in pixels, to the upper-left pixel of the region of interest within the source image.
- `kernel`: A pointer to the deconvolution kernel data, which needs to be a packed array without any padding. The kernel expresses a blurring convolution or point-spread function.
- `kernel2`: A pointer to the data of a second kernel, which needs to be a packed array without any padding. Supply this kernel only if the first kernel is asymmetrical; otherwise pass  .
- `kernel_height`: The height of the first kernel in pixels. This value needs to be odd.
- `kernel_width`: The width of the first kernel in pixels. This value needs to be odd.
- `kernel_height2`: The height of the second kernel in pixels (ignored if   is  ). This value needs to be odd.
- `kernel_width2`: The width of the second kernel in pixels (ignored if   is  ). This value needs to be odd.
- `divisor`: The divisor to use in convolutions with the first kernel.
- `divisor2`: The divisor to use in convolutions with the second kernel.
- `backgroundColor`: A background color. If you supply a color, you need to also set the   flag; otherwise, the function ignores the color.
- `iterationCount`: The number of times to iterate the deconvolution algorithm.
- `flags`: Pass one of the following flags to specify how vImage handles pixel locations beyond the edge of the source image:  ,  ,  , or  .

## See Also

- [func vImageRichardsonLucyDeConvolve_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, UnsafePointer<Int16>!, UnsafePointer<Int16>!, UInt32, UInt32, UInt32, UInt32, Int32, Int32, Pixel_8, UInt32, vImage_Flags) -> vImage_Error](vimagerichardsonlucydeconvolve_planar8(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Deconvolves an 8-bit planar image.
- [func vImageRichardsonLucyDeConvolve_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, UnsafePointer<Float>!, UnsafePointer<Float>!, UInt32, UInt32, UInt32, UInt32, Pixel_F, UInt32, vImage_Flags) -> vImage_Error](vimagerichardsonlucydeconvolve_planarf(_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Deconvolves a floating-point 32-bit planar image.
- [func vImageRichardsonLucyDeConvolve_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, UnsafePointer<Float>!, UnsafePointer<Float>!, UInt32, UInt32, UInt32, UInt32, UnsafePointer<Float>!, UInt32, vImage_Flags) -> vImage_Error](vimagerichardsonlucydeconvolve_argbffff(_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Deconvolves a floating-point 32-bit-per-channel, 4-channel interleaved image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagerichardsonlucydeconvolve_argb8888(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:))*