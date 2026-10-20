# convolve(with:bias:edgeMode:destination:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS
- watchOS 11.0+

## Declaration

```swift
func convolve(with kernel: vImage.ConvolutionKernel2D<Float>, bias: Float? = nil, edgeMode: vImage.EdgeMode<Pixel_8888>, destination: vImage.PixelBuffer<Format>)
```

Available when `Format` is `vImage.Interleaved8x4`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/convolve(with:bias:edgemode:destination:)-7no5n)*