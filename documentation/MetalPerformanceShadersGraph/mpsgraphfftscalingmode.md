# MPSGraphFFTScalingMode

**Framework**: Metal Performance Shaders Graph  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum MPSGraphFFTScalingMode : NSUInteger;
```

## Topics

### Enumeration Cases
- [MPSGraphFFTScalingMode.none](./mpsgraphfftscalingmode/none.md)
  Computes the FFT result with no scaling.
- [MPSGraphFFTScalingMode.size](./mpsgraphfftscalingmode/size.md)
  Scales the FFT result with reciprocal of the total FFT size over all transformed dimensions.
- [MPSGraphFFTScalingMode.unitary](./mpsgraphfftscalingmode/unitary.md)
  Scales the FFT result with reciprocal square root of the total FFT size over all transformed dimensions, resulting in signal strength conserving transformation.
### Initializers
- [init?(rawValue: UInt)](./mpsgraphfftscalingmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphfftscalingmode)*