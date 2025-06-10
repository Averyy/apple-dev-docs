# convolve(with:bias:edgeMode:useFloat16Accumulator:destination:)

**Framework**: Accelerate  
**Kind**: method

Convolves a floating-point 16-bit planar pixel buffer.

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
func convolve(with kernel: vImage.ConvolutionKernel2D<Float>, bias: Float? = nil, edgeMode: vImage.EdgeMode<Pixel_16F>, useFloat16Accumulator: Bool = false, destination: vImage.PixelBuffer<Format>)
```

## Parameters

- `kernel`: The convolution kernel.
- `bias`: An optional value that the operation adds to the sum of weighted pixels before it applies the divisor.
- `edgeMode`: The convolution edge mode.
- `useFloat16Accumulator`: A Boolean value that specifies that the function uses faster but lower-precision internal arithmetic. For more information, see  .
- `destination`: The destination pixel buffer.

## See Also

- [Blurring an image](blurring-an-image.md)
  Filter an image by convolving it with custom and high-speed kernels.
- [func convolve(with: vImage.ConvolutionKernel2D<Int16>, divisor: Int32?, bias: Int32?, edgeMode: vImage.EdgeMode<Pixel_8>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/convolve(with:divisor:bias:edgemode:destination:)-4o5w6.md)
  Convolves an 8-bit planar pixel buffer.
- [func convolve(with: vImage.ConvolutionKernel2D<Float>, bias: Float?, edgeMode: vImage.EdgeMode<Pixel_F>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/convolve(with:bias:edgemode:destination:)-tn07.md)
  Convolves a 32-bit planar pixel buffer.
- [func convolve(with: vImage.ConvolutionKernel2D<Int16>, divisor: Int32?, bias: Int32?, edgeMode: vImage.EdgeMode<Pixel_8888>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/convolve(with:divisor:bias:edgemode:destination:)-1oul9.md)
  Convolves an 8-bit-per-channel, 4-channel interleaved pixel buffer.
- [func convolve(with: (vImage.ConvolutionKernel2D<Int16>, vImage.ConvolutionKernel2D<Int16>, vImage.ConvolutionKernel2D<Int16>, vImage.ConvolutionKernel2D<Int16>), divisors: (Int32, Int32, Int32, Int32)?, biases: (Int32, Int32, Int32, Int32), edgeMode: vImage.EdgeMode<Pixel_8888>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/convolve(with:divisors:biases:edgemode:destination:).md)
  Convolves an 8-bit-per-channel, 4-channel interleaved pixel buffer with separate kernels for each channel.
- [func convolve(with: vImage.ConvolutionKernel2D<Float>, bias: Float?, edgeMode: vImage.EdgeMode<Pixel_ARGB_16F>, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/convolve(with:bias:edgemode:usefloat16accumulator:destination:)-81lqa.md)
  Convolves a floating-point 16-bit-per-channel, 4-channel interleaved pixel buffer.
- [func convolve(with: vImage.ConvolutionKernel2D<Float>, bias: Float?, edgeMode: vImage.EdgeMode<Pixel_FFFF>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/convolve(with:bias:edgemode:destination:)-8syhw.md)
  Convolves a 32-bit-per-channel, 4-channel interleaved pixel buffer.
- [func convolve(with: vImage.ConvolutionKernel2D<Int16>, divisor: Int32?, bias: Int32?, edgeMode: vImage.EdgeMode<Pixel_8>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/convolve(with:divisor:bias:edgemode:destination:)-4jjbx.md)
  Convolves an 8-bit multiple plane pixel buffer.
- [func convolve(with: vImage.ConvolutionKernel2D<Float>, bias: Float?, edgeMode: vImage.EdgeMode<Pixel_F>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/convolve(with:bias:edgemode:destination:)-3219s.md)
  Convolves a 32-bit multiple plane pixel buffer.
- [vImage.EdgeMode](vimage/edgemode.md)
  Constants that specify edge modes for convolution operations.
- [vImage.ConvolutionKernel2D](vimage/convolutionkernel2d.md)
  A 2D matrix that represents a convolution kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/convolve(with:bias:edgemode:usefloat16accumulator:destination:)-1xkvu)*