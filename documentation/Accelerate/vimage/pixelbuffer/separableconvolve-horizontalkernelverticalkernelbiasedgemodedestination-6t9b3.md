# separableConvolve(horizontalKernel:verticalKernel:bias:edgeMode:destination:)

**Framework**: Accelerate  
**Kind**: method

Performs separable convolution on a multiple plane 8-bit pixel buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
func separableConvolve(horizontalKernel: [Float], verticalKernel: [Float], bias: Float = 0, edgeMode: vImage.EdgeMode<Pixel_16U>, destination: vImage.PixelBuffer<Format>)
```

#### Discussion

The following code shows how to generate a multiplane pixel buffer from a [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) instance and apply a Gaussian blur using separable convolution:

```swift
let srcImage =  imageLiteral(resourceName: " ... ").cgImage(
    forProposedRect: nil,
    context: nil,
    hints: nil)!

var cgImageFormat = vImage_CGImageFormat(
    bitsPerComponent: 8,
    bitsPerPixel: 8 * 3,
    colorSpace: CGColorSpaceCreateDeviceRGB(),
    bitmapInfo: CGBitmapInfo(rawValue: CGImageAlphaInfo.none.rawValue))!

let interleavedBuffer = try vImage.PixelBuffer(
    cgImage: srcImage,
    cgImageFormat: &cgImageFormat,
    pixelFormat: vImage.Interleaved8x3.self)

let multiplaneSrcBuffer = vImage.PixelBuffer<vImage.Planar8x3>(
    interleavedBuffer: interleavedBuffer)

let multiplaneDestBuffer = vImage.PixelBuffer<vImage.Planar8x3>(
    size: multiplaneSrcBuffer.size)

multiplaneSrcBuffer.separableConvolve(
    horizontalKernel: vImage.ConvolutionKernel.gaussian1Dx7,
    verticalKernel:  vImage.ConvolutionKernel.gaussian1Dx7,
    edgeMode: .truncateKernel,
    destination: multiplaneDestBuffer)

multiplaneDestBuffer.convert(to: interleavedBuffer)

let outputImage = interleavedBuffer.makeCGImage(cgImageFormat: cgImageFormat)
```

## Parameters

- `horizontalKernel`: The 1D horizontal convolution kernel.
- `verticalKernel`: The 1D vertical convolution kernel.
- `bias`: A value that the operation adds to each element in the convolution result, before performing any clipping.
- `edgeMode`: The convolution edge mode. The background color must be a single   value.
- `destination`: The destination pixel buffer.

## See Also

- [Blurring an image](blurring-an-image.md)
  Filter an image by convolving it with custom and high-speed kernels.
- [func separableConvolve(horizontalKernel: [Float], verticalKernel: [Float], bias: Float, edgeMode: vImage.EdgeMode<Pixel_16U>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/separableconvolve(horizontalkernel:verticalkernel:bias:edgemode:destination:)-2iyq6.md)
  Performs separable convolution on an 8-bit planar pixel buffer.
- [func separableConvolve(horizontalKernel: [Float], verticalKernel: [Float], bias: Float, edgeMode: vImage.EdgeMode<Pixel_16F>, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/separableconvolve(horizontalkernel:verticalkernel:bias:edgemode:usefloat16accumulator:destination:).md)
  Performs separable convolution on a 16-bit planar pixel buffer.
- [func separableConvolve(horizontalKernel: [Float], verticalKernel: [Float], bias: Float, edgeMode: vImage.EdgeMode<Pixel_F>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/separableconvolve(horizontalkernel:verticalkernel:bias:edgemode:destination:)-2qofv.md)
  Performs separable convolution on a 32-bit planar pixel buffer.
- [func separableConvolve(horizontalKernel: [Float], verticalKernel: [Float], bias: Float, edgeMode: vImage.EdgeMode<Pixel_F>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/separableconvolve(horizontalkernel:verticalkernel:bias:edgemode:destination:)-6q5ro.md)
  Performs separable convolution on a multiple plane 32-bit pixel buffer.
- [vImage.ConvolutionKernel](vimage/convolutionkernel.md)
  Constants that describe 1D convolution kernels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/separableconvolve(horizontalkernel:verticalkernel:bias:edgemode:destination:)-6t9b3)*