# Transformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsAnnotatedFeatureTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, AnnotatedFeature<Self.Output, Annotation>>
](poseselector/adaptedasannotatedfeaturetransformer(annotationtype:).md)
  Returns an annotated-feature transformer that transforms the features using this transformer while leaving the annotations unchanged.
- [func adaptedAsAnnotatedPredictionTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, AnnotatedPrediction<Self.Output, Annotation>>
](poseselector/adaptedasannotatedpredictiontransformer(annotationtype:).md)
  Returns an annotated-prediction transformer that transforms the predictions using this transformer while leaving the annotations unchanged.
- [func adaptedAsEstimator() -> TransformerToEstimatorAdaptor<Self>](poseselector/adaptedasestimator.md)
  Exposes this transformer as a trivial estimator.
- [func adaptedAsRandomTransformer() -> some RandomTransformer<Self.Input, Self.Output>
](poseselector/adaptedasrandomtransformer.md)
  Returns a random transformer wrapping a transformer.
- [func adaptedAsTemporal() -> TransformerToTemporalAdaptor<Self>](poseselector/adaptedastemporal.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsUpdatableEstimator() -> TransformerToUpdatableEstimatorAdaptor<Self>](poseselector/adaptedasupdatableestimator.md)
  Exposes this transformer as a trivial estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, Other.Output>
](poseselector/appending(_:)-1yn6b.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](poseselector/appending(_:)-2xu5i.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedFeature<Other.Output, Annotation>>
](poseselector/appending(_:)-4wcf0.md)
  Composes this transformer with a feature-only transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedEstimator<Self, Other>](poseselector/appending(_:)-56e9c.md)
  Composes this transformer with an updatable supervised estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](poseselector/appending(_:)-5hwfz.md)
  Composes this transformer with an updatable temporal estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedEstimator<Self, Other>](poseselector/appending(_:)-5igpa.md)
  Composes this transformer with a supervised estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedPrediction<Other.Output, Annotation>>
](poseselector/appending(_:)-614ff.md)
  Composes this transformer with a prediction-only transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableEstimator<Self, Other>](poseselector/appending(_:)-63ksc.md)
  Composes this transformer with an updatable estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TemporalAdaptor<Self>, Other>](poseselector/appending(_:)-653r7.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](poseselector/appending(_:)-6v9xr.md)
  Composes this transformer with a temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](poseselector/appending(_:)-6yrds.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self>, Other>](poseselector/appending(_:)-7257v.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other>(Other) -> ComposedTransformer<Self, Other>](poseselector/appending(_:)-838ve.md)
  Composes this transformer with another transformer.
- [func appending<Other>(Other) -> PreprocessingEstimator<Self, Other>](poseselector/appending(_:)-8e4wh.md)
  Composes this transformer with an estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, Other.Output>
](poseselector/appending(_:)-9jz7l.md)
  Composes this transformer with an annotated-feature transformer.
- [func callAsFunction<S>(S, eventHandler: EventHandler?) async throws -> [Self.Output]](poseselector/callasfunction(_:eventhandler:)-2qijy.md)
  Performs the transformation on a sequence of inputs.
- [func callAsFunction(Self.Input, eventHandler: EventHandler?) async throws -> Self.Output](poseselector/callasfunction(_:eventhandler:)-5k6q8.md)
  Performs the transformation on a single input.
- [func export(to: URL) throws](poseselector/export(to:).md)
  Exports this transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](poseselector/export(to:metadata:).md)
  Exports this transformer as a CoreML model with userInfo.
- [func prediction<S, Label>(from: S) async throws -> [ClassificationDistribution<Label>]](poseselector/prediction(from:)-5ytfj.md)
  Performs a prediction from a sequence of inputs.
- [func prediction<Label>(from: Self.Input) async throws -> ClassificationDistribution<Label>](poseselector/prediction(from:)-89amf.md)
  Performs a prediction from a single input.
- [func prediction<S, Annotation>(from: S, eventHandler: EventHandler?) async throws -> [AnnotatedPrediction<Self.Output, Annotation>]](poseselector/prediction(from:eventhandler:).md)
  Performs a prediction on a sequence of annotated inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/poseselector/transformer-implementations)*