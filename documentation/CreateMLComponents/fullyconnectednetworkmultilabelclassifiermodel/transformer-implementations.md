# Transformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsAnnotatedFeatureTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, AnnotatedFeature<Self.Output, Annotation>>
](fullyconnectednetworkmultilabelclassifiermodel/adaptedasannotatedfeaturetransformer(annotationtype:).md)
  Returns an annotated-feature transformer that transforms the features using this transformer while leaving the annotations unchanged.
- [func adaptedAsAnnotatedPredictionTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, AnnotatedPrediction<Self.Output, Annotation>>
](fullyconnectednetworkmultilabelclassifiermodel/adaptedasannotatedpredictiontransformer(annotationtype:).md)
  Returns an annotated-prediction transformer that transforms the predictions using this transformer while leaving the annotations unchanged.
- [func adaptedAsEstimator() -> TransformerToEstimatorAdaptor<Self>](fullyconnectednetworkmultilabelclassifiermodel/adaptedasestimator.md)
  Exposes this transformer as a trivial estimator.
- [func adaptedAsRandomTransformer() -> some RandomTransformer<Self.Input, Self.Output>
](fullyconnectednetworkmultilabelclassifiermodel/adaptedasrandomtransformer.md)
  Returns a random transformer wrapping a transformer.
- [func adaptedAsTemporal() -> TransformerToTemporalAdaptor<Self>](fullyconnectednetworkmultilabelclassifiermodel/adaptedastemporal.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsUpdatableEstimator() -> TransformerToUpdatableEstimatorAdaptor<Self>](fullyconnectednetworkmultilabelclassifiermodel/adaptedasupdatableestimator.md)
  Exposes this transformer as a trivial estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self>, Other>](fullyconnectednetworkmultilabelclassifiermodel/appending(_:)-1tch1.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, Other.Output>
](fullyconnectednetworkmultilabelclassifiermodel/appending(_:)-2e9rw.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](fullyconnectednetworkmultilabelclassifiermodel/appending(_:)-2lj1p.md)
  Composes this transformer with a temporal estimator.
- [func appending<Other>(Other) -> PreprocessingEstimator<Self, Other>](fullyconnectednetworkmultilabelclassifiermodel/appending(_:)-2p0ps.md)
  Composes this transformer with an estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedPrediction<Other.Output, Annotation>>
](fullyconnectednetworkmultilabelclassifiermodel/appending(_:)-2zla4.md)
  Composes this transformer with a prediction-only transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedFeature<Other.Output, Annotation>>
](fullyconnectednetworkmultilabelclassifiermodel/appending(_:)-33p2t.md)
  Composes this transformer with a feature-only transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](fullyconnectednetworkmultilabelclassifiermodel/appending(_:)-3jmj2.md)
  Composes this transformer with an updatable temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](fullyconnectednetworkmultilabelclassifiermodel/appending(_:)-3kbf3.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableEstimator<Self, Other>](fullyconnectednetworkmultilabelclassifiermodel/appending(_:)-3sgcu.md)
  Composes this transformer with an updatable estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TemporalAdaptor<Self>, Other>](fullyconnectednetworkmultilabelclassifiermodel/appending(_:)-3waus.md)
  Composes this transformer with a temporal transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedEstimator<Self, Other>](fullyconnectednetworkmultilabelclassifiermodel/appending(_:)-5jpw2.md)
  Composes this transformer with an updatable supervised estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](fullyconnectednetworkmultilabelclassifiermodel/appending(_:)-7bfid.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, Other.Output>
](fullyconnectednetworkmultilabelclassifiermodel/appending(_:)-7z616.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> ComposedTransformer<Self, Other>](fullyconnectednetworkmultilabelclassifiermodel/appending(_:)-8o129.md)
  Composes this transformer with another transformer.
- [func appending<Other>(Other) -> PreprocessingSupervisedEstimator<Self, Other>](fullyconnectednetworkmultilabelclassifiermodel/appending(_:)-r39p.md)
  Composes this transformer with a supervised estimator.
- [func callAsFunction(Self.Input, eventHandler: EventHandler?) async throws -> Self.Output](fullyconnectednetworkmultilabelclassifiermodel/callasfunction(_:eventhandler:)-7qaoh.md)
  Performs the transformation on a single input.
- [func callAsFunction<S>(S, eventHandler: EventHandler?) async throws -> [Self.Output]](fullyconnectednetworkmultilabelclassifiermodel/callasfunction(_:eventhandler:)-i672.md)
  Performs the transformation on a sequence of inputs.
- [func export(to: URL) throws](fullyconnectednetworkmultilabelclassifiermodel/export(to:).md)
  Exports this transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](fullyconnectednetworkmultilabelclassifiermodel/export(to:metadata:).md)
  Exports this transformer as a CoreML model with userInfo.
- [func prediction<Label>(from: Self.Input) async throws -> ClassificationDistribution<Label>](fullyconnectednetworkmultilabelclassifiermodel/prediction(from:)-3r07n.md)
  Performs a prediction from a single input.
- [func prediction<S, Label>(from: S) async throws -> [ClassificationDistribution<Label>]](fullyconnectednetworkmultilabelclassifiermodel/prediction(from:)-6gcz9.md)
  Performs a prediction from a sequence of inputs.
- [func prediction<S, Annotation>(from: S, eventHandler: EventHandler?) async throws -> [AnnotatedPrediction<Self.Output, Annotation>]](fullyconnectednetworkmultilabelclassifiermodel/prediction(from:eventhandler:).md)
  Performs a prediction on a sequence of annotated inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkmultilabelclassifiermodel/transformer-implementations)*