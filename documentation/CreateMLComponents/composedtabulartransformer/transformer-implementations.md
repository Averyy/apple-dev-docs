# Transformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsAnnotatedFeatureTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, AnnotatedFeature<Self.Output, Annotation>>
](composedtabulartransformer/adaptedasannotatedfeaturetransformer(annotationtype:).md)
  Returns an annotated-feature transformer that transforms the features using this transformer while leaving the annotations unchanged.
- [func adaptedAsAnnotatedPredictionTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, AnnotatedPrediction<Self.Output, Annotation>>
](composedtabulartransformer/adaptedasannotatedpredictiontransformer(annotationtype:).md)
  Returns an annotated-prediction transformer that transforms the predictions using this transformer while leaving the annotations unchanged.
- [func adaptedAsRandomTransformer() -> some RandomTransformer<Self.Input, Self.Output>
](composedtabulartransformer/adaptedasrandomtransformer.md)
  Returns a random transformer wrapping a transformer.
- [func adaptedAsTemporal() -> TemporalAdaptor<Self>](composedtabulartransformer/adaptedastemporal-5pgg6.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsTemporal() -> TransformerToTemporalAdaptor<Self>](composedtabulartransformer/adaptedastemporal-8gyw6.md)
  Exposes this transformer as a temporal transformer.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](composedtabulartransformer/appending(_:)-10nc0.md)
  Composes this transformer with a temporal estimator.
- [func appending<Other>(Other) -> PreprocessingEstimator<Self, Other>](composedtabulartransformer/appending(_:)-18xu8.md)
  Composes this transformer with an estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableEstimator<Self, Other>](composedtabulartransformer/appending(_:)-1tkco.md)
  Composes this transformer with an updatable estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedFeature<Other.Output, Annotation>>
](composedtabulartransformer/appending(_:)-2dph5.md)
  Composes this transformer with a feature-only transformer.
- [func appending<Other>(Other) -> ComposedTransformer<Self, Other>](composedtabulartransformer/appending(_:)-2wwf1.md)
  Composes this transformer with another transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](composedtabulartransformer/appending(_:)-3zomn.md)
  Composes this transformer with an updatable temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedEstimator<Self, Other>](composedtabulartransformer/appending(_:)-431a1.md)
  Composes this transformer with an updatable supervised estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](composedtabulartransformer/appending(_:)-5k3w.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self>, Other>](composedtabulartransformer/appending(_:)-6qnp9.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedPrediction<Other.Output, Annotation>>
](composedtabulartransformer/appending(_:)-8ibmd.md)
  Composes this transformer with a prediction-only transformer.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TemporalAdaptor<Self>, Other>](composedtabulartransformer/appending(_:)-8nk9n.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other>(Other) -> PreprocessingSupervisedEstimator<Self, Other>](composedtabulartransformer/appending(_:)-8wt2y.md)
  Composes this transformer with a supervised estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, Other.Output>
](composedtabulartransformer/appending(_:)-99kvx.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, Other.Output>
](composedtabulartransformer/appending(_:)-9t06y.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](composedtabulartransformer/appending(_:)-zaps.md)
  Composes this transformer with a supervised temporal estimator.
- [func export(to: URL) throws](composedtabulartransformer/export(to:)-2rd6c.md)
  Exports this transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](composedtabulartransformer/export(to:metadata:)-85vf4.md)
  Exports this transformer as a CoreML model with userInfo.
- [func prediction<S, Label>(from: S) async throws -> [ClassificationDistribution<Label>]](composedtabulartransformer/prediction(from:)-7njg3.md)
  Performs a prediction from a sequence of inputs.
- [func prediction<Label>(from: Self.Input) async throws -> ClassificationDistribution<Label>](composedtabulartransformer/prediction(from:)-ezs.md)
  Performs a prediction from a single input.
- [func prediction<S, Annotation>(from: S, eventHandler: EventHandler?) async throws -> [AnnotatedPrediction<Self.Output, Annotation>]](composedtabulartransformer/prediction(from:eventhandler:).md)
  Performs a prediction on a sequence of annotated inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/composedtabulartransformer/transformer-implementations)*