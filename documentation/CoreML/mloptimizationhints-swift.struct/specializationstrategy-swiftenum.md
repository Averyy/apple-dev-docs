# MLOptimizationHints.SpecializationStrategy

**Framework**: Core ML  
**Kind**: enum

The optimization strategy for the model specialization.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
enum SpecializationStrategy
```

## Topics

### Enumeration Cases
- [MLOptimizationHints.SpecializationStrategy.default](mloptimizationhints-swift.struct/specializationstrategy-swift.enum/default.md)
  The strategy that should work well for most applications.
- [MLOptimizationHints.SpecializationStrategy.fastPrediction](mloptimizationhints-swift.struct/specializationstrategy-swift.enum/fastprediction.md)
  Prefer the prediction latency at the potential cost of specialization time, memory footprint, and the disk space usage of specialized artifacts.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mloptimizationhints-swift.struct/specializationstrategy-swift.enum)*