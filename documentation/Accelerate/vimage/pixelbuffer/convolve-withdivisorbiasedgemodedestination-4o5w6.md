# convolve(with:divisor:bias:edgeMode:destination:)

**Framework**: Accelerate  
**Kind**: method

Convolves an 8-bit planar pixel buffer.

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
func convolve(with kernel: vImage.ConvolutionKernel2D<Int16>, divisor: Int32?, bias: Int32? = nil, edgeMode: vImage.EdgeMode<Pixel_8>, destination: vImage.PixelBuffer<Format>)
```

## Parameters

- `kernel`: The convolution kernel.
- `divisor`: A value that the operation divides the results of the convolution by. Pass   to specify that the function calculates the divisor as the sum of the kernel values.
- `bias`: An optional value that the operation adds to the sum of weighted pixels before it applies the divisor.
- `edgeMode`: The convolution edge mode.
- `destination`: The destination pixel buffer.

## See Also

- [Blurring an image](blurring-an-image.md)
  Filter an image by convolving it with custom and high-speed kernels.
- [func convolve(with: vImage.ConvolutionKernel2D<Float>, bias: Float?, edgeMode: vImage.EdgeMode<Pixel_16F>, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/convolve(with:bias:edgemode:usefloat16accumulator:destination:)-1xkvu.md)
  Convolves a floating-point 16-bit planar pixel buffer.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/convolve(with:divisor:bias:edgemode:destination:)-4o5w6)*