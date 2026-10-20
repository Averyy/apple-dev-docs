# adaptedAsAnnotatedFeatureTransformer(annotationType:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Returns an annotated-feature transformer that transforms the features using this transformer while leaving the annotations unchanged.

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
func adaptedAsAnnotatedFeatureTransformer<Annotation>(annotationType: Annotation.Type = Annotation.self) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, AnnotatedFeature<Self.Output, Annotation>>
```

## See Also

### Applying and adapting
- [func applied(to: Self.Input, eventHandler: EventHandler?) async throws -> Self.Output](./applied%28to,eventhandler%29.md)
  Performs the transformation on a single input.
- [func adaptedAsAnnotatedPredictionTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, AnnotatedPrediction<Self.Output, Annotation>>
](./adaptedasannotatedpredictiontransformer%28annotationtype%29.md)
  Returns an annotated-prediction transformer that transforms the predictions using this transformer while leaving the annotations unchanged.
- [func adaptedAsEstimator() -> TransformerToEstimatorAdaptor<Self>](./adaptedasestimator%28%29.md)
  Exposes this transformer as a trivial estimator.
- [func adaptedAsRandomTransformer() -> some RandomTransformer<Self.Input, Self.Output>
](./adaptedasrandomtransformer%28%29.md)
  Returns a random transformer wrapping a transformer.
- [func adaptedAsTemporal()](./adaptedastemporal%28%29.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsUpdatableEstimator() -> TransformerToUpdatableEstimatorAdaptor<Self>](./adaptedasupdatableestimator%28%29.md)
  Exposes this transformer as a trivial estimator.
- [associatedtype Input](./input.md)
  The input type.
- [associatedtype Output](./output.md)
  The output type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/transformer/adaptedasannotatedfeaturetransformer(annotationtype:))*