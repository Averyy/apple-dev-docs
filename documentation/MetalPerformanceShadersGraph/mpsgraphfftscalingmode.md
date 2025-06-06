# MPSGraphFFTScalingMode

**Framework**: Metal Performance Shaders Graph  
**Kind**: enum

The scaling modes for Fourier transform operations.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum MPSGraphFFTScalingMode
```

## Topics

### Enumeration Cases
- [MPSGraphFFTScalingMode.none](mpsgraphfftscalingmode/none.md)
  Computes the FFT result with no scaling.
- [MPSGraphFFTScalingMode.size](mpsgraphfftscalingmode/size.md)
  Scales the FFT result with reciprocal of the total FFT size over all transformed dimensions.
- [MPSGraphFFTScalingMode.unitary](mpsgraphfftscalingmode/unitary.md)
  Scales the FFT result with reciprocal square root of the total FFT size over all transformed dimensions, resulting in signal strength conserving transformation.
### Initializers
- [init?(rawValue: UInt)](mpsgraphfftscalingmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphfftscalingmode)*