# Transformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsAnnotatedFeatureTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, AnnotatedFeature<Self.Output, Annotation>>
](columnconcatenator/adaptedasannotatedfeaturetransformer(annotationtype:).md)
  Returns an annotated-feature transformer that transforms the features using this transformer while leaving the annotations unchanged.
- [func adaptedAsAnnotatedPredictionTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, AnnotatedPrediction<Self.Output, Annotation>>
](columnconcatenator/adaptedasannotatedpredictiontransformer(annotationtype:).md)
  Returns an annotated-prediction transformer that transforms the predictions using this transformer while leaving the annotations unchanged.
- [func adaptedAsRandomTransformer() -> some RandomTransformer<Self.Input, Self.Output>
](columnconcatenator/adaptedasrandomtransformer.md)
  Returns a random transformer wrapping a transformer.
- [func adaptedAsTemporal() -> TransformerToTemporalAdaptor<Self>](columnconcatenator/adaptedastemporal-2crus.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsTemporal() -> TemporalAdaptor<Self>](columnconcatenator/adaptedastemporal-3xozd.md)
  Exposes this transformer as a temporal transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, Other.Output>
](columnconcatenator/appending(_:)-1dc5r.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TemporalAdaptor<Self>, Other>](columnconcatenator/appending(_:)-1gy88.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](columnconcatenator/appending(_:)-1o8di.md)
  Composes this transformer with an updatable temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableEstimator<Self, Other>](columnconcatenator/appending(_:)-1u34l.md)
  Composes this transformer with an updatable estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](columnconcatenator/appending(_:)-3mto2.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](columnconcatenator/appending(_:)-4m787.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedEstimator<Self, Other>](columnconcatenator/appending(_:)-4w7b1.md)
  Composes this transformer with an updatable supervised estimator.
- [func appending<Other>(Other) -> ComposedTransformer<Self, Other>](columnconcatenator/appending(_:)-689tw.md)
  Composes this transformer with another transformer.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self>, Other>](columnconcatenator/appending(_:)-69nam.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedPrediction<Other.Output, Annotation>>
](columnconcatenator/appending(_:)-6j5zf.md)
  Composes this transformer with a prediction-only transformer.
- [func appending<Other>(Other) -> PreprocessingSupervisedEstimator<Self, Other>](columnconcatenator/appending(_:)-7cjb7.md)
  Composes this transformer with a supervised estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, Other.Output>
](columnconcatenator/appending(_:)-7vzyj.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedFeature<Other.Output, Annotation>>
](columnconcatenator/appending(_:)-7xinl.md)
  Composes this transformer with a feature-only transformer.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](columnconcatenator/appending(_:)-8032w.md)
  Composes this transformer with a temporal estimator.
- [func appending<Other>(Other) -> PreprocessingEstimator<Self, Other>](columnconcatenator/appending(_:)-p4fx.md)
  Composes this transformer with an estimator.
- [func export(to: URL) throws](columnconcatenator/export(to:)-6lp32.md)
  Exports this transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](columnconcatenator/export(to:metadata:)-4j998.md)
  Exports this transformer as a CoreML model with userInfo.
- [func prediction<S, Label>(from: S) async throws -> [ClassificationDistribution<Label>]](columnconcatenator/prediction(from:)-2x6f6.md)
  Performs a prediction from a sequence of inputs.
- [func prediction<Label>(from: Self.Input) async throws -> ClassificationDistribution<Label>](columnconcatenator/prediction(from:)-8d66d.md)
  Performs a prediction from a single input.
- [func prediction<S, Annotation>(from: S, eventHandler: EventHandler?) async throws -> [AnnotatedPrediction<Self.Output, Annotation>]](columnconcatenator/prediction(from:eventhandler:).md)
  Performs a prediction on a sequence of annotated inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/columnconcatenator/transformer-implementations)*