# Transformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsAnnotatedFeatureTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, AnnotatedFeature<Self.Output, Annotation>>
](linearregressormodel/adaptedasannotatedfeaturetransformer(annotationtype:).md)
  Returns an annotated-feature transformer that transforms the features using this transformer while leaving the annotations unchanged.
- [func adaptedAsAnnotatedPredictionTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, AnnotatedPrediction<Self.Output, Annotation>>
](linearregressormodel/adaptedasannotatedpredictiontransformer(annotationtype:).md)
  Returns an annotated-prediction transformer that transforms the predictions using this transformer while leaving the annotations unchanged.
- [func adaptedAsEstimator() -> TransformerToEstimatorAdaptor<Self>](linearregressormodel/adaptedasestimator.md)
  Exposes this transformer as a trivial estimator.
- [func adaptedAsRandomTransformer() -> some RandomTransformer<Self.Input, Self.Output>
](linearregressormodel/adaptedasrandomtransformer.md)
  Returns a random transformer wrapping a transformer.
- [func adaptedAsTemporal() -> TransformerToTemporalAdaptor<Self>](linearregressormodel/adaptedastemporal-6p4uw.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsTemporal() -> TemporalAdaptor<Self>](linearregressormodel/adaptedastemporal-y3w6.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsUpdatableEstimator() -> TransformerToUpdatableEstimatorAdaptor<Self>](linearregressormodel/adaptedasupdatableestimator.md)
  Exposes this transformer as a trivial estimator.
- [func appending<Other>(Other) -> PreprocessingEstimator<Self, Other>](linearregressormodel/appending(_:)-1751k.md)
  Composes this transformer with an estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](linearregressormodel/appending(_:)-1dbeb.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](linearregressormodel/appending(_:)-1li7c.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedEstimator<Self, Other>](linearregressormodel/appending(_:)-24fgh.md)
  Composes this transformer with a supervised estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedFeature<Other.Output, Annotation>>
](linearregressormodel/appending(_:)-2aam7.md)
  Composes this transformer with a feature-only transformer.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](linearregressormodel/appending(_:)-2k57r.md)
  Composes this transformer with a temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableEstimator<Self, Other>](linearregressormodel/appending(_:)-3gabg.md)
  Composes this transformer with an updatable estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TemporalAdaptor<Self>, Other>](linearregressormodel/appending(_:)-3pha2.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedPrediction<Other.Output, Annotation>>
](linearregressormodel/appending(_:)-425fq.md)
  Composes this transformer with a prediction-only transformer.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self>, Other>](linearregressormodel/appending(_:)-4ioom.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedEstimator<Self, Other>](linearregressormodel/appending(_:)-4rn34.md)
  Composes this transformer with an updatable supervised estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](linearregressormodel/appending(_:)-53wwo.md)
  Composes this transformer with an updatable temporal estimator.
- [func appending<Other>(Other) -> ComposedTransformer<Self, Other>](linearregressormodel/appending(_:)-6rx3h.md)
  Composes this transformer with another transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, Other.Output>
](linearregressormodel/appending(_:)-7035h.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, Other.Output>
](linearregressormodel/appending(_:)-87k26.md)
  Composes this transformer with an annotated-feature transformer.
- [func callAsFunction(Self.Input, eventHandler: EventHandler?) async throws -> Self.Output](linearregressormodel/callasfunction(_:eventhandler:)-4iwrp.md)
  Performs the transformation on a single input.
- [func callAsFunction<S>(S, eventHandler: EventHandler?) async throws -> [Self.Output]](linearregressormodel/callasfunction(_:eventhandler:)-58vj.md)
  Performs the transformation on a sequence of inputs.
- [func export(to: URL) throws](linearregressormodel/export(to:).md)
  Exports this transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](linearregressormodel/export(to:metadata:).md)
  Exports this transformer as a CoreML model with userInfo.
- [func prediction<S, Annotation>(from: S, eventHandler: EventHandler?) async throws -> [AnnotatedPrediction<Self.Output, Annotation>]](linearregressormodel/prediction(from:eventhandler:).md)
  Performs a prediction on a sequence of annotated inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/linearregressormodel/transformer-implementations)*