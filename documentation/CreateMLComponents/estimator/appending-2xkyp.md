# appending(_:)

**Framework**: Create ML Components  
**Kind**: method

Composes this estimator with a supervised temporal estimator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func appending<Other>(_ other: Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Other.Annotation> where Other : SupervisedTemporalEstimator, Self.Transformer.Output == Other.Transformer.Input
```

## See Also

- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>>
](estimator/appending(_:)-10qfn.md)
  Composes this estimator with a temporal transformer.
- [func appending<Other>(Other) -> some Estimator<ComposedTransformer<Self.Transformer, Other.Transformer>>
](estimator/appending(_:)-1856y.md)
  Composes this estimator with another estimator.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](estimator/appending(_:)-atvs.md)
  Composes this estimator with a supervised estimator.
- [func appending<Other>(Other) -> some Estimator<ComposedTransformer<Self.Transformer, Other>>
](estimator/appending(_:)-u0ef.md)
  Composes this estimator with a transformer.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>>
](estimator/appending(_:)-w1ek.md)
  Composes this estimator with a temporal estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/estimator/appending(_:)-2xkyp)*