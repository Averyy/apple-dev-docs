# vImageConvolveFloatKernel_ARGB8888(_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Convolves an 8-bit-per-channel, 4-channel interleaved image using 32-bit weights.

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
func vImageConvolveFloatKernel_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutableRawPointer!, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ kernel: UnsafePointer<Float>!, _ kernelHeight: UInt32, _ kernelWidth: UInt32, _ bias: Float, _ backgroundColor: UnsafePointer<UInt8>!, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `tempBuffer`: A pointer to an optional buffer that the function uses as a workspace during the convolution operation. Pass   to specify that the function allocates and deallocates its own temporary buffer. Pass the   flag to specify that the function returns the required temporary buffer size for a set of parameters.
- `srcOffsetToROI_X`: The horizontal offset, in pixels, to the upper-left pixel of the region of interest within the source image.
- `srcOffsetToROI_Y`: The vertical offset, in pixels, to the upper-left pixel of the region of interest within the source image.
- `kernel`: A pointer to the 32-bit floating-point convolution weights.
- `kernelHeight`: The height of the convolution kernel.
- `kernelWidth`: The width of the convolution kernel.
- `bias`: The value that the operation adds to each element in the convolution result.
- `backgroundColor`: The background color that the function applies when you pass the   flag.
- `flags`: Pass one of the following flags to specify how vImage handles pixel locations beyond the edge of the source image:  ,  ,  , or  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvolvefloatkernel_argb8888(_:_:_:_:_:_:_:_:_:_:_:))*