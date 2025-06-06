# appending(_:)

**Framework**: Create ML Components  
**Kind**: method

Composes this temporal transformer with an updatable estimator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func appending<Other>(_ other: Other) -> PreprocessingUpdatableTemporalEstimator<Self, UpdatableEstimatorToTemporalAdaptor<Other>> where Other : UpdatableEstimator, Self.Output == Other.Transformer.Input
```

## See Also

- [func appending<Other>(Other) -> ComposedTemporalTransformer<Self, TransformerToTemporalAdaptor<Other>>](temporaltransformer/appending(_:)-3vdcn.md)
  Composes this temporal transformer with a transformer.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<Self, Other>](temporaltransformer/appending(_:)-7pna8.md)
  Composes this temporal transformer with another temporal transformer.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<Self, Other>](temporaltransformer/appending(_:)-152om.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<Self, Other>](temporaltransformer/appending(_:)-1pxxi.md)
  Composes this temporal transformer with an updatable temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<Self, UpdatableSupervisedEstimatorToTemporalAdaptor<Other>>](temporaltransformer/appending(_:)-2w0z6.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<Self, Other>](temporaltransformer/appending(_:)-68mym.md)
  Composes this temporal transformer with a temporal estimator.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<Self, EstimatorToTemporalAdaptor<Other>>](temporaltransformer/appending(_:)-6pxsk.md)
  Composes this temporal transformer with an estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<Self, SupervisedEstimatorToTemporalAdaptor<Other>>](temporaltransformer/appending(_:)-70exs.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<Self, Other>](temporaltransformer/appending(_:)-9jeg2.md)
  Composes this transformer with an updatable supervised temporal estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporaltransformer/appending(_:)-703rv)*