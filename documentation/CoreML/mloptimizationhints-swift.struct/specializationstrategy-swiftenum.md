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

### Specialization strategies
- [MLOptimizationHints.SpecializationStrategy.default](mloptimizationhints-swift.struct/specializationstrategy-swift.enum/default.md)
  The strategy that should work well for most applications.
- [MLOptimizationHints.SpecializationStrategy.fastPrediction](mloptimizationhints-swift.struct/specializationstrategy-swift.enum/fastprediction.md)
  Prefer the prediction latency at the potential cost of specialization time, memory footprint, and the disk space usage of specialized artifacts.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var specializationStrategy: MLOptimizationHints.SpecializationStrategy](mloptimizationhints-swift.struct/specializationstrategy-swift.property.md)
  Optimization strategy for the model specialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mloptimizationhints-swift.struct/specializationstrategy-swift.enum)*