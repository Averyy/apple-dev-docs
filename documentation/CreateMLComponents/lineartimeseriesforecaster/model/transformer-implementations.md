# Transformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsAnnotatedFeatureTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, AnnotatedFeature<Self.Output, Annotation>>
](lineartimeseriesforecaster/model/adaptedasannotatedfeaturetransformer(annotationtype:).md)
  Returns an annotated-feature transformer that transforms the features using this transformer while leaving the annotations unchanged.
- [func adaptedAsAnnotatedPredictionTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, AnnotatedPrediction<Self.Output, Annotation>>
](lineartimeseriesforecaster/model/adaptedasannotatedpredictiontransformer(annotationtype:).md)
  Returns an annotated-prediction transformer that transforms the predictions using this transformer while leaving the annotations unchanged.
- [func adaptedAsEstimator() -> TransformerToEstimatorAdaptor<Self>](lineartimeseriesforecaster/model/adaptedasestimator-41ebj.md)
  Exposes this transformer as a trivial estimator.
- [func adaptedAsRandomTransformer() -> some RandomTransformer<Self.Input, Self.Output>
](lineartimeseriesforecaster/model/adaptedasrandomtransformer.md)
  Returns a random transformer wrapping a transformer.
- [func adaptedAsTemporal() -> TemporalAdaptor<Self>](lineartimeseriesforecaster/model/adaptedastemporal.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsUpdatableEstimator() -> TransformerToUpdatableEstimatorAdaptor<Self>](lineartimeseriesforecaster/model/adaptedasupdatableestimator-t375.md)
  Exposes this transformer as a trivial estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableEstimator<Self, Other>](lineartimeseriesforecaster/model/appending(_:)-1lesu.md)
  Composes this transformer with an updatable estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](lineartimeseriesforecaster/model/appending(_:)-1ndwt.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, Other.Output>
](lineartimeseriesforecaster/model/appending(_:)-1oa6r.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedFeature<Other.Output, Annotation>>
](lineartimeseriesforecaster/model/appending(_:)-1vdq.md)
  Composes this transformer with a feature-only transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedEstimator<Self, Other>](lineartimeseriesforecaster/model/appending(_:)-1vehy.md)
  Composes this transformer with an updatable supervised estimator.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](lineartimeseriesforecaster/model/appending(_:)-2o7kk.md)
  Composes this transformer with a temporal estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TemporalAdaptor<Self>, Other>](lineartimeseriesforecaster/model/appending(_:)-2z6fg.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other>(Other) -> ComposedTransformer<Self, Other>](lineartimeseriesforecaster/model/appending(_:)-3isxs.md)
  Composes this transformer with another transformer.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self>, Other>](lineartimeseriesforecaster/model/appending(_:)-4bvbi.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other>(Other) -> PreprocessingEstimator<Self, Other>](lineartimeseriesforecaster/model/appending(_:)-4f8mg.md)
  Composes this transformer with an estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedPrediction<Other.Output, Annotation>>
](lineartimeseriesforecaster/model/appending(_:)-4qw9i.md)
  Composes this transformer with a prediction-only transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](lineartimeseriesforecaster/model/appending(_:)-5i45p.md)
  Composes this transformer with an updatable temporal estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedEstimator<Self, Other>](lineartimeseriesforecaster/model/appending(_:)-62faq.md)
  Composes this transformer with a supervised estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, Other.Output>
](lineartimeseriesforecaster/model/appending(_:)-79t5a.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](lineartimeseriesforecaster/model/appending(_:)-9w9d3.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func callAsFunction<S>(S, eventHandler: EventHandler?) async throws -> [Self.Output]](lineartimeseriesforecaster/model/callasfunction(_:eventhandler:)-38dwc.md)
  Performs the transformation on a sequence of inputs.
- [func callAsFunction(Self.Input, eventHandler: EventHandler?) async throws -> Self.Output](lineartimeseriesforecaster/model/callasfunction(_:eventhandler:)-607bh.md)
  Performs the transformation on a single input.
- [func prediction<Label>(from: Self.Input) async throws -> ClassificationDistribution<Label>](lineartimeseriesforecaster/model/prediction(from:)-2htjo.md)
  Performs a prediction from a single input.
- [func prediction<S, Label>(from: S) async throws -> [ClassificationDistribution<Label>]](lineartimeseriesforecaster/model/prediction(from:)-97w6k.md)
  Performs a prediction from a sequence of inputs.
- [func prediction<S, Annotation>(from: S, eventHandler: EventHandler?) async throws -> [AnnotatedPrediction<Self.Output, Annotation>]](lineartimeseriesforecaster/model/prediction(from:eventhandler:).md)
  Performs a prediction on a sequence of annotated inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/lineartimeseriesforecaster/model/transformer-implementations)*