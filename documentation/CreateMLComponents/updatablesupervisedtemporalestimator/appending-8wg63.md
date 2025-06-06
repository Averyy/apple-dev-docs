# appending(_:)

**Framework**: Create ML Components  
**Kind**: method

Composes this updatable supervised temporal estimator with a transformer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func appending<Other>(_ other: Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other>, Self.Annotation> where Other : TemporalTransformer, Other.Input == Self.Transformer.Output
```

## See Also

- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](updatablesupervisedtemporalestimator/appending(_:)-1sjwg.md)
  Composes this updatable supervised temporal estimator with another updatable supervised temporal estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](updatablesupervisedtemporalestimator/appending(_:)-30xpc.md)
  Composes this updatable supervised temporal estimator with an updatable temporal estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other>>, Self.Annotation>
](updatablesupervisedtemporalestimator/appending(_:)-3k3xn.md)
  Composes this updatable supervised temporal estimator with a transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Self.Annotation>
](updatablesupervisedtemporalestimator/appending(_:)-4xdv5.md)
  Composes this updatable supervised temporal estimator with an updatable estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Self.Annotation>
](updatablesupervisedtemporalestimator/appending(_:)-7orql.md)
  Composes this updatable supervised temporal estimator with an updatable supervised estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatablesupervisedtemporalestimator/appending(_:)-8wg63)*