# tentConvolved(kernelSize:edgeMode:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Returns a tent-filter convolved 8-bit-per-channel, 4-channel interleaved pixel buffer.

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
func tentConvolved(kernelSize: vImage.Size, edgeMode: vImage.EdgeMode<Pixel_8888>) -> vImage.PixelBuffer<Format>
```

Available when `Format` is `vImage.Interleaved8x4`.

## Return Value

A pixel buffer that contains a blurred version of the source pixel buffer.

## Parameters

- `kernelSize`: The convolution kernel size. The operation interprets even dimensions as the next odd number.
- `edgeMode`: The convolution edge mode.

## See Also

### Related Documentation
- [Blurring an image](../../blurring-an-image.md)
  Filter an image by convolving it with custom and high-speed kernels.
### Tent convolution
- [func tentConvolve(kernelSize: vImage.Size, edgeMode: vImage.EdgeMode<Pixel_8>, destination: vImage.PixelBuffer<Format>)](./tentconvolve%28kernelsize,edgemode,destination%29-1fpap.md)
  Convolves an 8-bit planar pixel buffer with a tent filter.
- [func tentConvolve(kernelSize: vImage.Size, edgeMode: vImage.EdgeMode<Pixel_8888>, destination: vImage.PixelBuffer<Format>)](./tentconvolve%28kernelsize,edgemode,destination%29-150xp.md)
  Convolves an 8-bit-per-channel, 4-channel interleaved pixel buffer with a tent filter.
- [func tentConvolve(kernelSize: vImage.Size, edgeMode: vImage.EdgeMode<Pixel_8>, destination: vImage.PixelBuffer<Format>)](./tentconvolve%28kernelsize,edgemode,destination%29-2dp48.md)
  Convolves a multiple-plane 8-bit-per-channel pixel buffer with a tent filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/tentconvolved(kernelsize:edgemode:))*