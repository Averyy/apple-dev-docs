# separableConvolve(horizontalKernel:verticalKernel:bias:edgeMode:destination:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Performs separable convolution on a multiple plane 8-bit pixel buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
func separableConvolve(horizontalKernel: [Float], verticalKernel: [Float], bias: Float = 0, edgeMode: vImage.EdgeMode<Pixel_16U>, destination: vImage.PixelBuffer<Format>)
```

Available when `Format` conforms to `MultiplePlanePixelFormat` and `Format.ComponentType` is `UInt8`.

## Discussion

The following code shows how to generate a multiplane pixel buffer from a [`CGImage`](../../../CoreGraphics/cgimage.md) instance and apply a Gaussian blur using separable convolution:

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
- `edgeMode`: The convolution edge mode. The background color must be a single [`Pixel_F`](../../pixel_f.md) value.
- `destination`: The destination pixel buffer.

## See Also

### Related Documentation
- [Blurring an image](../../blurring-an-image.md)
  Filter an image by convolving it with custom and high-speed kernels.
### Separable convolution
- [func separableConvolve(horizontalKernel: [Float], verticalKernel: [Float], bias: Float, edgeMode: vImage.EdgeMode<Pixel_16U>, destination: vImage.PixelBuffer<Format>)](./separableconvolve%28horizontalkernel,verticalkernel,bias,edgemode,destination%29-2iyq6.md)
  Performs separable convolution on an 8-bit planar pixel buffer.
- [func separableConvolve(horizontalKernel: [Float], verticalKernel: [Float], bias: Float, edgeMode: vImage.EdgeMode<Pixel_16F>, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](./separableconvolve%28horizontalkernel,verticalkernel,bias,edgemode,usefloat16accumulator,destination%29.md)
  Performs separable convolution on a 16-bit planar pixel buffer.
- [func separableConvolve(horizontalKernel: [Float], verticalKernel: [Float], bias: Float, edgeMode: vImage.EdgeMode<Pixel_F>, destination: vImage.PixelBuffer<Format>)](./separableconvolve%28horizontalkernel,verticalkernel,bias,edgemode,destination%29-2qofv.md)
  Performs separable convolution on a 32-bit planar pixel buffer.
- [func separableConvolve(horizontalKernel: [Float], verticalKernel: [Float], bias: Float, edgeMode: vImage.EdgeMode<Pixel_F>, destination: vImage.PixelBuffer<Format>)](./separableconvolve%28horizontalkernel,verticalkernel,bias,edgemode,destination%29-6q5ro.md)
  Performs separable convolution on a multiple plane 32-bit pixel buffer.
- [vImage.ConvolutionKernel](../convolutionkernel.md)
  Constants that describe 1D convolution kernels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/separableconvolve(horizontalkernel:verticalkernel:bias:edgemode:destination:)-6t9b3)*