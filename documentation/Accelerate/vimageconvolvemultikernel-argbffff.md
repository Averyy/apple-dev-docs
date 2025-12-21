# vImageConvolveMultiKernel_ARGBFFFF(_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Convolves each channel of a floating-point 32-bit-per-channel, 4-channel interleaved image by one of the four 2D kernels.

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
func vImageConvolveMultiKernel_ARGBFFFF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutableRawPointer!, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ kernels: UnsafeMutablePointer<UnsafePointer<Float>?>, _ kernel_height: UInt32, _ kernel_width: UInt32, _ biases: UnsafePointer<Float>, _ backgroundColor: UnsafePointer<Float>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, a negative value indicates one of the error codes that [`Data Types and Constants`](data-types-and-constants.md) describes, and a positive value indicates the required size for the temporary buffer.

#### Discussion

##### Optimize Performance with Temporary Buffers

This function uses a multiple-pass algorithm that saves intermediate pixel values between passes. In some cases, the destination buffer may not be large enough to store that intermediate data, so the operation requires additional storage.

Pass `nil` to the `tempBuffer` parameter to have vImage create and manage this temporary storage for you.

In cases where your code calls the function frequently (for example, when processing video), create and manage this temporary buffer yourself and reuse it across function calls. Reusing a buffer avoids vImage allocating the temporary storage with each call.

To use your own temporary buffer, first call the function with the same values for all other parameters that you intend to use for subsequent calls. In addition, pass the `kvImageGetTempBufferSize` flag. The `kvImageGetTempBufferSize` instructs the function not to perform any processing, and to return a positive value that represents the minimum size, in bytes, of the temporary buffer. A negative return value represents an error.

After you allocate the memory for the temporary buffer, pass that to the `tempBuffer` parameter for subsequent calls to the function, and don’t pass the `kvImageGetTempBufferSize` flag.

## Parameters

- `src`: A pointer to a vImage buffer structure that contains data for the source image.
- `dest`: A pointer to a vImage buffer data structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, you need to deallocate the memory. The size (number of rows and number of columns) of the destination buffer also specifies the size of the region of interest in the source buffer.
- `tempBuffer`: A pointer to workspace memory the function uses as it operates on an image. Pass   to instruct the function to allocate, use, and then free its own temporary buffer.
- `srcOffsetToROI_X`: The horizontal offset, in pixels, to the upper-left pixel of the region of interest within the source image.
- `srcOffsetToROI_Y`: The vertical offset, in pixels, to the upper-left pixel of the region of interest within the source image.
- `kernels`: An array of pointers to the data for four kernels. The first kernel is for the alpha channel, the second for red, the third for green, and the fourth for blue. The data for each kernel is a packed array of floating-point values.
- `kernel_height`: The height of the kernel in pixels. This value needs to be odd.
- `kernel_width`: The width of the kernel in pixels. This value needs to be odd.
- `biases`: An array of four values to add to each element of the convolution result for one channel, before clipping. The first value is for the alpha channel, the second for red, the third for green, and the fourth for blue
- `backgroundColor`: A background color. If you supply a color, you need to also set the   flag; otherwise, the function ignores the color.
- `flags`: Pass one of the following flags to specify how vImage handles pixel locations beyond the edge of the source image:  ,  ,  , or  .

## See Also

- [func vImageConvolveWithBias_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, UnsafePointer<Float>!, UInt32, UInt32, Float, UnsafePointer<Float>!, vImage_Flags) -> vImage_Error](vimageconvolvewithbias_argbffff(_:_:_:_:_:_:_:_:_:_:_:).md)
  Convolves a floating-point 32-bit-per-channel, 4-channel interleaved image by a 2D kernel and adds a bias.
- [func vImageConvolveMultiKernel_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, UnsafeMutablePointer<UnsafePointer<Int16>?>!, UInt32, UInt32, UnsafePointer<Int32>!, UnsafePointer<Int32>!, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvolvemultikernel_argb8888(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Convolves each channel of an 8-bit-per-channel, 4-channel interleaved image by one of the four 2D kernels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvolvemultikernel_argbffff(_:_:_:_:_:_:_:_:_:_:_:))*