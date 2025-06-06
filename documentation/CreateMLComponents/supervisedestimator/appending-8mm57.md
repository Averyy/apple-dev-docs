# appending(_:)

**Framework**: Create ML Components  
**Kind**: method

Composes this supervised estimator with a temporal estimator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@preconcurrency
func appending<Other>(_ other: Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation> where Other : TemporalEstimator, Self.Annotation : Sendable, Self.Transformer.Output == Other.Transformer.Input
```

## See Also

- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](supervisedestimator/appending(_:)-2436m.md)
  Composes this supervised estimator with a supervised temporal estimator.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](supervisedestimator/appending(_:)-36sou.md)
  Composes this supervised estimator with another supervised estimator.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](supervisedestimator/appending(_:)-48wwd.md)
  Composes this supervised estimator with an estimator.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other>, Self.Annotation>
](supervisedestimator/appending(_:)-629ia.md)
  Composes this supervised estimator with a transformer.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>, Self.Annotation>
](supervisedestimator/appending(_:)-m18k.md)
  Composes this supervised estimator with a temporal transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/supervisedestimator/appending(_:)-8mm57)*