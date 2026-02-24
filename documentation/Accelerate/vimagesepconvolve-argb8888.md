# vImageSepConvolve_ARGB8888(_:_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Convolves an 8-bit-per-channel, 4-channel interleaved image by separate horizontal and vertical separable kernels.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func vImageSepConvolve_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutableRawPointer!, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ kernelX: UnsafePointer<Float>!, _ kernelX_width: UInt32, _ kernelY: UnsafePointer<Float>!, _ kernelY_width: UInt32, _ bias: Float, _ backgroundColor: UnsafePointer<UInt8>!, _ flags: vImage_Flags) -> vImage_Error
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

You can use the same workspace memory for a group of images that are different sizes. To do this, create a vImage buffer structure with a size that shares the maximum width and maximum height of the images that you’re working with. For example, to create a workspace memory that’s suitable for 4x4, 5x4, and 4x5 images, pass a buffer with the size 5x5.

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the `height`, `width`, and `rowBytes` fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `tempBuffer`: A pointer to workspace memory the function uses as it operates on an image. Pass `nil` to instruct the function to allocate, use, and then free its own temporary buffer.
- `srcOffsetToROI_X`: The horizontal offset, in pixels, to the upper-left pixel of the region of interest within the source image.
- `srcOffsetToROI_Y`: The vertical offset, in pixels, to the upper-left pixel of the region of interest within the source image.
- `kernelX`: A pointer to the 32-bit floating-point horizontal convolution weights.
- `kernelX_width`: The number of elements in the horizontal convolution kernel.
- `kernelY`: A pointer to the 32-bit floating-point vertical convolution weights.
- `kernelY_width`: The number of elements in the vertical convolution kernel.
- `bias`: The value that the operation adds to each element in the convolution result.
- `backgroundColor`: The background color that the function applies when you pass the [`kvImageBackgroundColorFill`](kvimagebackgroundcolorfill.md) flag.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](kvimagedonottile.md). To instruct the function to return the minimum size of the workspace memory, set the [`kvImageGetTempBufferSize`](kvimagegettempbuffersize.md) flag. Pass one of the following flags to specify how vImage handles pixel locations beyond the edge of the source image: [`kvImageCopyInPlace`](kvimagecopyinplace.md), [`kvImageTruncateKernel`](kvimagetruncatekernel.md), [`kvImageBackgroundColorFill`](kvimagebackgroundcolorfill.md), or [`kvImageEdgeExtend`](kvimageedgeextend.md).

## See Also

- [func vImageSepConvolve_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, UnsafePointer<Float>!, UInt32, UnsafePointer<Float>!, UInt32, Float, Pixel_16U, vImage_Flags) -> vImage_Error](vimagesepconvolve_planar8(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Convolves an 8-bit planar image by separate horizontal and vertical separable kernels.
- [func vImageSepConvolve_Planar16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, UnsafePointer<Float>!, UInt32, UnsafePointer<Float>!, UInt32, Float, Pixel_16U, vImage_Flags) -> vImage_Error](vimagesepconvolve_planar16u(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Convolves an unsigned 16-bit planar image by separate horizontal and vertical separable kernels.
- [func vImageSepConvolve_Planar16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, UnsafePointer<Float>!, UInt32, UnsafePointer<Float>!, UInt32, Float, Pixel_16F, vImage_Flags) -> vImage_Error](vimagesepconvolve_planar16f(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Convolves a floating-point 16-bit planar image by separate horizontal and vertical separable kernels.
- [func vImageSepConvolve_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, UnsafePointer<Float>!, UInt32, UnsafePointer<Float>!, UInt32, Float, Pixel_F, vImage_Flags) -> vImage_Error](vimagesepconvolve_planarf(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Convolves a floating-point 32-bit planar image by separate horizontal and vertical separable kernels.
- [func vImageSepConvolve_Planar8to16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, UnsafePointer<Float>!, UInt32, UnsafePointer<Float>!, UInt32, Float, Float, Pixel_8, vImage_Flags) -> vImage_Error](vimagesepconvolve_planar8to16u(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Convolves an 8-bit planar image by separate horizontal and vertical separable kernels, and writes the result to an unsigned 16-bit planar destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagesepconvolve_argb8888(_:_:_:_:_:_:_:_:_:_:_:_:))*