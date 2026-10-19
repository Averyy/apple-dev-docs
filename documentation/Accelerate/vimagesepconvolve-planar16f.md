# vImageSepConvolve_Planar16F(_:_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Convolves a floating-point 16-bit planar image by separate horizontal and vertical separable kernels.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func vImageSepConvolve_Planar16F(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutableRawPointer!, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ kernelX: UnsafePointer<Float>!, _ kernelX_width: UInt32, _ kernelY: UnsafePointer<Float>!, _ kernelY_width: UInt32, _ bias: Float, _ backgroundColor: Pixel_16F, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, a negative value indicates one of the error codes that [`Data Types and Constants`](data-types-and-constants.md) describes, and a positive value indicates the required size for the temporary buffer.

#### Discussion

A separable convolution applies two separate 1D filters along the rows and columns of an image in succession. This allows for a faster implementation compared to applying the corresponding 2D convolution filter.

An example of separable convolution is the edge-detection Sobel filter, for approximating the image gradient. The Sobel filter is the outer product of the averaging filter, `[1, 2, 1]`, and the differentiation filter, `[-1, 0, 1]`. For the image x-derivative, this results in the general 2D filter:

![Matrix multiplication that describes the column matrix that contains the values one, two, one multiplied by the row matrix that contains the values minus one, zero, one. The result is a square matrix that contains the values minus one, zero, one, minus two, zero, two, minus one, zero, one.](/images/com.apple.accelerate/media-3957884@2x.png)

Note that the differentiation filter produces a result that contains, on average, half of the destination values having a negative value. Add a bias of 128 to allow the operation to represent values in the range `-1...1` as unsigned 8-bit integer destination pixels. For example, the operation represents a result of -1 as 0 in the destination, and represents a result of 1 as 255 in the destination.

The following code shows how to apply the averaging and differentiation components of the Sobel filter to a 16-bit half-float (`Planar16F`) planar buffer:

**Swift**:

```swift
// A 3 × 3 `Planar16F` source; all pixels = 1.0 (half-float 0x3C00).
let source = vImage.PixelBuffer<vImage.Planar16F>(
    pixelValues: [UInt16](repeating: 0x3C00, count: 9),
    size: .init(width: 3, height: 3))

// A 3 × 3 destination buffer, all zeros initially.
let destination = vImage.PixelBuffer<vImage.Planar16F>(
    pixelValues: [UInt16](repeating: 0, count: 9),
    size: .init(width: 3, height: 3))

// Separable box-filter kernels: all-ones 1×3, producing a 3×3 sum.
let kernelX: [Float] = [1, 1, 1]
let kernelY: [Float] = [1, 1, 1]
// bias = 128: offset added after convolution; result = 9.0 + 128.0 = 137.0.
let bias = Float(128)
// The `backgroundColor` equals 0; it's unused because `kvImageEdgeExtend` is used.
let backgroundColor = Pixel_16F(0)

// Apply the separable convolution; the `kvImageEdgeExtend` replicates edge pixels
// so every output pixel sums exactly nine source pixels.
source.withUnsafePointerToVImageBuffer { src in
    destination.withUnsafePointerToVImageBuffer { dest in
        _ = vImageSepConvolve_Planar16F(src,
                                        dest,
                                        nil,
                                        0, 0,
                                        kernelX, UInt32(kernelX.count),
                                        kernelY, UInt32(kernelY.count),
                                        bias,
                                        backgroundColor,
                                        vImage_Flags(kvImageEdgeExtend))
    }
}

// Convert the center pixel (index 4) from half-float to Float, and print.
let centerHalf = destination.array[4]
let halfBuffer = vImage.PixelBuffer<vImage.Planar16F>(
    pixelValues: [centerHalf],
    size: .init(width: 1, height: 1))
let floatBuffer = vImage.PixelBuffer<vImage.PlanarF>(
    pixelValues: [Float(0)],
    size: .init(width: 1, height: 1))
halfBuffer.withUnsafePointerToVImageBuffer { halfBuf in
    floatBuffer.withUnsafePointerToVImageBuffer { floatBuf in
        _ = vImageConvert_Planar16FtoPlanarF(halfBuf, floatBuf, vImage_Flags(kvImageNoFlags))
    }
}
// Prints "137.0".
print(floatBuffer.array[0])
```

**Objective-C**:

```objc
// Source: 3x3 `Planar16F` image; all pixels = 1.0 (half-float `0x3C00`).
uint16_t src[9];
for (int i = 0; i < 9; i++) { src[i] = 0x3C00; }
uint16_t dst[9] = {0};

vImage_Buffer srcBuf = {
    .data     = src,
    .width    = 3,
    .height   = 3,
    .rowBytes = 3 * 2
};

vImage_Buffer dstBuf = {
    .data     = dst,
    .width    = 3,
    .height   = 3,
    .rowBytes = 3 * 2
};

float kernelX[3] = {1.0f, 1.0f, 1.0f};
float kernelY[3] = {1.0f, 1.0f, 1.0f};
float bias = 128.0f;
Pixel_16F backgroundColor = 0;

vImageSepConvolve_Planar16F(&srcBuf,
                             &dstBuf,
                             NULL,
                             0, 0,
                             kernelX, 3,
                             kernelY, 3,
                             bias,
                             backgroundColor,
                             kvImageEdgeExtend);

// Convert center pixel (`dst[4]`) to float and print.
// Result: 9.0 + 128.0 = 137.0
vImage_Buffer halfBuf  = { .data = dst + 4, .width = 1, .height = 1, .rowBytes = 2 };
float fval = 0;
vImage_Buffer floatBuf = { .data = &fval, .width = 1, .height = 1, .rowBytes = 4 };
vImageConvert_Planar16FtoPlanarF(&halfBuf, &floatBuf, kvImageNoFlags);

// Prints "137.000000".
printf("%f\n", fval);
```

