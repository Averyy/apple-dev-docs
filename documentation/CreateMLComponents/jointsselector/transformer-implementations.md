# Transformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsAnnotatedFeatureTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, AnnotatedFeature<Self.Output, Annotation>>
](jointsselector/adaptedasannotatedfeaturetransformer(annotationtype:).md)
  Returns an annotated-feature transformer that transforms the features using this transformer while leaving the annotations unchanged.
- [func adaptedAsAnnotatedPredictionTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, AnnotatedPrediction<Self.Output, Annotation>>
](jointsselector/adaptedasannotatedpredictiontransformer(annotationtype:).md)
  Returns an annotated-prediction transformer that transforms the predictions using this transformer while leaving the annotations unchanged.
- [func adaptedAsEstimator() -> TransformerToEstimatorAdaptor<Self>](jointsselector/adaptedasestimator.md)
  Exposes this transformer as a trivial estimator.
- [func adaptedAsRandomTransformer() -> some RandomTransformer<Self.Input, Self.Output>
](jointsselector/adaptedasrandomtransformer.md)
  Returns a random transformer wrapping a transformer.
- [func adaptedAsTemporal() -> TransformerToTemporalAdaptor<Self>](jointsselector/adaptedastemporal.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsUpdatableEstimator() -> TransformerToUpdatableEstimatorAdaptor<Self>](jointsselector/adaptedasupdatableestimator.md)
  Exposes this transformer as a trivial estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedEstimator<Self, Other>](jointsselector/appending(_:)-1i9ax.md)
  Composes this transformer with a supervised estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedFeature<Other.Output, Annotation>>
](jointsselector/appending(_:)-28k1d.md)
  Composes this transformer with a feature-only transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedPrediction<Other.Output, Annotation>>
](jointsselector/appending(_:)-29sdq.md)
  Composes this transformer with a prediction-only transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedEstimator<Self, Other>](jointsselector/appending(_:)-3t6v7.md)
  Composes this transformer with an updatable supervised estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self>, Other>](jointsselector/appending(_:)-4z7i9.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, Other.Output>
](jointsselector/appending(_:)-5lzuk.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> PreprocessingEstimator<Self, Other>](jointsselector/appending(_:)-5riv8.md)
  Composes this transformer with an estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](jointsselector/appending(_:)-62ng2.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, Other.Output>
](jointsselector/appending(_:)-671t.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](jointsselector/appending(_:)-6c3eq.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](jointsselector/appending(_:)-6n19a.md)
  Composes this transformer with a temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableEstimator<Self, Other>](jointsselector/appending(_:)-9jv8h.md)
  Composes this transformer with an updatable estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](jointsselector/appending(_:)-9xkk0.md)
  Composes this transformer with an updatable temporal estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TemporalAdaptor<Self>, Other>](jointsselector/appending(_:)-etkt.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other>(Other) -> ComposedTransformer<Self, Other>](jointsselector/appending(_:)-gadl.md)
  Composes this transformer with another transformer.
- [func callAsFunction(Self.Input, eventHandler: EventHandler?) async throws -> Self.Output](jointsselector/callasfunction(_:eventhandler:)-1pxfv.md)
  Performs the transformation on a single input.
- [func callAsFunction<S>(S, eventHandler: EventHandler?) async throws -> [Self.Output]](jointsselector/callasfunction(_:eventhandler:)-4h0vf.md)
  Performs the transformation on a sequence of inputs.
- [func export(to: URL) throws](jointsselector/export(to:).md)
  Exports this transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](jointsselector/export(to:metadata:).md)
  Exports this transformer as a CoreML model with userInfo.
- [func prediction<Label>(from: Self.Input) async throws -> ClassificationDistribution<Label>](jointsselector/prediction(from:)-71d9l.md)
  Performs a prediction from a single input.
- [func prediction<S, Label>(from: S) async throws -> [ClassificationDistribution<Label>]](jointsselector/prediction(from:)-77lqt.md)
  Performs a prediction from a sequence of inputs.
- [func prediction<S, Annotation>(from: S, eventHandler: EventHandler?) async throws -> [AnnotatedPrediction<Self.Output, Annotation>]](jointsselector/prediction(from:eventhandler:).md)
  Performs a prediction on a sequence of annotated inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/jointsselector/transformer-implementations)*