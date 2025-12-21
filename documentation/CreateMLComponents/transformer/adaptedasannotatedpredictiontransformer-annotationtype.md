# adaptedAsAnnotatedPredictionTransformer(annotationType:)

**Framework**: Create ML Components  
**Kind**: method

Returns an annotated-prediction transformer that transforms the predictions using this transformer while leaving the annotations unchanged.

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
func adaptedAsAnnotatedPredictionTransformer<Annotation>(annotationType: Annotation.Type = Annotation.self) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, AnnotatedPrediction<Self.Output, Annotation>>
```

## See Also

- [func applied(to: Self.Input, eventHandler: EventHandler?) async throws -> Self.Output](transformer/applied(to:eventhandler:).md)
  Performs the transformation on a single input.
- [func adaptedAsAnnotatedFeatureTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, AnnotatedFeature<Self.Output, Annotation>>
](transformer/adaptedasannotatedfeaturetransformer(annotationtype:).md)
  Returns an annotated-feature transformer that transforms the features using this transformer while leaving the annotations unchanged.
- [func adaptedAsEstimator() -> TransformerToEstimatorAdaptor<Self>](transformer/adaptedasestimator.md)
  Exposes this transformer as a trivial estimator.
- [func adaptedAsRandomTransformer() -> some RandomTransformer<Self.Input, Self.Output>
](transformer/adaptedasrandomtransformer.md)
  Returns a random transformer wrapping a transformer.
- [func adaptedAsTemporal()](transformer/adaptedastemporal.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsUpdatableEstimator() -> TransformerToUpdatableEstimatorAdaptor<Self>](transformer/adaptedasupdatableestimator.md)
  Exposes this transformer as a trivial estimator.
- [associatedtype Input](transformer/input.md)
  The input type.
- [associatedtype Output](transformer/output.md)
  The output type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/transformer/adaptedasannotatedpredictiontransformer(annotationtype:))*