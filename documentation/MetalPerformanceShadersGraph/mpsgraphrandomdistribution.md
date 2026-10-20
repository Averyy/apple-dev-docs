# MPSGraphRandomDistribution

**Framework**: Metal Performance Shaders Graph  
**Kind**: enum  
**Role**: Enumeration

The distributions supported by random operations.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum MPSGraphRandomDistribution
```

```c
enum MPSGraphRandomDistribution : uint64_t;
```

## Topics

### Enumeration Cases
- [MPSGraphRandomDistribution.normal](./mpsgraphrandomdistribution/normal.md)
  The normal distribution defined by mean and standard deviation.
- [MPSGraphRandomDistribution.truncatedNormal](./mpsgraphrandomdistribution/truncatednormal.md)
  The normal distribution defined by mean and standard deviation, truncated to the range [min, max)
- [MPSGraphRandomDistribution.uniform](./mpsgraphrandomdistribution/uniform.md)
  The uniform distribution, with samples drawn uniformly from [min, max) for float types, and [min, max] for integer types.
### Initializers
- [init?(rawValue: UInt64)](./mpsgraphrandomdistribution/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphrandomdistribution)*