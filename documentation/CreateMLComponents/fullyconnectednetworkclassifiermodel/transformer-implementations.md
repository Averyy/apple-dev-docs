# Transformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsAnnotatedFeatureTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, AnnotatedFeature<Self.Output, Annotation>>
](fullyconnectednetworkclassifiermodel/adaptedasannotatedfeaturetransformer(annotationtype:).md)
  Returns an annotated-feature transformer that transforms the features using this transformer while leaving the annotations unchanged.
- [func adaptedAsAnnotatedPredictionTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, AnnotatedPrediction<Self.Output, Annotation>>
](fullyconnectednetworkclassifiermodel/adaptedasannotatedpredictiontransformer(annotationtype:).md)
  Returns an annotated-prediction transformer that transforms the predictions using this transformer while leaving the annotations unchanged.
- [func adaptedAsEstimator() -> TransformerToEstimatorAdaptor<Self>](fullyconnectednetworkclassifiermodel/adaptedasestimator.md)
  Exposes this transformer as a trivial estimator.
- [func adaptedAsRandomTransformer() -> some RandomTransformer<Self.Input, Self.Output>
](fullyconnectednetworkclassifiermodel/adaptedasrandomtransformer.md)
  Returns a random transformer wrapping a transformer.
- [func adaptedAsTemporal() -> TemporalAdaptor<Self>](fullyconnectednetworkclassifiermodel/adaptedastemporal-6736t.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsTemporal() -> TransformerToTemporalAdaptor<Self>](fullyconnectednetworkclassifiermodel/adaptedastemporal-71ii4.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsUpdatableEstimator() -> TransformerToUpdatableEstimatorAdaptor<Self>](fullyconnectednetworkclassifiermodel/adaptedasupdatableestimator.md)
  Exposes this transformer as a trivial estimator.
- [func appending<Other>(Other) -> PreprocessingEstimator<Self, Other>](fullyconnectednetworkclassifiermodel/appending(_:)-11y7x.md)
  Composes this transformer with an estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedFeature<Other.Output, Annotation>>
](fullyconnectednetworkclassifiermodel/appending(_:)-384gk.md)
  Composes this transformer with a feature-only transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedPrediction<Other.Output, Annotation>>
](fullyconnectednetworkclassifiermodel/appending(_:)-3d5cy.md)
  Composes this transformer with a prediction-only transformer.
- [func appending<Other>(Other) -> ComposedTransformer<Self, Other>](fullyconnectednetworkclassifiermodel/appending(_:)-5ltze.md)
  Composes this transformer with another transformer.
- [func appending<Other>(Other) -> PreprocessingSupervisedEstimator<Self, Other>](fullyconnectednetworkclassifiermodel/appending(_:)-63nya.md)
  Composes this transformer with a supervised estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableEstimator<Self, Other>](fullyconnectednetworkclassifiermodel/appending(_:)-6jx0k.md)
  Composes this transformer with an updatable estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, Other.Output>
](fullyconnectednetworkclassifiermodel/appending(_:)-6oqi5.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](fullyconnectednetworkclassifiermodel/appending(_:)-6x6jp.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedEstimator<Self, Other>](fullyconnectednetworkclassifiermodel/appending(_:)-70dq9.md)
  Composes this transformer with an updatable supervised estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self>, Other>](fullyconnectednetworkclassifiermodel/appending(_:)-837ui.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](fullyconnectednetworkclassifiermodel/appending(_:)-87a5w.md)
  Composes this transformer with an updatable temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](fullyconnectednetworkclassifiermodel/appending(_:)-8a2e9.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TemporalAdaptor<Self>, Other>](fullyconnectednetworkclassifiermodel/appending(_:)-lj52.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, Other.Output>
](fullyconnectednetworkclassifiermodel/appending(_:)-n2gv.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](fullyconnectednetworkclassifiermodel/appending(_:)-pwks.md)
  Composes this transformer with a temporal estimator.
- [func callAsFunction(Self.Input, eventHandler: EventHandler?) async throws -> Self.Output](fullyconnectednetworkclassifiermodel/callasfunction(_:eventhandler:)-5arud.md)
  Performs the transformation on a single input.
- [func callAsFunction<S>(S, eventHandler: EventHandler?) async throws -> [Self.Output]](fullyconnectednetworkclassifiermodel/callasfunction(_:eventhandler:)-8pcu2.md)
  Performs the transformation on a sequence of inputs.
- [func export(to: URL) throws](fullyconnectednetworkclassifiermodel/export(to:).md)
  Exports this transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](fullyconnectednetworkclassifiermodel/export(to:metadata:).md)
  Exports this transformer as a CoreML model with userInfo.
- [func prediction<Label>(from: Self.Input) async throws -> ClassificationDistribution<Label>](fullyconnectednetworkclassifiermodel/prediction(from:)-4ds7u.md)
  Performs a prediction from a single input.
- [func prediction<S, Label>(from: S) async throws -> [ClassificationDistribution<Label>]](fullyconnectednetworkclassifiermodel/prediction(from:)-gykq.md)
  Performs a prediction from a sequence of inputs.
- [func prediction<S, Annotation>(from: S, eventHandler: EventHandler?) async throws -> [AnnotatedPrediction<Self.Output, Annotation>]](fullyconnectednetworkclassifiermodel/prediction(from:eventhandler:).md)
  Performs a prediction on a sequence of annotated inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkclassifiermodel/transformer-implementations)*