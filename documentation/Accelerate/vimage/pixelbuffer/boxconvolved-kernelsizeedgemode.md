# boxConvolved(kernelSize:edgeMode:)

**Framework**: Accelerate  
**Kind**: method

Returns a box-filter convolved 8-bit-per-channel, 4-channel interleaved pixel buffer.

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
func boxConvolved(kernelSize: vImage.Size, edgeMode: vImage.EdgeMode<Pixel_8888>) -> vImage.PixelBuffer<Format>
```

#### Return Value

A pixel buffer that contains a blurred version of the source pixel buffer.

## Parameters

- `kernelSize`: The convolution kernel size. The operation interprets even dimensions as the next odd number.
- `edgeMode`: The convolution edge mode.

## See Also

- [Blurring an image](blurring-an-image.md)
  Filter an image by convolving it with custom and high-speed kernels.
- [func boxConvolve(kernelSize: vImage.Size, edgeMode: vImage.EdgeMode<Pixel_8>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/boxconvolve(kernelsize:edgemode:destination:)-2h7fy.md)
  Convolves an 8-bit planar pixel buffer with a box filter.
- [func boxConvolve(kernelSize: vImage.Size, edgeMode: vImage.EdgeMode<Pixel_8888>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/boxconvolve(kernelsize:edgemode:destination:)-2m20d.md)
  Convolves an 8-bit-per-channel, 4-channel interleaved pixel buffer with a box filter.
- [func boxConvolve(kernelSize: vImage.Size, edgeMode: vImage.EdgeMode<Pixel_8>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/boxconvolve(kernelsize:edgemode:destination:)-3kabm.md)
  Convolves a multiple-plane 8-bit-per-channel pixel buffer with a box filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/boxconvolved(kernelsize:edgemode:))*