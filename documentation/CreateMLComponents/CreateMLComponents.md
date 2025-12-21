# Create ML Components

**Framework**: Create ML Components  
**Kind**: module

Create more customizable machine learning models in your app.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

#### Overview

Create ML Components is a fundamental technology that exposes the underpinnings of monolithic tasks. You’re in full control and can create custom pipelines for greater flexibility.

![A flowchart that depicts a task represented as 4 component rectangles. The flow begins in the bottom left rectangle which has a camera icon to represent an input image and a label that reads Component 0. This rectangle has two flow arrows — one points up to the single rectangle above the other three rectangles. This top rectangle has a wand and four stars icon that represents an enhancement to the image and a label that reads Component 1. The second flow arrow points to the bottom center rectangle which has a screen within a screen scaling icon that represents the resizing of the image and a label that reads Component 2. Next, the single top rectangle has a flow arrow that points down to the bottom right rectangle which has a photo icon that represents the finished image and a label that reads Component n. A series of three dots connects this rectangle to the center rectangle in the bottom row.](https://docs-assets.developer.apple.com/published/eb40070181caf3b058aa089ccb01534f/create-ml-task%402x.png)

Use components to configure your machine learning tasks with a detailed level of granularity. Choose a specific classifier for images, video, or tabular data.

## Topics

### Image components
- [Augmenting images to expand your training data](augmenting-images-to-expand-your-training-data.md)
  Improve your model by using transformed versions of your training images.
- [Creating a multi-label image classifier](creating-a-multi-label-image-classifier.md)
  Train a machine learning model to assign multiple labels to an image.
- [struct ImageReader](imagereader.md)
  An image file reader.
- [protocol ImageFeatureExtractor](imagefeatureextractor.md)
  A transformer that takes an image and outputs image features.
- [struct ImageCropper](imagecropper.md)
  An image crop transformer.
- [struct ImageScaler](imagescaler.md)
  An image scaling transformer.
- [struct ImageFeaturePrint](imagefeatureprint.md)
  ImageFeaturePrint image feature extractor.
- [struct ImageBlur](imageblur.md)
  An image blurring transformer.
- [struct ImageColorTransformer](imagecolortransformer.md)
  An image color transformer.
- [struct ImageExposureAdjuster](imageexposureadjuster.md)
  An image exposure adjusting transformer.
- [struct ImageFlipper](imageflipper.md)
  An image flipper transformer.
- [struct ImageRotator](imagerotator.md)
  An image rotating transformer.
- [struct RandomImageNoiseGenerator](randomimagenoisegenerator.md)
  A transformer that adds random noise to an image.
- [struct MLModelImageFeatureExtractor](mlmodelimagefeatureextractor.md)
  An image feature extractor provided by an MLModel.
### Pose components
- [Counting human body action repetitions in a live video feed](counting-human-body-action-repetitions-in-a-live-video-feed.md)
  Use Create ML Components to analyze a series of video frames and count a person’s repetitive or periodic body movements.
- [struct Pose](pose.md)
  A pose that contains joint keypoints from a person, a hand, or a combination.
- [struct JointKey](jointkey.md)
  A key that uniquely identifies a joint.
- [struct JointPoint](jointpoint.md)
  A joint in a pose that contains a location and scoring information.
- [struct PoseSelector](poseselector.md)
  A transformer that selects one pose from an array of poses.
- [enum PoseSelectionStrategy](poseselectionstrategy.md)
  Pose selection strategy.
- [struct JointsSelector](jointsselector.md)
  Joints selector from a pose.
- [struct HumanBodyPoseExtractor](humanbodyposeextractor.md)
  The human body pose image feature extractor.
- [struct HumanHandPoseExtractor](humanhandposeextractor.md)
  The human hand pose image feature extractor.
- [struct HumanBodyActionCounter](humanbodyactioncounter.md)
  A human body action repetition counting transformer that takes window of human body poses and produces cumulative human body action repetition counts.
- [struct HumanBodyActionPeriodPredictor](humanbodyactionperiodpredictor.md)
  A human body action period predictor transformer that takes window of poses and produces a window of predictions.
### Audio components
- [struct AudioReader](audioreader.md)
  An audio file reader.
- [struct AudioFeaturePrint](audiofeatureprint.md)
  A stream transformer that extracts audio features from audio buffers.
- [struct AudioConvertingTransformer](audioconvertingtransformer.md)
  A transformer for audio conversion.
### Time-based components
- [Creating a time-series classifier](creating-a-time-series-classifier.md)
  Train a machine learning model to predict the class label of time-series signals.
- [Creating a time-series forecaster](creating-a-time-series-forecaster.md)
  Forecast future data points by training a machine learning model using historical data.
- [struct DateFeatures](datefeatures.md)
  A set of date and time features.
- [struct DateFeatureExtractor](datefeatureextractor.md)
  A time and date feature extractor.
- [struct LinearTimeSeriesForecaster](lineartimeseriesforecaster.md)
  A time-series forecasting estimator.
- [struct LinearTimeSeriesForecasterConfiguration](lineartimeseriesforecasterconfiguration.md)
  The configuration for a linear time-series forecaster.
- [struct TimeSeriesForecasterBatches](timeseriesforecasterbatches.md)
  A sequence of forecaster batches on a time series shaped array.
- [struct TimeSeriesForecasterAnnotatedWindows](timeseriesforecasterannotatedwindows.md)
  A sequence of forecasting windows on a time series shaped array.
- [struct TemporalFeature](temporalfeature.md)
  A temporal feature contains a segment identifier and a feature value.
- [protocol TemporalSequence](temporalsequence.md)
  Async sequence for temporal features.
- [struct TemporalSegmentIdentifier](temporalsegmentidentifier.md)
  Uniquely identifiers a segment of a temporal sequence.
- [struct SlidingWindows](slidingwindows.md)
  A sequence of windows on a time series shaped array.
- [struct SlidingWindowTransformer](slidingwindowtransformer.md)
  A temporal transformer that groups input elements.
- [struct Downsampler](downsampler.md)
  A temporal transformer that down samples the input stream.
- [struct VideoReader](videoreader.md)
  A video file reader.
- [struct TemporalFileSegment](temporalfilesegment.md)
  A URL and a time range identifying a specific segment of a time-based (temporal) file.
- [struct AnyTemporalIterator](anytemporaliterator.md)
  A type-erased async iterator.
- [struct AnyTemporalSequence](anytemporalsequence.md)
  A type-erased temporal sequence.
- [struct PreprocessedFeatureSequence](preprocessedfeaturesequence.md)
  An asynchronous sequence of eagerly stored temporal features.
### Object detection components
- [struct DetectedObject](detectedobject.md)
  An item in a detection result.
- [struct ObjectDetectionAnnotation](objectdetectionannotation.md)
  An object detection annotation.
- [struct ObjectDetectionMetrics](objectdetectionmetrics.md)
  Metrics for object detection model.
### Tabular components
- [protocol TabularTransformer](tabulartransformer.md)
  A tabular transformer that transforms a data frame.
- [protocol TabularEstimator](tabularestimator.md)
  A tabular estimator that creates a transformer by fitting to a data set in a data frame.
- [protocol SupervisedTabularEstimator](supervisedtabularestimator.md)
  A tabular estimator that creates a transformer by fitting to a data set in a data frame.
- [struct ColumnSelector](columnselector.md)
  An operation that applies an estimator to a selection of columns.
- [struct ColumnSelectorTransformer](columnselectortransformer.md)
  A transformer that applies a base transformer to specific columns in a data frame.
- [enum ColumnSelection](columnselection.md)
  A selection of columns from a data frame.
- [struct ColumnConcatenator](columnconcatenator.md)
  A transformer that concatenates every numerical column in a dataframe into to a shaped array for each row.
- [struct PreprocessingSupervisedTabularEstimator](preprocessingsupervisedtabularestimator.md)
  A supervised tabular estimator that composes a preprocessing transformer and a supervised tabular estimator.
- [struct PreprocessingTabularEstimator](preprocessingtabularestimator.md)
  An estimator that composes a preprocessing transformer and an estimator.
- [struct PreprocessingUpdatableSupervisedTabularEstimator](preprocessingupdatablesupervisedtabularestimator.md)
  An updatable supervised estimator that composes a preprocessing transformer and an updatable supervised estimator.
- [struct PreprocessingUpdatableTabularEstimator](preprocessingupdatabletabularestimator.md)
  An updatable estimator that composes a preprocessing transformer and an updatable estimator.
### Protocols
- [protocol Transformer](transformer.md)
  A transformer that takes an input and produces an output.
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
### Core ML adaptors
- [struct MLModelTransformerAdaptor](mlmodeltransformeradaptor.md)
  A transformer that uses a Core ML model.
- [struct MLModelClassifierAdaptor](mlmodelclassifieradaptor.md)
  A transformer that uses a Core ML model as a classifier.
- [struct MLModelRegressorAdaptor](mlmodelregressoradaptor.md)
  A transformer that uses a Core ML model as a regressor.
- [struct ModelMetadata](modelmetadata.md)
  User info keys that specify useful information about a model.
### Annotations
- [struct AnnotatedFiles](annotatedfiles.md)
  An annotated files collection.
- [struct AnnotatedBatch](annotatedbatch.md)
  A batch of annotated examples for fitting a supervised estimator.
- [struct AnnotatedFeature](annotatedfeature.md)
  An annotated example for fitting a supervised estimator.
- [struct AnnotatedFeatureProvider](annotatedfeatureprovider.md)
  An adaptor that converts a regular estimator to a tabular estimator by selecting features and annotations from columns.
- [struct AnnotatedPrediction](annotatedprediction.md)
  An annotated prediction.
- [struct DataFrameTemporalAnnotationParameters](dataframetemporalannotationparameters.md)
  Annotation parameters for the dataframe containing temporal annotations.
### Augmentations
- [struct ApplyEachRandomly](applyeachrandomly.md)
  Applies each transformer randomly given a probability.
- [struct ApplyRandomly](applyrandomly.md)
  Randomly applies the transformer with the given probability.
- [struct AugmentationBuilder](augmentationbuilder.md)
  A series of augmentations.
- [struct AugmentationSequence](augmentationsequence.md)
  An async sequence of augmented elements.
- [struct Augmenter](augmenter.md)
  An augmenter.
- [struct ChooseRandomly](chooserandomly.md)
  Apply single transformation randomly chosen from a list of transformers.
- [struct RandomImageCropper](randomimagecropper.md)
  Crops an image at a random location.
- [struct ShuffleRandomly](shufflerandomly.md)
  Apply transformations in a random order.
- [struct UniformRandomFloatingPointParameter](uniformrandomfloatingpointparameter.md)
  Applies the transformer with a randomly generated input parameter.
- [class UniformRandomIntegerParameter](uniformrandomintegerparameter.md)
  Applies the transformer with a randomly generated input parameter.
- [struct UpsampledAugmentationSequence](upsampledaugmentationsequence.md)
  An async sequence of augmented elements.
### Event handling
- [struct Event](event.md)
  Maintains the status of the pipeline.
- [typealias EventHandler](eventhandler.md)
  A closure to handle processing events.
- [struct MetricsKey](metricskey.md)
  A key that uniquely identifies a metric.
### Scalers
- [struct StandardScaler](standardscaler.md)
  An estimator that standardizes the input by removing the mean and scaling to unit variance.
- [struct MaxAbsScaler](maxabsscaler.md)
  An estimator that scales the input values so that the maximum absolute value is 1.0.
- [struct MinMaxScaler](minmaxscaler.md)
  An estimator that scales the input values so that they all lie in a closed range.
- [struct NormalizationScaler](normalizationscaler.md)
  An estimator that normalizes the input values using a normalization strategy.
- [struct RobustScaler](robustscaler.md)
  An estimator that scales the input using statistics that are robust to outliers.
### Preprocessors
- [struct LinearTransformer](lineartransformer.md)
  A transformer that runs an input through a scale and offset.
- [struct ImputeTransformer](imputetransformer.md)
  A transformer that replaces missing values with a pre-defined value.
- [struct OneHotEncoder](onehotencoder.md)
  An estimator that encodes categorical values to an integer array.
- [struct OrdinalEncoder](ordinalencoder.md)
  An ordinal encoder estimator encodes categorical values to ordinal integer values.
- [struct NumericImputer](numericimputer.md)
  An estimator that replaces missing values in the numeric input.
- [struct Reshaper](reshaper.md)
  A transformer that reshapes a shaped array.
- [struct CategoricalImputer](categoricalimputer.md)
  An estimator that replaces missing values in the categorical input.
- [struct OptionalUnwrapper](optionalunwrapper.md)
  A transformer that unwraps optional elements and throws when encountering missing values.
### Regressors
- [protocol Regressor](regressor.md)
  A transformer that predicts a float value.
- [struct LinearRegressor](linearregressor.md)
  A linear regressor.
- [struct LinearRegressorModel](linearregressormodel.md)
  A trained linear regressor model.
- [struct MultivariateLinearRegressor](multivariatelinearregressor.md)
  A multivariate linear regressor.
- [struct MultivariateLinearRegressorConfiguration](multivariatelinearregressorconfiguration.md)
  A linear regressor configuration.
- [MultivariateLinearRegressor.Model](multivariatelinearregressor/model.md)
  A trained multivariate linear regressor model.
- [struct FullyConnectedNetworkRegressor](fullyconnectednetworkregressor.md)
  A regressor that uses a fully connected network.
- [struct FullyConnectedNetworkRegressorModel](fullyconnectednetworkregressormodel.md)
  A regressor model that uses a fully connected network.
- [struct BoostedTreeRegressor](boostedtreeregressor.md)
  A gradient boosted decision tree regressor.
- [struct TreeRegressorModel](treeregressormodel.md)
  A trained tree regressor model.
- [enum OptimizationStrategy](optimizationstrategy.md)
  A linear optimization strategy.
### Serializers
- [protocol EstimatorDecoder](estimatordecoder.md)
  A type that can decode values from a model representation.
- [protocol EstimatorEncoder](estimatorencoder.md)
  A type that can encode values into a model representation.
### Classifiers
- [protocol Classifier](classifier.md)
  An estimator that predicts classification probabilities.
- [struct LogisticRegressionClassifier](logisticregressionclassifier.md)
  A logistic regression classifier.
- [struct LogisticRegressionClassifierModel](logisticregressionclassifiermodel.md)
  A trained logistic regression classifier model.
- [struct BoostedTreeClassifier](boostedtreeclassifier.md)
  A gradient boosted decision tree classifier.
- [struct BoostedTreeConfiguration](boostedtreeconfiguration.md)
  A boosted tree configuration.
- [struct FullyConnectedNetworkClassifier](fullyconnectednetworkclassifier.md)
  A classifier that uses a fully connected network.
- [struct FullyConnectedNetworkClassifierModel](fullyconnectednetworkclassifiermodel.md)
  A classifier model that uses a fully connected network.
- [struct FullyConnectedNetworkMultiLabelClassifier](fullyconnectednetworkmultilabelclassifier.md)
  A classifier that uses a multi-label fully-connected network.
- [struct FullyConnectedNetworkMultiLabelClassifierModel](fullyconnectednetworkmultilabelclassifiermodel.md)
  A multi-label classifier model that uses a fully-connected network.
- [struct FullyConnectedNetworkConfiguration](fullyconnectednetworkconfiguration.md)
  A fully connected network configuration.
- [struct TreeClassifierModel](treeclassifiermodel.md)
  A trained tree classifier model.
- [struct TimeSeriesClassifier](timeseriesclassifier.md)
- [struct TimeSeriesClassifierConfiguration](timeseriesclassifierconfiguration.md)
  The configuration for a time-series classifier.
### Metrics
- [struct Classification](classification.md)
  An item in a classification result.
- [struct ClassificationDistribution](classificationdistribution.md)
  A classification distribution that contains a probability for each classification label.
- [struct ClassificationMetrics](classificationmetrics.md)
  Classification metrics.
- [struct MultiLabelClassificationMetrics](multilabelclassificationmetrics.md)
  Multi-label classification metrics.
- [func rootMeanSquaredError<T>([AnnotatedPrediction<T, T>]) -> T](rootmeansquarederror(_:).md)
  Computes the root mean squared error between predicted and ground truth values.
- [func rootMeanSquaredError<T>(some Collection, some Collection) -> T](rootmeansquarederror(_:_:).md)
  Computes the root mean squared error between predicted and ground truth values.
- [func maximumAbsoluteError<T>([AnnotatedPrediction<T, T>]) -> T](maximumabsoluteerror(_:).md)
  Computes the maximum absolute error between predicted and ground truth values.
- [func maximumAbsoluteError<T>(some Collection, some Collection) -> T](maximumabsoluteerror(_:_:).md)
  Computes the maximum absolute error between predicted and ground truth values.
- [func meanAbsoluteError<T>([AnnotatedPrediction<T, T>]) -> T](meanabsoluteerror(_:).md)
  Computes the mean absolute error between predicted and ground truth values.
- [func meanAbsoluteError<T>(some Collection, some Collection) -> T](meanabsoluteerror(_:_:).md)
  Computes the mean absolute error between predicted and ground truth values.
- [func meanAbsolutePercentageError<T>([AnnotatedPrediction<T, T>]) -> T](meanabsolutepercentageerror(_:).md)
  Computes the mean absolute percentage error between predicted and ground truth values.
- [func meanSquaredError<T>([AnnotatedPrediction<T, T>]) -> T](meansquarederror(_:).md)
  Computes the root mean squared error between predicted and ground truth values.
- [func meanSquaredError<T>(some Collection, some Collection) -> T](meansquarederror(_:_:).md)
  Computes the mean squared error between predicted and ground truth values.
### Transformer adaptors
- [struct TransformerToEstimatorAdaptor](transformertoestimatoradaptor.md)
  An estimator that always returns a predefined transformer.
- [struct TransformerToTemporalAdaptor](transformertotemporaladaptor.md)
  A temporal transformer that applies a regular transformer to each value of a temporal sequence.
- [struct TransformerToUpdatableEstimatorAdaptor](transformertoupdatableestimatoradaptor.md)
  An updatable estimator that always returns a predefined transformer.
### Updatable adaptors
- [struct UpdatableEstimatorToTemporalAdaptor](updatableestimatortotemporaladaptor.md)
  An updatable temporal estimator wrapping an updatable estimator.
- [struct UpdatableEstimatorToSupervisedAdaptor](updatableestimatortosupervisedadaptor.md)
  An adaptor that exposes an updatable estimator as an updatable supervised estimator.
- [struct UpdatableSupervisedEstimatorToTemporalAdaptor](updatablesupervisedestimatortotemporaladaptor.md)
  An updatable supervised temporal estimator wrapping an updatable supervised estimator.
- [struct UpdatableTemporalEstimatorToSupervisedAdaptor](updatabletemporalestimatortosupervisedadaptor.md)
  An adaptor that exposes an updatable temporal estimator as an updatable supervised temporal estimator.
### Estimator adaptors
- [struct EstimatorToSupervisedAdaptor](estimatortosupervisedadaptor.md)
  An adaptor that exposes an estimator as a supervised estimator.
- [struct EstimatorToTemporalAdaptor](estimatortotemporaladaptor.md)
  A temporal estimator wrapping an estimator.
- [struct SupervisedEstimatorToTemporalAdaptor](supervisedestimatortotemporaladaptor.md)
  A supervised temporal estimator wrapping a supervised estimator.
### Tabular adaptors
- [struct TabularEstimatorToSupervisedAdaptor](tabularestimatortosupervisedadaptor.md)
  An adaptor that exposes a tabular estimator as a tabular supervised estimator.
- [struct TabularTransformerToEstimatorAdaptor](tabulartransformertoestimatoradaptor.md)
  A tabular estimator that always returns a predefined tabular transformer.
- [struct TabularTransformerToUpdatableEstimatorAdaptor](tabulartransformertoupdatableestimatoradaptor.md)
  An updatable tabular estimator that always returns a predefined transformer.
- [struct UpdatableTabularEstimatorToSupervisedAdaptor](updatabletabularestimatortosupervisedadaptor.md)
  An adaptor that exposes an updatable tabular estimator as an updatable supervised tabular estimator.
### Temporal adaptors
- [struct TemporalAdaptor](temporaladaptor.md)
  A temporal transformer that applies a regular transformer to each value of a temporal sequence.
- [struct TemporalTransformerToEstimatorAdaptor](temporaltransformertoestimatoradaptor.md)
  A temporal estimator that always returns a predefined temporal transformer.
- [struct TemporalEstimatorToSupervisedAdaptor](temporalestimatortosupervisedadaptor.md)
  An adaptor that exposes a temporal estimator as a supervised temporal estimator.
- [struct TemporalTransformerToUpdatableEstimatorAdaptor](temporaltransformertoupdatableestimatoradaptor.md)
  A temporal estimator that always returns a predefined temporal transformer.
### Composition with preprocessing
- [struct PreprocessingEstimator](preprocessingestimator.md)
  An estimator that composes a preprocessing transformer and an estimator.
- [struct PreprocessingTemporalEstimator](preprocessingtemporalestimator.md)
  A temporal estimator that composes a preprocessing transformer and a temporal estimator.
- [struct PreprocessingSupervisedEstimator](preprocessingsupervisedestimator.md)
  A supervised estimator that composes a preprocessing transformer and a supervised estimator.
- [struct PreprocessingSupervisedTemporalEstimator](preprocessingsupervisedtemporalestimator.md)
  A supervised temporal estimator that composes a preprocessing transformer and a supervised temporal estimator.
- [struct PreprocessingUpdatableEstimator](preprocessingupdatableestimator.md)
  An updatable estimator that composes a preprocessing transformer and an updatable estimator.
- [struct PreprocessingUpdatableTemporalEstimator](preprocessingupdatabletemporalestimator.md)
  An updatable temporal estimator that composes a preprocessing transformer and an updatable temporal estimator.
- [struct PreprocessingUpdatableSupervisedEstimator](preprocessingupdatablesupervisedestimator.md)
  An updatable supervised estimator that composes a preprocessing transformer and an updatable supervised estimator.
- [struct PreprocessingUpdatableSupervisedTemporalEstimator](preprocessingupdatablesupervisedtemporalestimator.md)
  An updatable supervised temporal estimator that composes a preprocessing transformer and an updatable supervised temporal estimator.
### Composition
- [struct ComposedTransformer](composedtransformer.md)
  A transformer that composes two transformers by applying them one after the other.
- [struct ComposedTemporalTransformer](composedtemporaltransformer.md)
  A temporal transformer that composes two temporal transformers by applying them one after the other.
- [struct ComposedTabularTransformer](composedtabulartransformer.md)
  A transformer that composes two tabular transformers by applying them one after the other.
### Errors
- [enum AudioPreprocessingError](audiopreprocessingerror.md)
  Audio preprocessing errors.
- [enum AudioReaderError](audioreadererror.md)
  Audio reader errors.
- [enum CompatibilityError](compatibilityerror.md)
  A compatibility error.
- [enum ConcatenationError](concatenationerror.md)
  Errors thrown when concatenating numeric values.
- [enum DatasetError](dataseterror.md)
  Dataset processing errors.
- [enum EstimatorEncodingError](estimatorencodingerror.md)
  An estimator encoding error.
- [enum ModelCompatibilityError](modelcompatibilityerror.md)
  Errors related to CoreML model compatibility.
- [enum ModelUpdateError](modelupdateerror.md)
  An updatable model error.
- [enum OptimizationError](optimizationerror.md)
  An optimization error.
- [enum PipelineDataError](pipelinedataerror.md)
  Errors related to pipeline data affinity problems.
- [enum SerializationError](serializationerror.md)
  A serialization error.
- [enum TabularPipelineDataError](tabularpipelinedataerror.md)
  Errors related to tabular pipeline data affinity problems.
- [enum VideoReaderError](videoreadererror.md)
  Video loader errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CreateMLComponents)*