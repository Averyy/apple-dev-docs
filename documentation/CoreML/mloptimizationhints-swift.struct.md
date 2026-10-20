# MLOptimizationHints

**Framework**: Core ML  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.0+
- watchOS 10.4+

## Declaration

```swift
struct MLOptimizationHints
```

## Topics

### Creating optimization hints
- [init()](./mloptimizationhints-swift.struct/init%28%29.md)
  Construct an MLOptimizationHints
### Getting the reshape frequency
- [var reshapeFrequency: MLOptimizationHints.ReshapeFrequency](./mloptimizationhints-swift.struct/reshapefrequency-swift.property.md)
  The anticipated reshape frequency
- [MLOptimizationHints.ReshapeFrequency](./mloptimizationhints-swift.struct/reshapefrequency-swift.enum.md)
  The anticipated frequency of changing input shapes.
### Getting the specialization strategy
- [var specializationStrategy: MLOptimizationHints.SpecializationStrategy](./mloptimizationhints-swift.struct/specializationstrategy-swift.property.md)
  Optimization strategy for the model specialization.
- [MLOptimizationHints.SpecializationStrategy](./mloptimizationhints-swift.struct/specializationstrategy-swift.enum.md)
  The optimization strategy for the model specialization.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [class MLModelConfiguration](./mlmodelconfiguration.md)
  The settings for creating or updating a machine learning model.
- [class MLKey](./mlkey.md)
  An abstract base class for machine learning key types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mloptimizationhints-swift.struct)*