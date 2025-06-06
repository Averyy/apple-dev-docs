# Transformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsAnnotatedFeatureTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, AnnotatedFeature<Self.Output, Annotation>>
](normalizationscaler/transformer/adaptedasannotatedfeaturetransformer(annotationtype:).md)
  Returns an annotated-feature transformer that transforms the features using this transformer while leaving the annotations unchanged.
- [func adaptedAsAnnotatedPredictionTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, AnnotatedPrediction<Self.Output, Annotation>>
](normalizationscaler/transformer/adaptedasannotatedpredictiontransformer(annotationtype:).md)
  Returns an annotated-prediction transformer that transforms the predictions using this transformer while leaving the annotations unchanged.
- [func adaptedAsEstimator() -> TransformerToEstimatorAdaptor<Self>](normalizationscaler/transformer/adaptedasestimator.md)
  Exposes this transformer as a trivial estimator.
- [func adaptedAsRandomTransformer() -> some RandomTransformer<Self.Input, Self.Output>
](normalizationscaler/transformer/adaptedasrandomtransformer.md)
  Returns a random transformer wrapping a transformer.
- [func adaptedAsTemporal() -> TemporalAdaptor<Self>](normalizationscaler/transformer/adaptedastemporal-2s6jv.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsTemporal() -> TransformerToTemporalAdaptor<Self>](normalizationscaler/transformer/adaptedastemporal-8gfif.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsUpdatableEstimator() -> TransformerToUpdatableEstimatorAdaptor<Self>](normalizationscaler/transformer/adaptedasupdatableestimator.md)
  Exposes this transformer as a trivial estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TemporalAdaptor<Self>, Other>](normalizationscaler/transformer/appending(_:)-1ce0q.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](normalizationscaler/transformer/appending(_:)-28ry8.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](normalizationscaler/transformer/appending(_:)-2eoke.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingEstimator<Self, Other>](normalizationscaler/transformer/appending(_:)-2sg3q.md)
  Composes this transformer with an estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedPrediction<Other.Output, Annotation>>
](normalizationscaler/transformer/appending(_:)-2z6sz.md)
  Composes this transformer with a prediction-only transformer.
- [func appending<Other>(Other) -> PreprocessingSupervisedEstimator<Self, Other>](normalizationscaler/transformer/appending(_:)-35dis.md)
  Composes this transformer with a supervised estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, Other.Output>
](normalizationscaler/transformer/appending(_:)-3rnwn.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedEstimator<Self, Other>](normalizationscaler/transformer/appending(_:)-45jqj.md)
  Composes this transformer with an updatable supervised estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, Other.Output>
](normalizationscaler/transformer/appending(_:)-4jw1t.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> ComposedTransformer<Self, Other>](normalizationscaler/transformer/appending(_:)-5pxdf.md)
  Composes this transformer with another transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableEstimator<Self, Other>](normalizationscaler/transformer/appending(_:)-79c92.md)
  Composes this transformer with an updatable estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedFeature<Other.Output, Annotation>>
](normalizationscaler/transformer/appending(_:)-8fu21.md)
  Composes this transformer with a feature-only transformer.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self>, Other>](normalizationscaler/transformer/appending(_:)-9p8l8.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](normalizationscaler/transformer/appending(_:)-9qr8b.md)
  Composes this transformer with a temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](normalizationscaler/transformer/appending(_:)-l6rn.md)
  Composes this transformer with an updatable temporal estimator.
- [func callAsFunction<S>(S, eventHandler: EventHandler?) async throws -> [Self.Output]](normalizationscaler/transformer/callasfunction(_:eventhandler:)-1nx1g.md)
  Performs the transformation on a sequence of inputs.
- [func callAsFunction(Self.Input, eventHandler: EventHandler?) async throws -> Self.Output](normalizationscaler/transformer/callasfunction(_:eventhandler:)-8bfu2.md)
  Performs the transformation on a single input.
- [func export(to: URL) throws](normalizationscaler/transformer/export(to:).md)
  Exports this transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](normalizationscaler/transformer/export(to:metadata:).md)
  Exports this transformer as a CoreML model with userInfo.
- [func prediction<S, Label>(from: S) async throws -> [ClassificationDistribution<Label>]](normalizationscaler/transformer/prediction(from:)-5qirg.md)
  Performs a prediction from a sequence of inputs.
- [func prediction<Label>(from: Self.Input) async throws -> ClassificationDistribution<Label>](normalizationscaler/transformer/prediction(from:)-87apl.md)
  Performs a prediction from a single input.
- [func prediction<S, Annotation>(from: S, eventHandler: EventHandler?) async throws -> [AnnotatedPrediction<Self.Output, Annotation>]](normalizationscaler/transformer/prediction(from:eventhandler:).md)
  Performs a prediction on a sequence of annotated inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/normalizationscaler/transformer/transformer-implementations)*