# Transformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsAnnotatedFeatureTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, AnnotatedFeature<Self.Output, Annotation>>
](imputetransformer/adaptedasannotatedfeaturetransformer(annotationtype:).md)
  Returns an annotated-feature transformer that transforms the features using this transformer while leaving the annotations unchanged.
- [func adaptedAsAnnotatedPredictionTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, AnnotatedPrediction<Self.Output, Annotation>>
](imputetransformer/adaptedasannotatedpredictiontransformer(annotationtype:).md)
  Returns an annotated-prediction transformer that transforms the predictions using this transformer while leaving the annotations unchanged.
- [func adaptedAsEstimator() -> TransformerToEstimatorAdaptor<Self>](imputetransformer/adaptedasestimator.md)
  Exposes this transformer as a trivial estimator.
- [func adaptedAsRandomTransformer() -> some RandomTransformer<Self.Input, Self.Output>
](imputetransformer/adaptedasrandomtransformer.md)
  Returns a random transformer wrapping a transformer.
- [func adaptedAsTemporal() -> TransformerToTemporalAdaptor<Self>](imputetransformer/adaptedastemporal-21rth.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsTemporal() -> TemporalAdaptor<Self>](imputetransformer/adaptedastemporal-27klg.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsUpdatableEstimator() -> TransformerToUpdatableEstimatorAdaptor<Self>](imputetransformer/adaptedasupdatableestimator.md)
  Exposes this transformer as a trivial estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, Other.Output>
](imputetransformer/appending(_:)-2pdxo.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableEstimator<Self, Other>](imputetransformer/appending(_:)-3wrpn.md)
  Composes this transformer with an updatable estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedFeature<Other.Output, Annotation>>
](imputetransformer/appending(_:)-3y8it.md)
  Composes this transformer with a feature-only transformer.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self>, Other>](imputetransformer/appending(_:)-4rj53.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedEstimator<Self, Other>](imputetransformer/appending(_:)-5098m.md)
  Composes this transformer with an updatable supervised estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](imputetransformer/appending(_:)-5sohq.md)
  Composes this transformer with an updatable temporal estimator.
- [func appending<Other>(Other) -> ComposedTransformer<Self, Other>](imputetransformer/appending(_:)-6rrfd.md)
  Composes this transformer with another transformer.
- [func appending<Other>(Other) -> PreprocessingEstimator<Self, Other>](imputetransformer/appending(_:)-76we5.md)
  Composes this transformer with an estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](imputetransformer/appending(_:)-7avr7.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](imputetransformer/appending(_:)-80te4.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, Other.Output>
](imputetransformer/appending(_:)-87hea.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedPrediction<Other.Output, Annotation>>
](imputetransformer/appending(_:)-8dudy.md)
  Composes this transformer with a prediction-only transformer.
- [func appending<Other>(Other) -> PreprocessingSupervisedEstimator<Self, Other>](imputetransformer/appending(_:)-93itn.md)
  Composes this transformer with a supervised estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TemporalAdaptor<Self>, Other>](imputetransformer/appending(_:)-9nb0v.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](imputetransformer/appending(_:)-9w544.md)
  Composes this transformer with a temporal estimator.
- [func callAsFunction(Self.Input, eventHandler: EventHandler?) async throws -> Self.Output](imputetransformer/callasfunction(_:eventhandler:)-8crnh.md)
  Performs the transformation on a single input.
- [func callAsFunction<S>(S, eventHandler: EventHandler?) async throws -> [Self.Output]](imputetransformer/callasfunction(_:eventhandler:)-8vdkm.md)
  Performs the transformation on a sequence of inputs.
- [func export(to: URL) throws](imputetransformer/export(to:).md)
  Exports this transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](imputetransformer/export(to:metadata:).md)
  Exports this transformer as a CoreML model with userInfo.
- [func prediction<S, Label>(from: S) async throws -> [ClassificationDistribution<Label>]](imputetransformer/prediction(from:)-3uhl0.md)
  Performs a prediction from a sequence of inputs.
- [func prediction<Label>(from: Self.Input) async throws -> ClassificationDistribution<Label>](imputetransformer/prediction(from:)-4dcpu.md)
  Performs a prediction from a single input.
- [func prediction<S, Annotation>(from: S, eventHandler: EventHandler?) async throws -> [AnnotatedPrediction<Self.Output, Annotation>]](imputetransformer/prediction(from:eventhandler:).md)
  Performs a prediction on a sequence of annotated inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/imputetransformer/transformer-implementations)*