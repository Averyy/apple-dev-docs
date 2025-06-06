# Transformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsAnnotatedFeatureTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, AnnotatedFeature<Self.Output, Annotation>>
](humanbodyactionperiodpredictor/adaptedasannotatedfeaturetransformer(annotationtype:).md)
  Returns an annotated-feature transformer that transforms the features using this transformer while leaving the annotations unchanged.
- [func adaptedAsAnnotatedPredictionTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, AnnotatedPrediction<Self.Output, Annotation>>
](humanbodyactionperiodpredictor/adaptedasannotatedpredictiontransformer(annotationtype:).md)
  Returns an annotated-prediction transformer that transforms the predictions using this transformer while leaving the annotations unchanged.
- [func adaptedAsEstimator() -> TransformerToEstimatorAdaptor<Self>](humanbodyactionperiodpredictor/adaptedasestimator.md)
  Exposes this transformer as a trivial estimator.
- [func adaptedAsRandomTransformer() -> some RandomTransformer<Self.Input, Self.Output>
](humanbodyactionperiodpredictor/adaptedasrandomtransformer.md)
  Returns a random transformer wrapping a transformer.
- [func adaptedAsTemporal() -> TransformerToTemporalAdaptor<Self>](humanbodyactionperiodpredictor/adaptedastemporal.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsUpdatableEstimator() -> TransformerToUpdatableEstimatorAdaptor<Self>](humanbodyactionperiodpredictor/adaptedasupdatableestimator.md)
  Exposes this transformer as a trivial estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](humanbodyactionperiodpredictor/appending(_:)-1yb5p.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](humanbodyactionperiodpredictor/appending(_:)-2r0g6.md)
  Composes this transformer with an updatable temporal estimator.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](humanbodyactionperiodpredictor/appending(_:)-2tpp3.md)
  Composes this transformer with a temporal estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedPrediction<Other.Output, Annotation>>
](humanbodyactionperiodpredictor/appending(_:)-2uxt4.md)
  Composes this transformer with a prediction-only transformer.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TemporalAdaptor<Self>, Other>](humanbodyactionperiodpredictor/appending(_:)-3dp2q.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](humanbodyactionperiodpredictor/appending(_:)-3r068.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self>, Other>](humanbodyactionperiodpredictor/appending(_:)-3r0sh.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other>(Other) -> PreprocessingSupervisedEstimator<Self, Other>](humanbodyactionperiodpredictor/appending(_:)-5f8gt.md)
  Composes this transformer with a supervised estimator.
- [func appending<Other>(Other) -> PreprocessingEstimator<Self, Other>](humanbodyactionperiodpredictor/appending(_:)-5gena.md)
  Composes this transformer with an estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, Other.Output>
](humanbodyactionperiodpredictor/appending(_:)-7ggv0.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedEstimator<Self, Other>](humanbodyactionperiodpredictor/appending(_:)-7s9re.md)
  Composes this transformer with an updatable supervised estimator.
- [func appending<Other>(Other) -> ComposedTransformer<Self, Other>](humanbodyactionperiodpredictor/appending(_:)-85tow.md)
  Composes this transformer with another transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedFeature<Other.Output, Annotation>>
](humanbodyactionperiodpredictor/appending(_:)-8dgwf.md)
  Composes this transformer with a feature-only transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, Other.Output>
](humanbodyactionperiodpredictor/appending(_:)-8kee1.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableEstimator<Self, Other>](humanbodyactionperiodpredictor/appending(_:)-8mjf8.md)
  Composes this transformer with an updatable estimator.
- [func callAsFunction<S>(S, eventHandler: EventHandler?) async throws -> [Self.Output]](humanbodyactionperiodpredictor/callasfunction(_:eventhandler:)-5ypqq.md)
  Performs the transformation on a sequence of inputs.
- [func callAsFunction(Self.Input, eventHandler: EventHandler?) async throws -> Self.Output](humanbodyactionperiodpredictor/callasfunction(_:eventhandler:)-8ryat.md)
  Performs the transformation on a single input.
- [func export(to: URL) throws](humanbodyactionperiodpredictor/export(to:).md)
  Exports this transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](humanbodyactionperiodpredictor/export(to:metadata:).md)
  Exports this transformer as a CoreML model with userInfo.
- [func prediction<Label>(from: Self.Input) async throws -> ClassificationDistribution<Label>](humanbodyactionperiodpredictor/prediction(from:)-6dz52.md)
  Performs a prediction from a single input.
- [func prediction<S, Label>(from: S) async throws -> [ClassificationDistribution<Label>]](humanbodyactionperiodpredictor/prediction(from:)-92lsq.md)
  Performs a prediction from a sequence of inputs.
- [func prediction<S, Annotation>(from: S, eventHandler: EventHandler?) async throws -> [AnnotatedPrediction<Self.Output, Annotation>]](humanbodyactionperiodpredictor/prediction(from:eventhandler:).md)
  Performs a prediction on a sequence of annotated inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/humanbodyactionperiodpredictor/transformer-implementations)*