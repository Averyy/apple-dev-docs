# appending(_:)

**Framework**: Create ML Components  
**Kind**: method

Composes this temporal estimator with another temporal estimator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func appending<Other>(_ other: Other) -> some TemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>> where Other : TemporalEstimator, Self.Transformer.Output == Other.Transformer.Input
```

## See Also

- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other>>
](temporalestimator/appending(_:)-3ywtc.md)
  Composes this temporal estimator with a temporal transformer.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](temporalestimator/appending(_:)-40b0.md)
  Composes this temporal estimator with a supervised temporal estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>>
](temporalestimator/appending(_:)-43khh.md)
  Composes this temporal estimator with an estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other>>>
](temporalestimator/appending(_:)-5bepa.md)
  Composes this temporal estimator with a transformer.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Other.Annotation>
](temporalestimator/appending(_:)-90283.md)
  Composes this temporal estimator with a supervised temporal estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporalestimator/appending(_:)-933dy)*