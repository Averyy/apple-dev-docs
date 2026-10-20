# MPSGraphOptimizationProfile

**Framework**: Metal Performance Shaders Graph  
**Kind**: enum  
**Role**: Enumeration

The optimization profile used as a heuristic as the graph compiler optimizes the network.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum MPSGraphOptimizationProfile
```

```c
enum MPSGraphOptimizationProfile : uint64_t;
```

## Topics

### Enumeration Cases
- [MPSGraphOptimizationProfile.performance](./mpsgraphoptimizationprofile/performance.md)
  Default, graph optimized for performance.
- [MPSGraphOptimizationProfile.powerEfficiency](./mpsgraphoptimizationprofile/powerefficiency.md)
  Graph optimized for power efficiency.
### Initializers
- [init?(rawValue: UInt64)](./mpsgraphoptimizationprofile/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphoptimizationprofile)*