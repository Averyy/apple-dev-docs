# appending(_:)

**Framework**: Create ML Components  
**Kind**: method

Composes this estimator with a transformer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func appending<Other>(_ other: Other) -> some Estimator<ComposedTransformer<Self.Transformer, Other>> where Other : Transformer, Other.Input == Self.Transformer.Output
```

## See Also

- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>>
](estimator/appending(_:)-10qfn.md)
  Composes this estimator with a temporal transformer.
- [func appending<Other>(Other) -> some Estimator<ComposedTransformer<Self.Transformer, Other.Transformer>>
](estimator/appending(_:)-1856y.md)
  Composes this estimator with another estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Other.Annotation>
](estimator/appending(_:)-2xkyp.md)
  Composes this estimator with a supervised temporal estimator.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](estimator/appending(_:)-atvs.md)
  Composes this estimator with a supervised estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>>
](estimator/appending(_:)-w1ek.md)
  Composes this estimator with a temporal estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/estimator/appending(_:)-u0ef)*