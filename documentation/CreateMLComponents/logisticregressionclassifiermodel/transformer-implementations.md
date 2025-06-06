# Transformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsAnnotatedFeatureTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, AnnotatedFeature<Self.Output, Annotation>>
](logisticregressionclassifiermodel/adaptedasannotatedfeaturetransformer(annotationtype:).md)
  Returns an annotated-feature transformer that transforms the features using this transformer while leaving the annotations unchanged.
- [func adaptedAsAnnotatedPredictionTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, AnnotatedPrediction<Self.Output, Annotation>>
](logisticregressionclassifiermodel/adaptedasannotatedpredictiontransformer(annotationtype:).md)
  Returns an annotated-prediction transformer that transforms the predictions using this transformer while leaving the annotations unchanged.
- [func adaptedAsEstimator() -> TransformerToEstimatorAdaptor<Self>](logisticregressionclassifiermodel/adaptedasestimator.md)
  Exposes this transformer as a trivial estimator.
- [func adaptedAsRandomTransformer() -> some RandomTransformer<Self.Input, Self.Output>
](logisticregressionclassifiermodel/adaptedasrandomtransformer.md)
  Returns a random transformer wrapping a transformer.
- [func adaptedAsTemporal() -> TransformerToTemporalAdaptor<Self>](logisticregressionclassifiermodel/adaptedastemporal-41uet.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsTemporal() -> TemporalAdaptor<Self>](logisticregressionclassifiermodel/adaptedastemporal-4i6k3.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsUpdatableEstimator() -> TransformerToUpdatableEstimatorAdaptor<Self>](logisticregressionclassifiermodel/adaptedasupdatableestimator.md)
  Exposes this transformer as a trivial estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, Other.Output>
](logisticregressionclassifiermodel/appending(_:)-134v3.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, Other.Output>
](logisticregressionclassifiermodel/appending(_:)-26dsj.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableEstimator<Self, Other>](logisticregressionclassifiermodel/appending(_:)-2eug9.md)
  Composes this transformer with an updatable estimator.
- [func appending<Other>(Other) -> ComposedTransformer<Self, Other>](logisticregressionclassifiermodel/appending(_:)-48f2b.md)
  Composes this transformer with another transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedPrediction<Other.Output, Annotation>>
](logisticregressionclassifiermodel/appending(_:)-5gxn8.md)
  Composes this transformer with a prediction-only transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedFeature<Other.Output, Annotation>>
](logisticregressionclassifiermodel/appending(_:)-6kqjk.md)
  Composes this transformer with a feature-only transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedEstimator<Self, Other>](logisticregressionclassifiermodel/appending(_:)-6v019.md)
  Composes this transformer with an updatable supervised estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](logisticregressionclassifiermodel/appending(_:)-71ejt.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](logisticregressionclassifiermodel/appending(_:)-76p4m.md)
  Composes this transformer with a temporal estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TemporalAdaptor<Self>, Other>](logisticregressionclassifiermodel/appending(_:)-78i8h.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](logisticregressionclassifiermodel/appending(_:)-7e462.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self>, Other>](logisticregressionclassifiermodel/appending(_:)-7l1qo.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other>(Other) -> PreprocessingEstimator<Self, Other>](logisticregressionclassifiermodel/appending(_:)-8okdx.md)
  Composes this transformer with an estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](logisticregressionclassifiermodel/appending(_:)-9sjrl.md)
  Composes this transformer with an updatable temporal estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedEstimator<Self, Other>](logisticregressionclassifiermodel/appending(_:)-lbex.md)
  Composes this transformer with a supervised estimator.
- [func callAsFunction(Self.Input, eventHandler: EventHandler?) async throws -> Self.Output](logisticregressionclassifiermodel/callasfunction(_:eventhandler:)-21woe.md)
  Performs the transformation on a single input.
- [func callAsFunction<S>(S, eventHandler: EventHandler?) async throws -> [Self.Output]](logisticregressionclassifiermodel/callasfunction(_:eventhandler:)-36zak.md)
  Performs the transformation on a sequence of inputs.
- [func export(to: URL) throws](logisticregressionclassifiermodel/export(to:).md)
  Exports this transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](logisticregressionclassifiermodel/export(to:metadata:).md)
  Exports this transformer as a CoreML model with userInfo.
- [func prediction<Label>(from: Self.Input) async throws -> ClassificationDistribution<Label>](logisticregressionclassifiermodel/prediction(from:)-7es1r.md)
  Performs a prediction from a single input.
- [func prediction<S, Label>(from: S) async throws -> [ClassificationDistribution<Label>]](logisticregressionclassifiermodel/prediction(from:)-7pw8i.md)
  Performs a prediction from a sequence of inputs.
- [func prediction<S, Annotation>(from: S, eventHandler: EventHandler?) async throws -> [AnnotatedPrediction<Self.Output, Annotation>]](logisticregressionclassifiermodel/prediction(from:eventhandler:).md)
  Performs a prediction on a sequence of annotated inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/logisticregressionclassifiermodel/transformer-implementations)*