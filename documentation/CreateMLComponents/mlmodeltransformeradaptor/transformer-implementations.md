# Transformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsAnnotatedFeatureTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, AnnotatedFeature<Self.Output, Annotation>>
](mlmodeltransformeradaptor/adaptedasannotatedfeaturetransformer(annotationtype:).md)
  Returns an annotated-feature transformer that transforms the features using this transformer while leaving the annotations unchanged.
- [func adaptedAsAnnotatedPredictionTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, AnnotatedPrediction<Self.Output, Annotation>>
](mlmodeltransformeradaptor/adaptedasannotatedpredictiontransformer(annotationtype:).md)
  Returns an annotated-prediction transformer that transforms the predictions using this transformer while leaving the annotations unchanged.
- [func adaptedAsEstimator() -> TransformerToEstimatorAdaptor<Self>](mlmodeltransformeradaptor/adaptedasestimator.md)
  Exposes this transformer as a trivial estimator.
- [func adaptedAsRandomTransformer() -> some RandomTransformer<Self.Input, Self.Output>
](mlmodeltransformeradaptor/adaptedasrandomtransformer.md)
  Returns a random transformer wrapping a transformer.
- [func adaptedAsTemporal() -> TemporalAdaptor<Self>](mlmodeltransformeradaptor/adaptedastemporal-6s9lf.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsTemporal() -> TransformerToTemporalAdaptor<Self>](mlmodeltransformeradaptor/adaptedastemporal-80f7u.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsUpdatableEstimator() -> TransformerToUpdatableEstimatorAdaptor<Self>](mlmodeltransformeradaptor/adaptedasupdatableestimator.md)
  Exposes this transformer as a trivial estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedFeature<Other.Output, Annotation>>
](mlmodeltransformeradaptor/appending(_:)-107qh.md)
  Composes this transformer with a feature-only transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, Other.Output>
](mlmodeltransformeradaptor/appending(_:)-175j6.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> PreprocessingEstimator<Self, Other>](mlmodeltransformeradaptor/appending(_:)-1cc37.md)
  Composes this transformer with an estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableEstimator<Self, Other>](mlmodeltransformeradaptor/appending(_:)-1maxa.md)
  Composes this transformer with an updatable estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](mlmodeltransformeradaptor/appending(_:)-1n54o.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self>, Other>](mlmodeltransformeradaptor/appending(_:)-2nzax.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TemporalAdaptor<Self>, Other>](mlmodeltransformeradaptor/appending(_:)-33gk0.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](mlmodeltransformeradaptor/appending(_:)-53nk2.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> ComposedTransformer<Self, Other>](mlmodeltransformeradaptor/appending(_:)-5acez.md)
  Composes this transformer with another transformer.
- [func appending<Other>(Other) -> PreprocessingSupervisedEstimator<Self, Other>](mlmodeltransformeradaptor/appending(_:)-75ixf.md)
  Composes this transformer with a supervised estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedPrediction<Other.Output, Annotation>>
](mlmodeltransformeradaptor/appending(_:)-7vs2y.md)
  Composes this transformer with a prediction-only transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedEstimator<Self, Other>](mlmodeltransformeradaptor/appending(_:)-8ft9.md)
  Composes this transformer with an updatable supervised estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, Other.Output>
](mlmodeltransformeradaptor/appending(_:)-8vbsm.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](mlmodeltransformeradaptor/appending(_:)-91rmj.md)
  Composes this transformer with an updatable temporal estimator.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](mlmodeltransformeradaptor/appending(_:)-93bho.md)
  Composes this transformer with a temporal estimator.
- [func callAsFunction<S>(S, eventHandler: EventHandler?) async throws -> [Self.Output]](mlmodeltransformeradaptor/callasfunction(_:eventhandler:)-4uc1y.md)
  Performs the transformation on a sequence of inputs.
- [func callAsFunction(Self.Input, eventHandler: EventHandler?) async throws -> Self.Output](mlmodeltransformeradaptor/callasfunction(_:eventhandler:)-9snug.md)
  Performs the transformation on a single input.
- [func export(to: URL) throws](mlmodeltransformeradaptor/export(to:).md)
  Exports this transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](mlmodeltransformeradaptor/export(to:metadata:).md)
  Exports this transformer as a CoreML model with userInfo.
- [func prediction<Label>(from: Self.Input) async throws -> ClassificationDistribution<Label>](mlmodeltransformeradaptor/prediction(from:)-21ilx.md)
  Performs a prediction from a single input.
- [func prediction<S, Label>(from: S) async throws -> [ClassificationDistribution<Label>]](mlmodeltransformeradaptor/prediction(from:)-4fc8z.md)
  Performs a prediction from a sequence of inputs.
- [func prediction<S, Annotation>(from: S, eventHandler: EventHandler?) async throws -> [AnnotatedPrediction<Self.Output, Annotation>]](mlmodeltransformeradaptor/prediction(from:eventhandler:).md)
  Performs a prediction on a sequence of annotated inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/mlmodeltransformeradaptor/transformer-implementations)*