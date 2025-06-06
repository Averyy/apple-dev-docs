# Transformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsAnnotatedFeatureTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, AnnotatedFeature<Self.Output, Annotation>>
](standardscaler/transformer/adaptedasannotatedfeaturetransformer(annotationtype:).md)
  Returns an annotated-feature transformer that transforms the features using this transformer while leaving the annotations unchanged.
- [func adaptedAsAnnotatedPredictionTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, AnnotatedPrediction<Self.Output, Annotation>>
](standardscaler/transformer/adaptedasannotatedpredictiontransformer(annotationtype:).md)
  Returns an annotated-prediction transformer that transforms the predictions using this transformer while leaving the annotations unchanged.
- [func adaptedAsEstimator() -> TransformerToEstimatorAdaptor<Self>](standardscaler/transformer/adaptedasestimator.md)
  Exposes this transformer as a trivial estimator.
- [func adaptedAsRandomTransformer() -> some RandomTransformer<Self.Input, Self.Output>
](standardscaler/transformer/adaptedasrandomtransformer.md)
  Returns a random transformer wrapping a transformer.
- [func adaptedAsTemporal() -> TemporalAdaptor<Self>](standardscaler/transformer/adaptedastemporal-16ay7.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsTemporal() -> TransformerToTemporalAdaptor<Self>](standardscaler/transformer/adaptedastemporal-r5cz.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsUpdatableEstimator() -> TransformerToUpdatableEstimatorAdaptor<Self>](standardscaler/transformer/adaptedasupdatableestimator.md)
  Exposes this transformer as a trivial estimator.
- [func appending<Other>(Other) -> ComposedTransformer<Self, Other>](standardscaler/transformer/appending(_:)-2bj9y.md)
  Composes this transformer with another transformer.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](standardscaler/transformer/appending(_:)-2pv2t.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](standardscaler/transformer/appending(_:)-367bf.md)
  Composes this transformer with a temporal estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedFeature<Other.Output, Annotation>>
](standardscaler/transformer/appending(_:)-4d3ar.md)
  Composes this transformer with a feature-only transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedEstimator<Self, Other>](standardscaler/transformer/appending(_:)-540ko.md)
  Composes this transformer with an updatable supervised estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self>, Other>](standardscaler/transformer/appending(_:)-666bf.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, Other.Output>
](standardscaler/transformer/appending(_:)-67bxz.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](standardscaler/transformer/appending(_:)-6mn01.md)
  Composes this transformer with an updatable temporal estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedEstimator<Self, Other>](standardscaler/transformer/appending(_:)-7h8yd.md)
  Composes this transformer with a supervised estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, Other.Output>
](standardscaler/transformer/appending(_:)-7kwrq.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableEstimator<Self, Other>](standardscaler/transformer/appending(_:)-8uvj0.md)
  Composes this transformer with an updatable estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TemporalAdaptor<Self>, Other>](standardscaler/transformer/appending(_:)-915ls.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other>(Other) -> PreprocessingEstimator<Self, Other>](standardscaler/transformer/appending(_:)-9955o.md)
  Composes this transformer with an estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](standardscaler/transformer/appending(_:)-9yj0w.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedPrediction<Other.Output, Annotation>>
](standardscaler/transformer/appending(_:)-dugn.md)
  Composes this transformer with a prediction-only transformer.
- [func callAsFunction<S>(S, eventHandler: EventHandler?) async throws -> [Self.Output]](standardscaler/transformer/callasfunction(_:eventhandler:)-1ayi6.md)
  Performs the transformation on a sequence of inputs.
- [func callAsFunction(Self.Input, eventHandler: EventHandler?) async throws -> Self.Output](standardscaler/transformer/callasfunction(_:eventhandler:)-2ur2y.md)
  Performs the transformation on a single input.
- [func export(to: URL) throws](standardscaler/transformer/export(to:).md)
  Exports this transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](standardscaler/transformer/export(to:metadata:).md)
  Exports this transformer as a CoreML model with userInfo.
- [func prediction<S, Label>(from: S) async throws -> [ClassificationDistribution<Label>]](standardscaler/transformer/prediction(from:)-9v48q.md)
  Performs a prediction from a sequence of inputs.
- [func prediction<Label>(from: Self.Input) async throws -> ClassificationDistribution<Label>](standardscaler/transformer/prediction(from:)-cp24.md)
  Performs a prediction from a single input.
- [func prediction<S, Annotation>(from: S, eventHandler: EventHandler?) async throws -> [AnnotatedPrediction<Self.Output, Annotation>]](standardscaler/transformer/prediction(from:eventhandler:).md)
  Performs a prediction on a sequence of annotated inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/standardscaler/transformer/transformer-implementations)*