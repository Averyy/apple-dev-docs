# appending(_:)

**Framework**: Create ML Components  
**Kind**: method

Composes this transformer with an annotated-feature transformer.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func appending<Other, Annotation>(_ other: Other) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, Other.Output> where Other : Transformer, Other.Input == AnnotatedPrediction<Self.Output, Annotation>
```

## See Also

- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](transformer/appending(_:)-13v67.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](transformer/appending(_:)-2bp6m.md)
  Composes this transformer with a temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](transformer/appending(_:)-2i7p8.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableEstimator<Self, Other>](transformer/appending(_:)-4xmcp.md)
  Composes this transformer with an updatable estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, Other.Output>
](transformer/appending(_:)-51wcs.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> ComposedTransformer<Self, Other>](transformer/appending(_:)-6btna.md)
  Composes this transformer with another transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedPrediction<Other.Output, Annotation>>
](transformer/appending(_:)-6fg5q.md)
  Composes this transformer with a prediction-only transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedEstimator<Self, Other>](transformer/appending(_:)-70fmy.md)
  Composes this transformer with an updatable supervised estimator.
- [func appending<Other>(Other) -> PreprocessingEstimator<Self, Other>](transformer/appending(_:)-86js4.md)
  Composes this transformer with an estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedFeature<Other.Output, Annotation>>
](transformer/appending(_:)-8y0df.md)
  Composes this transformer with a feature-only transformer.
- [func appending<Other>(Other) -> PreprocessingSupervisedEstimator<Self, Other>](transformer/appending(_:)-lta.md)
  Composes this transformer with a supervised estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](transformer/appending(_:)-qqh2.md)
  Composes this transformer with an updatable temporal estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self>, Other>](transformer/appending(_:)-wd3u.md)
  Composes this transformer with a temporal transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/transformer/appending(_:)-91f58)*