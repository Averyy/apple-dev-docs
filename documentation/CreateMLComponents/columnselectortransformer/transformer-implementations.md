# Transformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsAnnotatedFeatureTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, AnnotatedFeature<Self.Output, Annotation>>
](columnselectortransformer/adaptedasannotatedfeaturetransformer(annotationtype:).md)
  Returns an annotated-feature transformer that transforms the features using this transformer while leaving the annotations unchanged.
- [func adaptedAsAnnotatedPredictionTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, AnnotatedPrediction<Self.Output, Annotation>>
](columnselectortransformer/adaptedasannotatedpredictiontransformer(annotationtype:).md)
  Returns an annotated-prediction transformer that transforms the predictions using this transformer while leaving the annotations unchanged.
- [func adaptedAsRandomTransformer() -> some RandomTransformer<Self.Input, Self.Output>
](columnselectortransformer/adaptedasrandomtransformer.md)
  Returns a random transformer wrapping a transformer.
- [func adaptedAsTemporal() -> TransformerToTemporalAdaptor<Self>](columnselectortransformer/adaptedastemporal-126zh.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsTemporal() -> TemporalAdaptor<Self>](columnselectortransformer/adaptedastemporal-87mc0.md)
  Exposes this transformer as a temporal transformer.
- [func appending<Other>(Other) -> PreprocessingEstimator<Self, Other>](columnselectortransformer/appending(_:)-1sz5d.md)
  Composes this transformer with an estimator.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](columnselectortransformer/appending(_:)-1t8ry.md)
  Composes this transformer with a temporal estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](columnselectortransformer/appending(_:)-2ogto.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, Other.Output>
](columnselectortransformer/appending(_:)-30qos.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TemporalAdaptor<Self>, Other>](columnselectortransformer/appending(_:)-3k3di.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self>, Other>](columnselectortransformer/appending(_:)-3yxxe.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, Other.Output>
](columnselectortransformer/appending(_:)-54uba.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedFeature<Other.Output, Annotation>>
](columnselectortransformer/appending(_:)-5h7jf.md)
  Composes this transformer with a feature-only transformer.
- [func appending<Other>(Other) -> ComposedTransformer<Self, Other>](columnselectortransformer/appending(_:)-6uvq3.md)
  Composes this transformer with another transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedEstimator<Self, Other>](columnselectortransformer/appending(_:)-7daah.md)
  Composes this transformer with an updatable supervised estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](columnselectortransformer/appending(_:)-9bjp.md)
  Composes this transformer with an updatable temporal estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedEstimator<Self, Other>](columnselectortransformer/appending(_:)-9v1r0.md)
  Composes this transformer with a supervised estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableEstimator<Self, Other>](columnselectortransformer/appending(_:)-drev.md)
  Composes this transformer with an updatable estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedPrediction<Other.Output, Annotation>>
](columnselectortransformer/appending(_:)-ers7.md)
  Composes this transformer with a prediction-only transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](columnselectortransformer/appending(_:)-ihu7.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func export(to: URL) throws](columnselectortransformer/export(to:)-5a7w9.md)
  Exports this transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](columnselectortransformer/export(to:metadata:)-8ar2h.md)
  Exports this transformer as a CoreML model with userInfo.
- [func prediction<S, Label>(from: S) async throws -> [ClassificationDistribution<Label>]](columnselectortransformer/prediction(from:)-60z6p.md)
  Performs a prediction from a sequence of inputs.
- [func prediction<Label>(from: Self.Input) async throws -> ClassificationDistribution<Label>](columnselectortransformer/prediction(from:)-8i3yp.md)
  Performs a prediction from a single input.
- [func prediction<S, Annotation>(from: S, eventHandler: EventHandler?) async throws -> [AnnotatedPrediction<Self.Output, Annotation>]](columnselectortransformer/prediction(from:eventhandler:).md)
  Performs a prediction on a sequence of annotated inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/columnselectortransformer/transformer-implementations)*