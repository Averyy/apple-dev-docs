# tentConvolve(kernelSize:edgeMode:destination:)

**Framework**: Accelerate  
**Kind**: method

Convolves an 8-bit planar pixel buffer with a tent filter.

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
func tentConvolve(kernelSize: vImage.Size, edgeMode: vImage.EdgeMode<Pixel_8>, destination: vImage.PixelBuffer<Format>)
```

## Parameters

- `kernelSize`: The convolution kernel size. The operation interprets even dimensions as the next odd number.
- `edgeMode`: The convolution edge mode.
- `destination`: The destination pixel buffer.

## See Also

- [Blurring an image](blurring-an-image.md)
  Filter an image by convolving it with custom and high-speed kernels.
- [func tentConvolve(kernelSize: vImage.Size, edgeMode: vImage.EdgeMode<Pixel_8888>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/tentconvolve(kernelsize:edgemode:destination:)-150xp.md)
  Convolves an 8-bit-per-channel, 4-channel interleaved pixel buffer with a tent filter.
- [func tentConvolved(kernelSize: vImage.Size, edgeMode: vImage.EdgeMode<Pixel_8888>) -> vImage.PixelBuffer<Format>](vimage/pixelbuffer/tentconvolved(kernelsize:edgemode:).md)
  Returns a tent-filter convolved 8-bit-per-channel, 4-channel interleaved pixel buffer.
- [func tentConvolve(kernelSize: vImage.Size, edgeMode: vImage.EdgeMode<Pixel_8>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/tentconvolve(kernelsize:edgemode:destination:)-2dp48.md)
  Convolves a multiple-plane 8-bit-per-channel pixel buffer with a tent filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/tentconvolve(kernelsize:edgemode:destination:)-1fpap)*