# MPSGraphOptimizationProfile

**Framework**: Metal Performance Shaders Graph  
**Kind**: enum

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

## Topics

### Enumeration Cases
- [MPSGraphOptimizationProfile.performance](mpsgraphoptimizationprofile/performance.md)
  Default, graph optimized for performance.
- [MPSGraphOptimizationProfile.powerEfficiency](mpsgraphoptimizationprofile/powerefficiency.md)
  Graph optimized for power efficiency.
### Initializers
- [init?(rawValue: UInt64)](mpsgraphoptimizationprofile/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphoptimizationprofile)*