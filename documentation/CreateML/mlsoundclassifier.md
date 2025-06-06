# MLSoundClassifier

**Framework**: Create ML  
**Kind**: struct

A machine learning model you train with audio files to recognize and identify sounds on a device.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
struct MLSoundClassifier
```

#### Overview

A sound classifier is a machine learning model that identifies and categorizes sounds in an app. Create a sound classifier by gathering a dataset of audio files and use them to train a model with [`MLSoundClassifier`](mlsoundclassifier.md).

Assemble an audio dataset by recording or gathering audio files that best represent the sounds you want your app to identify. Additionally, create a  — a group of related noises the sound classifier might hear but aren’t relevant — by collecting or recording example sounds.

For example, say you’re creating a sound classifier to identify laughter and applause. In addition to gathering audio examples of people laughing and clapping, you can add an additional category for background noise. By adding recordings from various settings, such as theaters and amphitheaters, your sound classifier can distinguish the sounds of interest from environmental noises. In other words, the sound classifier won’t predict “Applause” when there isn’t any. Like any classifier, when you request a prediction, a sound classifier always returns one of the categories it learned from a training dataset.

Gather at least 10 audio examples of each sound category you want the sound classifier to learn, plus at least one negative class for background noise. The audio examples can be in any file format that Core Audio supports, including:

- M4A
- MP3
- AIFF
- WAV

> 💡 **Tip**: Use single-channel audio files with a sample rate of 16 kHz or higher for best results.

Use single-channel audio files with a sample rate of 16 kHz or higher for best results.

Reduce a sound classifier’s bias — which can adversely affect its performance — by gathering audio files that use a consistent bit depth and sample rate.

Train, evaluate, and export your sound classifier by following similar steps to creating any other Create ML model type. For more information about the Create ML training workflow, see:

- [`Creating an Image Classifier Model`](creating-an-image-classifier-model.md)
- [`Creating an Action Classifier Model`](creating-an-action-classifier-model.md)

Add the sound classifier’s Core ML model to an Xcode project and use it to create an [`SNClassifySoundRequest`](https://developer.apple.com/documentation/SoundAnalysis/SNClassifySoundRequest) at runtime. Your app uses the sound request to identify sounds in an audio file or audio stream by following the steps in the following articles, respectively:

- [`Classifying Sounds in an Audio File`](https://developer.apple.com/documentation/SoundAnalysis/classifying-sounds-in-an-audio-file)
- [`Classifying Sounds in an Audio Stream`](https://developer.apple.com/documentation/SoundAnalysis/classifying-sounds-in-an-audio-stream)

## Topics

### Training a sound classifier asynchronously
- [static func train(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLSoundClassifier>](mlsoundclassifier/train(trainingdata:parameters:sessionparameters:)-5hdqg.md)
  Begins an asynchronous sound classifier training session with a training dataset represented by a data source.
- [static func train(trainingData: [String : [URL]], parameters: MLSoundClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLSoundClassifier>](mlsoundclassifier/train(trainingdata:parameters:sessionparameters:)-6z4c8.md)
  Begins an asynchronous sound classifier training session with a training dataset represented by a dictionary.
- [static func makeTrainingSession(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLSoundClassifier>](mlsoundclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:).md)
  Creates an asynchronous training session for a sound classifier.
- [static func resume(MLTrainingSession<MLSoundClassifier>) throws -> MLJob<MLSoundClassifier>](mlsoundclassifier/resume(_:).md)
  Begins or continues an asynchronous training session for a sound classifier.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLSoundClassifier>](mlsoundclassifier/restoretrainingsession(sessionparameters:).md)
  Creates an asynchronous training session for a sound classifier by restoring an existing training session’s state from its parameters.
- [static func extractFeatures(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.FeatureExtractionParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLSoundClassifier.DataSource>](mlsoundclassifier/extractfeatures(trainingdata:parameters:sessionparameters:).md)
  Begins an asynchronous session that extracts sound features from a data source of sound files.
- [MLSoundClassifier.FeatureExtractionParameters](mlsoundclassifier/featureextractionparameters.md)
  Parameters that affect the process of extracting sound features from audio files.
### Creating a sound classifier from a checkpoint
- [init(checkpoint: MLCheckpoint) throws](mlsoundclassifier/init(checkpoint:).md)
  Creates a sound classifier from a training session checkpoint.
### Training a sound classifier synchronously
- [init(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.ModelParameters) throws](mlsoundclassifier/init(trainingdata:parameters:)-bztx.md)
  Creates a sound classifier with a training dataset represented by a data source.
- [init(trainingData: [String : [URL]], parameters: MLSoundClassifier.ModelParameters) throws](mlsoundclassifier/init(trainingdata:parameters:)-83tih.md)
  Creates a sound classifier with a training dataset represented by a dictionary.
### Assessing model accuracy
- [var trainingMetrics: MLClassifierMetrics](mlsoundclassifier/trainingmetrics.md)
  Measurements of the classifier’s performance on the training data set.
- [var validationMetrics: MLClassifierMetrics](mlsoundclassifier/validationmetrics.md)
  Measurements of the image classifier’s performance on the validation dataset.
### Evaluating a sound classifier
- [func evaluation(on: MLSoundClassifier.DataSource) -> MLClassifierMetrics](mlsoundclassifier/evaluation(on:)-7fmux.md)
  Generates metrics by evaluating the sound classifier’s performance on a dataset represented by a data source.
- [func evaluation(on: [String : [URL]]) -> MLClassifierMetrics](mlsoundclassifier/evaluation(on:)-8kplo.md)
  Generates metrics by evaluating the sound classifier’s performance on a dataset represented by a dictionary.
### Testing a sound classifier
- [func predictions(from: [URL]) throws -> [String]](mlsoundclassifier/predictions(from:).md)
  Generates predictions for an array of audio files.
- [func predictions(from: [URL], overlapFactor: Double, predictionTimeWindowSize: TimeInterval) throws -> [String]](mlsoundclassifier/predictions(from:overlapfactor:predictiontimewindowsize:).md)
  Generates predictions that use an overlap factor and time window size for an array of audio files.
### Saving a sound classifier
- [func write(to: URL, metadata: MLModelMetadata?) throws](mlsoundclassifier/write(to:metadata:).md)
  Exports the sound classifier as a model file to a location in the file system.
- [func write(toFile: String, metadata: MLModelMetadata?) throws](mlsoundclassifier/write(tofile:metadata:).md)
  Exports the sound classifier as a model file to a path in the file system.
### Inspecting a sound classifier model
- [var model: MLModel](mlsoundclassifier/model.md)
  The underlying model instance of the sound classifier stored in memory.
- [let modelParameters: MLSoundClassifier.ModelParameters](mlsoundclassifier/modelparameters-swift.property.md)
  The model configuration parameters the sound classifier used during its training session.
### Describing a sound classifier
- [var description: String](mlsoundclassifier/description.md)
  A text representation of the sound classifier.
- [var debugDescription: String](mlsoundclassifier/debugdescription.md)
  A text representation of the sound classifier that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlsoundclassifier/playgrounddescription.md)
  A description of the sound classifier in a playground.
### Supporting types
- [MLSoundClassifier.DataSource](mlsoundclassifier/datasource.md)
  A representation of a sound-classifier dataset located in the file system or in a data table.
- [MLSoundClassifier.ModelParameters](mlsoundclassifier/modelparameters-swift.struct.md)
  Parameters that affect the process of training a sound-classifier model.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlsoundclassifier/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlsoundclassifier/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlsoundclassifier/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier)*