# Transformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsAnnotatedFeatureTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, AnnotatedFeature<Self.Output, Annotation>>
](treeclassifiermodel/adaptedasannotatedfeaturetransformer(annotationtype:).md)
  Returns an annotated-feature transformer that transforms the features using this transformer while leaving the annotations unchanged.
- [func adaptedAsAnnotatedPredictionTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, AnnotatedPrediction<Self.Output, Annotation>>
](treeclassifiermodel/adaptedasannotatedpredictiontransformer(annotationtype:).md)
  Returns an annotated-prediction transformer that transforms the predictions using this transformer while leaving the annotations unchanged.
- [func adaptedAsRandomTransformer() -> some RandomTransformer<Self.Input, Self.Output>
](treeclassifiermodel/adaptedasrandomtransformer.md)
  Returns a random transformer wrapping a transformer.
- [func adaptedAsTemporal() -> TransformerToTemporalAdaptor<Self>](treeclassifiermodel/adaptedastemporal-3tjgt.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsTemporal() -> TemporalAdaptor<Self>](treeclassifiermodel/adaptedastemporal-5pv82.md)
  Exposes this transformer as a temporal transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedEstimator<Self, Other>](treeclassifiermodel/appending(_:)-1l79b.md)
  Composes this transformer with an updatable supervised estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, Other.Output>
](treeclassifiermodel/appending(_:)-1tm2q.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> PreprocessingEstimator<Self, Other>](treeclassifiermodel/appending(_:)-1tmzu.md)
  Composes this transformer with an estimator.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](treeclassifiermodel/appending(_:)-235ac.md)
  Composes this transformer with a temporal estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedPrediction<Other.Output, Annotation>>
](treeclassifiermodel/appending(_:)-2odud.md)
  Composes this transformer with a prediction-only transformer.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](treeclassifiermodel/appending(_:)-3c7pz.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TemporalAdaptor<Self>, Other>](treeclassifiermodel/appending(_:)-3pod8.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other>(Other) -> ComposedTransformer<Self, Other>](treeclassifiermodel/appending(_:)-3rydc.md)
  Composes this transformer with another transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](treeclassifiermodel/appending(_:)-3zcke.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedFeature<Other.Output, Annotation>>
](treeclassifiermodel/appending(_:)-52wjp.md)
  Composes this transformer with a feature-only transformer.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self>, Other>](treeclassifiermodel/appending(_:)-67op4.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, Other.Output>
](treeclassifiermodel/appending(_:)-748hk.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](treeclassifiermodel/appending(_:)-77qa3.md)
  Composes this transformer with an updatable temporal estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedEstimator<Self, Other>](treeclassifiermodel/appending(_:)-86lys.md)
  Composes this transformer with a supervised estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableEstimator<Self, Other>](treeclassifiermodel/appending(_:)-86yi2.md)
  Composes this transformer with an updatable estimator.
- [func export(to: URL) throws](treeclassifiermodel/export(to:)-3odk.md)
  Exports this transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](treeclassifiermodel/export(to:metadata:)-244fa.md)
  Exports this transformer as a CoreML model with userInfo.
- [func prediction<Label>(from: Self.Input) async throws -> ClassificationDistribution<Label>](treeclassifiermodel/prediction(from:)-7yuyc.md)
  Performs a prediction from a single input.
- [func prediction<S, Label>(from: S) async throws -> [ClassificationDistribution<Label>]](treeclassifiermodel/prediction(from:)-9m626.md)
  Performs a prediction from a sequence of inputs.
- [func prediction<S, Annotation>(from: S, eventHandler: EventHandler?) async throws -> [AnnotatedPrediction<Self.Output, Annotation>]](treeclassifiermodel/prediction(from:eventhandler:).md)
  Performs a prediction on a sequence of annotated inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/treeclassifiermodel/transformer-implementations)*