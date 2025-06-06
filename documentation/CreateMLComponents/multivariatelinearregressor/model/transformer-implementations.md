# Transformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsAnnotatedFeatureTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, AnnotatedFeature<Self.Output, Annotation>>
](multivariatelinearregressor/model/adaptedasannotatedfeaturetransformer(annotationtype:).md)
  Returns an annotated-feature transformer that transforms the features using this transformer while leaving the annotations unchanged.
- [func adaptedAsAnnotatedPredictionTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, AnnotatedPrediction<Self.Output, Annotation>>
](multivariatelinearregressor/model/adaptedasannotatedpredictiontransformer(annotationtype:).md)
  Returns an annotated-prediction transformer that transforms the predictions using this transformer while leaving the annotations unchanged.
- [func adaptedAsEstimator() -> TransformerToEstimatorAdaptor<Self>](multivariatelinearregressor/model/adaptedasestimator.md)
  Exposes this transformer as a trivial estimator.
- [func adaptedAsRandomTransformer() -> some RandomTransformer<Self.Input, Self.Output>
](multivariatelinearregressor/model/adaptedasrandomtransformer.md)
  Returns a random transformer wrapping a transformer.
- [func adaptedAsTemporal() -> TemporalAdaptor<Self>](multivariatelinearregressor/model/adaptedastemporal.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsUpdatableEstimator() -> TransformerToUpdatableEstimatorAdaptor<Self>](multivariatelinearregressor/model/adaptedasupdatableestimator.md)
  Exposes this transformer as a trivial estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](multivariatelinearregressor/model/appending(_:)-1uhfk.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedFeature<Other.Output, Annotation>>
](multivariatelinearregressor/model/appending(_:)-2oond.md)
  Composes this transformer with a feature-only transformer.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self>, Other>](multivariatelinearregressor/model/appending(_:)-2vu89.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TemporalAdaptor<Self>, Other>](multivariatelinearregressor/model/appending(_:)-3tk9s.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedEstimator<Self, Other>](multivariatelinearregressor/model/appending(_:)-421ao.md)
  Composes this transformer with an updatable supervised estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableEstimator<Self, Other>](multivariatelinearregressor/model/appending(_:)-62zda.md)
  Composes this transformer with an updatable estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedPrediction<Other.Output, Annotation>>
](multivariatelinearregressor/model/appending(_:)-6jidc.md)
  Composes this transformer with a prediction-only transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, Other.Output>
](multivariatelinearregressor/model/appending(_:)-6lizu.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> PreprocessingEstimator<Self, Other>](multivariatelinearregressor/model/appending(_:)-79fki.md)
  Composes this transformer with an estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedEstimator<Self, Other>](multivariatelinearregressor/model/appending(_:)-7h92e.md)
  Composes this transformer with a supervised estimator.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](multivariatelinearregressor/model/appending(_:)-7te03.md)
  Composes this transformer with a temporal estimator.
- [func appending<Other>(Other) -> ComposedTransformer<Self, Other>](multivariatelinearregressor/model/appending(_:)-88cz6.md)
  Composes this transformer with another transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, Other.Output>
](multivariatelinearregressor/model/appending(_:)-93ddq.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](multivariatelinearregressor/model/appending(_:)-960m9.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](multivariatelinearregressor/model/appending(_:)-98i8r.md)
  Composes this transformer with an updatable temporal estimator.
- [func callAsFunction<S>(S, eventHandler: EventHandler?) async throws -> [Self.Output]](multivariatelinearregressor/model/callasfunction(_:eventhandler:)-30uv5.md)
  Performs the transformation on a sequence of inputs.
- [func callAsFunction(Self.Input, eventHandler: EventHandler?) async throws -> Self.Output](multivariatelinearregressor/model/callasfunction(_:eventhandler:)-7g333.md)
  Performs the transformation on a single input.
- [func export(to: URL) throws](multivariatelinearregressor/model/export(to:).md)
  Exports this transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](multivariatelinearregressor/model/export(to:metadata:).md)
  Exports this transformer as a CoreML model with userInfo.
- [func prediction<Label>(from: Self.Input) async throws -> ClassificationDistribution<Label>](multivariatelinearregressor/model/prediction(from:)-1duq6.md)
  Performs a prediction from a single input.
- [func prediction<S, Label>(from: S) async throws -> [ClassificationDistribution<Label>]](multivariatelinearregressor/model/prediction(from:)-76sni.md)
  Performs a prediction from a sequence of inputs.
- [func prediction<S, Annotation>(from: S, eventHandler: EventHandler?) async throws -> [AnnotatedPrediction<Self.Output, Annotation>]](multivariatelinearregressor/model/prediction(from:eventhandler:).md)
  Performs a prediction on a sequence of annotated inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multivariatelinearregressor/model/transformer-implementations)*