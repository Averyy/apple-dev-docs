# Transformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsAnnotatedFeatureTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, AnnotatedFeature<Self.Output, Annotation>>
](imagerotator/adaptedasannotatedfeaturetransformer(annotationtype:).md)
  Returns an annotated-feature transformer that transforms the features using this transformer while leaving the annotations unchanged.
- [func adaptedAsAnnotatedPredictionTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, AnnotatedPrediction<Self.Output, Annotation>>
](imagerotator/adaptedasannotatedpredictiontransformer(annotationtype:).md)
  Returns an annotated-prediction transformer that transforms the predictions using this transformer while leaving the annotations unchanged.
- [func adaptedAsEstimator() -> TransformerToEstimatorAdaptor<Self>](imagerotator/adaptedasestimator.md)
  Exposes this transformer as a trivial estimator.
- [func adaptedAsRandomTransformer() -> some RandomTransformer<Self.Input, Self.Output>
](imagerotator/adaptedasrandomtransformer.md)
  Returns a random transformer wrapping a transformer.
- [func adaptedAsTemporal() -> TransformerToTemporalAdaptor<Self>](imagerotator/adaptedastemporal.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsUpdatableEstimator() -> TransformerToUpdatableEstimatorAdaptor<Self>](imagerotator/adaptedasupdatableestimator.md)
  Exposes this transformer as a trivial estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](imagerotator/appending(_:)-16sm3.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](imagerotator/appending(_:)-3kjmv.md)
  Composes this transformer with an updatable temporal estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedPrediction<Other.Output, Annotation>>
](imagerotator/appending(_:)-41s36.md)
  Composes this transformer with a prediction-only transformer.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](imagerotator/appending(_:)-4eku7.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedEstimator<Self, Other>](imagerotator/appending(_:)-4glrk.md)
  Composes this transformer with an updatable supervised estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self>, Other>](imagerotator/appending(_:)-4q4kz.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other>(Other) -> ComposedTransformer<Self, Other>](imagerotator/appending(_:)-5zonq.md)
  Composes this transformer with another transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedFeature<Other.Output, Annotation>>
](imagerotator/appending(_:)-7jps6.md)
  Composes this transformer with a feature-only transformer.
- [func appending<Other>(Other) -> PreprocessingSupervisedEstimator<Self, Other>](imagerotator/appending(_:)-7w23p.md)
  Composes this transformer with a supervised estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableEstimator<Self, Other>](imagerotator/appending(_:)-8bwts.md)
  Composes this transformer with an updatable estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TemporalAdaptor<Self>, Other>](imagerotator/appending(_:)-8dm70.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, Other.Output>
](imagerotator/appending(_:)-8hfke.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](imagerotator/appending(_:)-98vc6.md)
  Composes this transformer with a temporal estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, Other.Output>
](imagerotator/appending(_:)-bhmz.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> PreprocessingEstimator<Self, Other>](imagerotator/appending(_:)-n1wv.md)
  Composes this transformer with an estimator.
- [func callAsFunction<S>(S, eventHandler: EventHandler?) async throws -> [Self.Output]](imagerotator/callasfunction(_:eventhandler:)-1bgtr.md)
  Performs the transformation on a sequence of inputs.
- [func callAsFunction(Self.Input, eventHandler: EventHandler?) async throws -> Self.Output](imagerotator/callasfunction(_:eventhandler:)-7xti6.md)
  Performs the transformation on a single input.
- [func export(to: URL) throws](imagerotator/export(to:).md)
  Exports this transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](imagerotator/export(to:metadata:).md)
  Exports this transformer as a CoreML model with userInfo.
- [func prediction<S, Label>(from: S) async throws -> [ClassificationDistribution<Label>]](imagerotator/prediction(from:)-8dc5m.md)
  Performs a prediction from a sequence of inputs.
- [func prediction<Label>(from: Self.Input) async throws -> ClassificationDistribution<Label>](imagerotator/prediction(from:)-bae3.md)
  Performs a prediction from a single input.
- [func prediction<S, Annotation>(from: S, eventHandler: EventHandler?) async throws -> [AnnotatedPrediction<Self.Output, Annotation>]](imagerotator/prediction(from:eventhandler:).md)
  Performs a prediction on a sequence of annotated inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/imagerotator/transformer-implementations)*