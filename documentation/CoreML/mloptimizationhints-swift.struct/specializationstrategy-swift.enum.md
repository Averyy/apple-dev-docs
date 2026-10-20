# MLOptimizationHints.SpecializationStrategy

**Framework**: Core ML  
**Kind**: enum  
**Role**: Enumeration

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
- [MLOptimizationHints.SpecializationStrategy.default](./specializationstrategy-swift.enum/default.md)
  The strategy that should work well for most applications.
- [MLOptimizationHints.SpecializationStrategy.fastPrediction](./specializationstrategy-swift.enum/fastprediction.md)
  Prefer the prediction latency at the potential cost of specialization time, memory footprint, and the disk space usage of specialized artifacts.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the specialization strategy
- [var specializationStrategy: MLOptimizationHints.SpecializationStrategy](./specializationstrategy-swift.property.md)
  Optimization strategy for the model specialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mloptimizationhints-swift.struct/specializationstrategy-swift.enum)*