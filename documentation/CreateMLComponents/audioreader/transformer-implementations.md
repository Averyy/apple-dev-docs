# Transformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsAnnotatedFeatureTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, AnnotatedFeature<Self.Output, Annotation>>
](audioreader/adaptedasannotatedfeaturetransformer(annotationtype:).md)
  Returns an annotated-feature transformer that transforms the features using this transformer while leaving the annotations unchanged.
- [func adaptedAsAnnotatedPredictionTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, AnnotatedPrediction<Self.Output, Annotation>>
](audioreader/adaptedasannotatedpredictiontransformer(annotationtype:).md)
  Returns an annotated-prediction transformer that transforms the predictions using this transformer while leaving the annotations unchanged.
- [func adaptedAsEstimator() -> TransformerToEstimatorAdaptor<Self>](audioreader/adaptedasestimator.md)
  Exposes this transformer as a trivial estimator.
- [func adaptedAsRandomTransformer() -> some RandomTransformer<Self.Input, Self.Output>
](audioreader/adaptedasrandomtransformer.md)
  Returns a random transformer wrapping a transformer.
- [func adaptedAsTemporal() -> TransformerToTemporalAdaptor<Self>](audioreader/adaptedastemporal.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsUpdatableEstimator() -> TransformerToUpdatableEstimatorAdaptor<Self>](audioreader/adaptedasupdatableestimator.md)
  Exposes this transformer as a trivial estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TemporalAdaptor<Self>, Other>](audioreader/appending(_:)-1u0xu.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedFeature<Other.Output, Annotation>>
](audioreader/appending(_:)-26ps2.md)
  Composes this transformer with a feature-only transformer.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self>, Other>](audioreader/appending(_:)-3gmt7.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableEstimator<Self, Other>](audioreader/appending(_:)-4kjju.md)
  Composes this transformer with an updatable estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](audioreader/appending(_:)-4nrto.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](audioreader/appending(_:)-6gsrw.md)
  Composes this transformer with a temporal estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedEstimator<Self, Other>](audioreader/appending(_:)-7eky7.md)
  Composes this transformer with a supervised estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedEstimator<Self, Other>](audioreader/appending(_:)-7hblg.md)
  Composes this transformer with an updatable supervised estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, Other.Output>
](audioreader/appending(_:)-7os44.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](audioreader/appending(_:)-7va8u.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingEstimator<Self, Other>](audioreader/appending(_:)-8ltrh.md)
  Composes this transformer with an estimator.
- [func appending<Other>(Other) -> ComposedTransformer<Self, Other>](audioreader/appending(_:)-92zfv.md)
  Composes this transformer with another transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](audioreader/appending(_:)-9xhmy.md)
  Composes this transformer with an updatable temporal estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, Other.Output>
](audioreader/appending(_:)-dl98.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedPrediction<Other.Output, Annotation>>
](audioreader/appending(_:)-u9cr.md)
  Composes this transformer with a prediction-only transformer.
- [func callAsFunction(Self.Input, eventHandler: EventHandler?) async throws -> Self.Output](audioreader/callasfunction(_:eventhandler:)-6330i.md)
  Performs the transformation on a single input.
- [func callAsFunction<S>(S, eventHandler: EventHandler?) async throws -> [Self.Output]](audioreader/callasfunction(_:eventhandler:)-88yk1.md)
  Performs the transformation on a sequence of inputs.
- [func export(to: URL) throws](audioreader/export(to:).md)
  Exports this transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](audioreader/export(to:metadata:).md)
  Exports this transformer as a CoreML model with userInfo.
- [func prediction<Label>(from: Self.Input) async throws -> ClassificationDistribution<Label>](audioreader/prediction(from:)-16ffq.md)
  Performs a prediction from a single input.
- [func prediction<S, Label>(from: S) async throws -> [ClassificationDistribution<Label>]](audioreader/prediction(from:)-5h6ox.md)
  Performs a prediction from a sequence of inputs.
- [func prediction<S, Annotation>(from: S, eventHandler: EventHandler?) async throws -> [AnnotatedPrediction<Self.Output, Annotation>]](audioreader/prediction(from:eventhandler:).md)
  Performs a prediction on a sequence of annotated inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/audioreader/transformer-implementations)*