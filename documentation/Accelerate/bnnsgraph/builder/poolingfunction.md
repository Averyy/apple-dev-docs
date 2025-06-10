# BNNSGraph.Builder.PoolingFunction

**Framework**: Accelerate  
**Kind**: enum

The pooling function

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
enum PoolingFunction
```

## Topics

### Enumeration Cases
- [BNNSGraph.Builder.PoolingFunction.average(includePadding:)](bnnsgraph/builder/poolingfunction/average(includepadding:).md)
  A function for pooling that computes the average of each element in the pooling kernel.
- [BNNSGraph.Builder.PoolingFunction.l2Norm](bnnsgraph/builder/poolingfunction/l2norm.md)
  A function for pooling that computes the square root of the sum of squares of each element in the pooling kernel.
- [BNNSGraph.Builder.PoolingFunction.max](bnnsgraph/builder/poolingfunction/max.md)
  A function for pooling that computes the maximum of each element in the pooling kernel.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/poolingfunction)*