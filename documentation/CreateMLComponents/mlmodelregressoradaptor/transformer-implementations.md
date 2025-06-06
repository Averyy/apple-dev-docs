# Transformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsAnnotatedFeatureTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, AnnotatedFeature<Self.Output, Annotation>>
](mlmodelregressoradaptor/adaptedasannotatedfeaturetransformer(annotationtype:).md)
  Returns an annotated-feature transformer that transforms the features using this transformer while leaving the annotations unchanged.
- [func adaptedAsAnnotatedPredictionTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, AnnotatedPrediction<Self.Output, Annotation>>
](mlmodelregressoradaptor/adaptedasannotatedpredictiontransformer(annotationtype:).md)
  Returns an annotated-prediction transformer that transforms the predictions using this transformer while leaving the annotations unchanged.
- [func adaptedAsEstimator() -> TransformerToEstimatorAdaptor<Self>](mlmodelregressoradaptor/adaptedasestimator.md)
  Exposes this transformer as a trivial estimator.
- [func adaptedAsRandomTransformer() -> some RandomTransformer<Self.Input, Self.Output>
](mlmodelregressoradaptor/adaptedasrandomtransformer.md)
  Returns a random transformer wrapping a transformer.
- [func adaptedAsTemporal() -> TemporalAdaptor<Self>](mlmodelregressoradaptor/adaptedastemporal-2l7.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsTemporal() -> TransformerToTemporalAdaptor<Self>](mlmodelregressoradaptor/adaptedastemporal-4yzdb.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsUpdatableEstimator() -> TransformerToUpdatableEstimatorAdaptor<Self>](mlmodelregressoradaptor/adaptedasupdatableestimator.md)
  Exposes this transformer as a trivial estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self>, Other>](mlmodelregressoradaptor/appending(_:)-1yczq.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other>(Other) -> PreprocessingEstimator<Self, Other>](mlmodelregressoradaptor/appending(_:)-21j3p.md)
  Composes this transformer with an estimator.
- [func appending<Other>(Other) -> ComposedTransformer<Self, Other>](mlmodelregressoradaptor/appending(_:)-2cpy4.md)
  Composes this transformer with another transformer.
- [func appending<Other>(Other) -> PreprocessingSupervisedEstimator<Self, Other>](mlmodelregressoradaptor/appending(_:)-39w9.md)
  Composes this transformer with a supervised estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, Other.Output>
](mlmodelregressoradaptor/appending(_:)-3hoyd.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](mlmodelregressoradaptor/appending(_:)-4zfp5.md)
  Composes this transformer with a temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedEstimator<Self, Other>](mlmodelregressoradaptor/appending(_:)-50n0m.md)
  Composes this transformer with an updatable supervised estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, Other.Output>
](mlmodelregressoradaptor/appending(_:)-5eo93.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](mlmodelregressoradaptor/appending(_:)-6mayg.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](mlmodelregressoradaptor/appending(_:)-6pv5.md)
  Composes this transformer with an updatable temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableEstimator<Self, Other>](mlmodelregressoradaptor/appending(_:)-82gis.md)
  Composes this transformer with an updatable estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedFeature<Other.Output, Annotation>>
](mlmodelregressoradaptor/appending(_:)-996yo.md)
  Composes this transformer with a feature-only transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](mlmodelregressoradaptor/appending(_:)-9igbq.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TemporalAdaptor<Self>, Other>](mlmodelregressoradaptor/appending(_:)-9to55.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedPrediction<Other.Output, Annotation>>
](mlmodelregressoradaptor/appending(_:)-z4rb.md)
  Composes this transformer with a prediction-only transformer.
- [func callAsFunction(Self.Input, eventHandler: EventHandler?) async throws -> Self.Output](mlmodelregressoradaptor/callasfunction(_:eventhandler:)-4lpsz.md)
  Performs the transformation on a single input.
- [func callAsFunction<S>(S, eventHandler: EventHandler?) async throws -> [Self.Output]](mlmodelregressoradaptor/callasfunction(_:eventhandler:)-8crtb.md)
  Performs the transformation on a sequence of inputs.
- [func export(to: URL) throws](mlmodelregressoradaptor/export(to:).md)
  Exports this transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](mlmodelregressoradaptor/export(to:metadata:).md)
  Exports this transformer as a CoreML model with userInfo.
- [func prediction<S, Annotation>(from: S, eventHandler: EventHandler?) async throws -> [AnnotatedPrediction<Self.Output, Annotation>]](mlmodelregressoradaptor/prediction(from:eventhandler:).md)
  Performs a prediction on a sequence of annotated inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/mlmodelregressoradaptor/transformer-implementations)*