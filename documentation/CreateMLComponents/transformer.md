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
- [func adaptedAsTemporal()](transformer/adaptedastemporal.md)
  Exposes this transformer as a temporal transformer.
- [func adaptedAsUpdatableEstimator() -> TransformerToUpdatableEstimatorAdaptor<Self>](transformer/adaptedasupdatableestimator.md)
  Exposes this transformer as a trivial estimator.
- [associatedtype Input](transformer/input.md)
  The input type.
- [associatedtype Output](transformer/output.md)
  The output type.
### Appending
- [func appending(_:)](transformer/appending(_:).md)
  Composes this transformer with an annotated-feature transformer.
### Transforming and predicting
- [func callAsFunction(_:eventHandler:)](transformer/callasfunction(_:eventhandler:).md)
  Performs the transformation on a single input.
- [func prediction(from:)](transformer/prediction(from:).md)
  Performs a prediction from a single input.
- [func prediction<S, Annotation>(from: S, eventHandler: EventHandler?) async throws -> [AnnotatedPrediction<Self.Output, Annotation>]](transformer/prediction(from:eventhandler:).md)
  Performs a prediction on a sequence of annotated inputs.
### Exporting
- [func export(to: URL) throws](transformer/export(to:).md)
  Exports this transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](transformer/export(to:metadata:).md)
  Exports this transformer as a CoreML model with userInfo.

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