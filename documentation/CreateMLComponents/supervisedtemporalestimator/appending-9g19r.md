# appending(_:)

**Framework**: Create ML Components  
**Kind**: method

Composes this supervised temporal estimator with a transformer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func appending<Other>(_ other: Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other>>, Self.Annotation> where Other : Transformer, Other.Input == Self.Transformer.Output
```

## See Also

- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Self.Annotation>
](supervisedtemporalestimator/appending(_:)-1vtjj.md)
  Composes this supervised temporal estimator with a supervised estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other>, Self.Annotation>
](supervisedtemporalestimator/appending(_:)-3xipm.md)
  Composes this supervised temporal estimator with a transformer.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](supervisedtemporalestimator/appending(_:)-4a6ux.md)
  Composes this supervised temporal estimator with another supervised temporal estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](supervisedtemporalestimator/appending(_:)-4km9v.md)
  Composes this supervised temporal estimator with a temporal estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Self.Annotation>
](supervisedtemporalestimator/appending(_:)-4vdf2.md)
  Composes this supervised temporal estimator with an estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/supervisedtemporalestimator/appending(_:)-9g19r)*