# Transformer

**Framework**: Create ML Components  
**Kind**: protocol

A transformer that takes an input and produces an output.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
protocol Transformer<Input, Output>
```

## Topics

### Applying and adapting
- [func applied(to: Self.Input, eventHandler: EventHandler?) async throws -> Self.Output](transformer/applied(to:eventhandler:).md)
  Performs the transformation on a single input.
- [func adaptedAsAnnotatedFeatureTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, AnnotatedFeature<Self.Output, Annotation>>
](transformer/adaptedasannotatedfeaturetransformer(annotationtype:).md)
  Returns an annotated-feature transformer that transforms the features using this transformer while leaving the annotations unchanged.
- [func adaptedAsAnnotatedPredictionTransformer<Annotation>(annotationType: Annotation.Type) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, AnnotatedPrediction<Self.Output, Annotation>>
](transformer/adaptedasannotatedpredictiontransformer(annotationtype:).md)
  Returns an annotated-prediction transformer that transforms the predictions using this transformer while leaving the annotations unchanged.
- [func adaptedAsEstimator() -> TransformerToEstimatorAdaptor<Self>](transformer/adaptedasestimator.md)
  Exposes this transformer as a trivial estimator.
- [func adaptedAsRandomTransformer() -> some RandomTransformer<Self.Input, Self.Output>
](transformer/adaptedasrandomtransformer.md)
  Returns a random transformer wrapping a transformer.
- [func adaptedAsUpdatableEstimator() -> TransformerToUpdatableEstimatorAdaptor<Self>](transformer/adaptedasupdatableestimator.md)
  Exposes this transformer as a trivial estimator.
- [associatedtype Input](transformer/input.md)
  The input type.
- [associatedtype Output](transformer/output.md)
  The output type.
### Appending
- [func appending<Other>(Other) -> PreprocessingSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](transformer/appending(_:)-13v67.md)
  Composes this transformer with a supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](transformer/appending(_:)-2bp6m.md)
  Composes this transformer with a temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](transformer/appending(_:)-2i7p8.md)
  Composes this transformer with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableEstimator<Self, Other>](transformer/appending(_:)-4xmcp.md)
  Composes this transformer with an updatable estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, Other.Output>
](transformer/appending(_:)-51wcs.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> ComposedTransformer<Self, Other>](transformer/appending(_:)-6btna.md)
  Composes this transformer with another transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedPrediction<Other.Output, Annotation>>
](transformer/appending(_:)-6fg5q.md)
  Composes this transformer with a prediction-only transformer.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedEstimator<Self, Other>](transformer/appending(_:)-70fmy.md)
  Composes this transformer with an updatable supervised estimator.
- [func appending<Other>(Other) -> PreprocessingEstimator<Self, Other>](transformer/appending(_:)-86js4.md)
  Composes this transformer with an estimator.
- [func appending<Other, Annotation>(Other) -> some Transformer<Self.Input, AnnotatedFeature<Other.Output, Annotation>>
](transformer/appending(_:)-8y0df.md)
  Composes this transformer with a feature-only transformer.
- [func appending<Other, Annotation>(Other) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, Other.Output>
](transformer/appending(_:)-91f58.md)
  Composes this transformer with an annotated-feature transformer.
- [func appending<Other>(Other) -> PreprocessingSupervisedEstimator<Self, Other>](transformer/appending(_:)-lta.md)
  Composes this transformer with a supervised estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableTemporalEstimator<TransformerToTemporalAdaptor<Self>, Other>](transformer/appending(_:)-qqh2.md)
  Composes this transformer with an updatable temporal estimator.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self>, Other>](transformer/appending(_:)-wd3u.md)
  Composes this transformer with a temporal transformer.
### Transforming and predicting
- [func callAsFunction(Self.Input, eventHandler: EventHandler?) async throws -> Self.Output](transformer/callasfunction(_:eventhandler:)-1xy6d.md)
  Performs the transformation on a single input.
- [func callAsFunction<S>(S, eventHandler: EventHandler?) async throws -> [Self.Output]](transformer/callasfunction(_:eventhandler:)-477jv.md)
  Performs the transformation on a sequence of inputs.
- [func prediction<S, Label>(from: S) async throws -> [ClassificationDistribution<Label>]](transformer/prediction(from:)-107lm.md)
  Performs a prediction from a sequence of inputs.
- [func prediction<Label>(from: Self.Input) async throws -> ClassificationDistribution<Label>](transformer/prediction(from:)-57fan.md)
  Performs a prediction from a single input.
- [func prediction<S, Annotation>(from: S, eventHandler: EventHandler?) async throws -> [AnnotatedPrediction<Self.Output, Annotation>]](transformer/prediction(from:eventhandler:).md)
  Performs a prediction on a sequence of annotated inputs.
### Exporting
- [func export(to: URL) throws](transformer/export(to:).md)
  Exports this transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](transformer/export(to:metadata:).md)
  Exports this transformer as a CoreML model with userInfo.
### Instance Methods
- [func adaptedAsTemporal() -> TransformerToTemporalAdaptor<Self>](transformer/adaptedastemporal-4irar.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsTemporal() -> TemporalAdaptor<Self>](transformer/adaptedastemporal-5p8wr.md)
  Exposes this transformer as a temporal transformer.
- [func appending<Other>(Other) -> ComposedTemporalTransformer<TemporalAdaptor<Self>, Other>](transformer/appending(_:)-9myn0.md)
  Composes this transformer with a temporal transformer.

## Relationships

### Inherited By
- [Classifier](classifier.md)
- [ImageFeatureExtractor](imagefeatureextractor.md)
- [Regressor](regressor.md)
- [TabularTransformer](tabulartransformer.md)
### Conforming Types
- [AudioConvertingTransformer](audioconvertingtransformer.md)
- [AudioReader](audioreader.md)
- [ColumnConcatenator](columnconcatenator.md)
- [ColumnSelectorTransformer](columnselectortransformer.md)
- [ComposedTabularTransformer](composedtabulartransformer.md)
- [ComposedTransformer](composedtransformer.md)
- [DateFeatureExtractor](datefeatureextractor.md)
- [FullyConnectedNetworkClassifierModel](fullyconnectednetworkclassifiermodel.md)
- [FullyConnectedNetworkMultiLabelClassifierModel](fullyconnectednetworkmultilabelclassifiermodel.md)
- [FullyConnectedNetworkRegressorModel](fullyconnectednetworkregressormodel.md)
- [HumanBodyActionPeriodPredictor](humanbodyactionperiodpredictor.md)
- [HumanBodyPoseExtractor](humanbodyposeextractor.md)
- [HumanHandPoseExtractor](humanhandposeextractor.md)
- [ImageBlur](imageblur.md)
- [ImageColorTransformer](imagecolortransformer.md)
- [ImageCropper](imagecropper.md)
- [ImageExposureAdjuster](imageexposureadjuster.md)
- [ImageFeaturePrint](imagefeatureprint.md)
- [ImageFlipper](imageflipper.md)
- [ImageReader](imagereader.md)
- [ImageRotator](imagerotator.md)
- [ImageScaler](imagescaler.md)
- [ImputeTransformer](imputetransformer.md)
- [JointsSelector](jointsselector.md)
- [LinearRegressorModel](linearregressormodel.md)
- [LinearTimeSeriesForecaster.Model](lineartimeseriesforecaster/model.md)
- [LinearTransformer](lineartransformer.md)
- [LogisticRegressionClassifierModel](logisticregressionclassifiermodel.md)
- [MLModelClassifierAdaptor](mlmodelclassifieradaptor.md)
- [MLModelImageFeatureExtractor](mlmodelimagefeatureextractor.md)
- [MLModelRegressorAdaptor](mlmodelregressoradaptor.md)
- [MLModelTransformerAdaptor](mlmodeltransformeradaptor.md)
- [MaxAbsScaler.Transformer](maxabsscaler/transformer.md)
- [MinMaxScaler.Transformer](minmaxscaler/transformer.md)
- [MultivariateLinearRegressor.Model](multivariatelinearregressor/model.md)
- [NormalizationScaler.Transformer](normalizationscaler/transformer.md)
- [OneHotEncoder.Transformer](onehotencoder/transformer.md)
- [OptionalUnwrapper](optionalunwrapper.md)
- [OrdinalEncoder.Transformer](ordinalencoder/transformer.md)
- [PoseSelector](poseselector.md)
- [RandomImageNoiseGenerator](randomimagenoisegenerator.md)
- [Reshaper](reshaper.md)
- [RobustScaler.Transformer](robustscaler/transformer.md)
- [StandardScaler.Transformer](standardscaler/transformer.md)
- [TimeSeriesClassifier.Model](timeseriesclassifier/model.md)
- [TreeClassifierModel](treeclassifiermodel.md)
- [TreeRegressorModel](treeregressormodel.md)
- [VideoReader](videoreader.md)

## See Also

- [protocol TemporalTransformer](temporaltransformer.md)
  A transformer that takes an asynchronous input sequence of temporal features and produces an asynchronous output  sequence.
- [protocol RandomTransformer](randomtransformer.md)
  A transformer that takes an input and a random number generator and produces a randomized output.
- [protocol Estimator](estimator.md)
  An estimator that creates a transformer by fitting to a data set.
- [protocol TemporalEstimator](temporalestimator.md)
  An estimator that creates a transformer by fitting to a sequence of temporal features.
- [protocol SupervisedEstimator](supervisedestimator.md)
  An estimator that creates a transformer by fitting to a data set.
- [protocol SupervisedTemporalEstimator](supervisedtemporalestimator.md)
  An estimator that creates a transformer by fitting to a sequence of annotated temporal features.
- [protocol UpdatableEstimator](updatableestimator.md)
  An estimator that can be incrementally updated.
- [protocol UpdatableSupervisedEstimator](updatablesupervisedestimator.md)
  A supervised estimator that can be incrementally updated.
- [protocol UpdatableSupervisedTemporalEstimator](updatablesupervisedtemporalestimator.md)
  A supervised temporal estimator that can be incrementally updated.
- [protocol UpdatableSupervisedTabularEstimator](updatablesupervisedtabularestimator.md)
  A supervised tabular estimator that can be incrementally updated.
- [protocol UpdatableTemporalEstimator](updatabletemporalestimator.md)
  A temporal estimator that can be incrementally updated.
- [protocol UpdatableTabularEstimator](updatabletabularestimator.md)
  A tabular estimator that can be incrementally updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/transformer)*