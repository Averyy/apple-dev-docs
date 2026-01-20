# init(coder:device:)

**Framework**: Metal Performance Shaders  
**Kind**: init

Initializes a transposed convolution kernel.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init?(coder aDecoder: NSCoder, device: any MTLDevice)
```

## See Also

- [init(device: any MTLDevice, weights: any MPSCNNConvolutionDataSource)](mpscnnconvolutiontranspose/init(device:weights:).md)
  Initializes a transposed convolution kernel.
- [protocol MPSCNNConvolutionDataSource](mpscnnconvolutiondatasource.md)
  The protocol that provides convolution filter weights and bias terms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiontranspose/init(coder:device:))*