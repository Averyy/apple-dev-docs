# BNNSGraph.Builder.PoolingFunction

**Framework**: Accelerate  
**Kind**: enum  
**Role**: Enumeration

The pooling function

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
enum PoolingFunction
```

## Topics

### Enumeration Cases
- [BNNSGraph.Builder.PoolingFunction.average(includePadding:)](./poolingfunction/average%28includepadding%29.md)
  A function for pooling that computes the average of each element in the pooling kernel.
- [BNNSGraph.Builder.PoolingFunction.l2Norm](./poolingfunction/l2norm.md)
  A function for pooling that computes the square root of the sum of squares of each element in the pooling kernel.
- [BNNSGraph.Builder.PoolingFunction.max](./poolingfunction/max.md)
  A function for pooling that computes the maximum of each element in the pooling kernel.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/poolingfunction)*