The following image shows two photographs, with the original image on the left, and the image after applying the Sobel filter on the right:

![An image of some buildings before and after applying an edge detection filter.](/images/com.apple.accelerate/media-3957882@2x.png)

##### Optimize Performance with Temporary Buffers

This function uses a multiple-pass algorithm that saves intermediate pixel values between passes. In some cases, the destination buffer may not be large enough to store that intermediate data, so the operation requires additional storage.

Pass `nil` to the `tempBuffer` parameter to have vImage create and manage this temporary storage for you.

In cases where your code calls the function frequently (for example, when processing video), create and manage this temporary buffer yourself and reuse it across function calls. Reusing a buffer avoids vImage allocating the temporary storage with each call.

To use your own temporary buffer, first call the function with the same values for all other parameters that you intend to use for subsequent calls. In addition, pass the `kvImageGetTempBufferSize` flag. The `kvImageGetTempBufferSize` instructs the function not to perform any processing, and to return a positive value that represents the minimum size, in bytes, of the temporary buffer. A negative return value represents an error.

After you allocate the memory for the temporary buffer, pass that to the `tempBuffer` parameter for subsequent calls to the function, and don’t pass the `kvImageGetTempBufferSize` flag.

You can use the same workspace memory for a group of images that are different sizes. To do this, create a vImage buffer structure with a size that shares the maximum width and maximum height of the images that you’re working with. For example, to create a workspace memory that’s suitable for 4x4, 5x4, and 4x5 images, pass a buffer with the size 5x5.

## Parameters

- `src`: A pointer to a vImage buffer structure that contains data for the source image.
- `dest`: A pointer to a vImage buffer data structure. You’re responsible for filling out the `height`, `width`, and `rowBytes` fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer to which this structure points contains the destination image data. When you no longer need the data buffer, you need to deallocate the memory. The size dimensions of the destination buffer also specifies the size of the region of interest in the source buffer.
- `tempBuffer`: A pointer to workspace memory the function uses as it operates on an image. Pass `nil` to instruct the function to allocate, use, and then free its own temporary buffer.
- `srcOffsetToROI_X`: The horizontal offset, in pixels, to the upper-left pixel of the region of interest within the source image.
- `srcOffsetToROI_Y`: The vertical offset, in pixels, to the upper-left pixel of the region of interest within the source image.
- `kernelX`: A pointer to the 1D horizontal weights.
- `kernelX_width`: The number of elements in the horizontal weights array.
- `kernelY`: A pointer to the 1D vertical weights.
- `kernelY_width`: The number of elements in the vertical weights array.
- `bias`: The value to add to each element in the convolution result, before performing any clipping.
- `backgroundColor`: A background color. If you supply a color, you need to also set the `kvImageBackgroundColorFill` flag; otherwise, the function ignores the color.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](kvimagedonottile.md). To instruct the function to return the minimum size of the workspace memory, set the [`kvImageGetTempBufferSize`](kvimagegettempbuffersize.md) flag. Pass one of the following flags to specify how vImage handles pixel locations beyond the edge of the source image: [`kvImageCopyInPlace`](kvimagecopyinplace.md), [`kvImageTruncateKernel`](kvimagetruncatekernel.md), [`kvImageBackgroundColorFill`](kvimagebackgroundcolorfill.md), or [`kvImageEdgeExtend`](kvimageedgeextend.md). If you want vImage to use faster but lower-precision internal arithmetic, set the [`kvImageUseFP16Accumulator`](kvimageusefp16accumulator.md) flag.

## See Also

- [func vImageSepConvolve_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, UnsafePointer<Float>!, UInt32, UnsafePointer<Float>!, UInt32, Float, Pixel_16U, vImage_Flags) -> vImage_Error](vimagesepconvolve_planar8(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Convolves an 8-bit planar image by separate horizontal and vertical separable kernels.
- [func vImageSepConvolve_Planar16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, UnsafePointer<Float>!, UInt32, UnsafePointer<Float>!, UInt32, Float, Pixel_16U, vImage_Flags) -> vImage_Error](vimagesepconvolve_planar16u(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Convolves an unsigned 16-bit planar image by separate horizontal and vertical separable kernels.
- [func vImageSepConvolve_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, UnsafePointer<Float>!, UInt32, UnsafePointer<Float>!, UInt32, Float, Pixel_F, vImage_Flags) -> vImage_Error](vimagesepconvolve_planarf(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Convolves a floating-point 32-bit planar image by separate horizontal and vertical separable kernels.
- [func vImageSepConvolve_Planar8to16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, UnsafePointer<Float>!, UInt32, UnsafePointer<Float>!, UInt32, Float, Float, Pixel_8, vImage_Flags) -> vImage_Error](vimagesepconvolve_planar8to16u(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Convolves an 8-bit planar image by separate horizontal and vertical separable kernels, and writes the result to an unsigned 16-bit planar destination.
- [func vImageSepConvolve_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, UnsafePointer<Float>!, UInt32, UnsafePointer<Float>!, UInt32, Float, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimagesepconvolve_argb8888(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Convolves an 8-bit-per-channel, 4-channel interleaved image by separate horizontal and vertical separable kernels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagesepconvolve_planar16f(_:_:_:_:_:_:_:_:_:_:_:_:))*