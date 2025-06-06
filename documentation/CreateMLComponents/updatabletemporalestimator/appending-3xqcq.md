# appending(_:)

**Framework**: Create ML Components  
**Kind**: method

Composes this updatable temporal estimator with an updatable estimator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func appending<Other>(_ other: Other) -> some UpdatableTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>> where Other : UpdatableEstimator, Self.Transformer.Output == Other.Transformer.Input
```

## See Also

- [func appending<Other>(Other) -> some UpdatableTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other>>>
](updatabletemporalestimator/appending(_:)-1qj6y.md)
  Composes this updatable temporal estimator with a transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](updatabletemporalestimator/appending(_:)-6ekr1.md)
  Composes this updatable temporal estimator with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Other.Annotation>
](updatabletemporalestimator/appending(_:)-6j0vp.md)
  Composes this updatable temporal estimator with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> some UpdatableTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>>
](updatabletemporalestimator/appending(_:)-8xn6o.md)
  Composes this updatable temporal estimator with another updatable temporal estimator.
- [func appending<Other>(Other) -> some UpdatableTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other>>
](updatabletemporalestimator/appending(_:)-92r9q.md)
  Composes this updatable temporal estimator with a temporal transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatabletemporalestimator/appending(_:)-3xqcq)*