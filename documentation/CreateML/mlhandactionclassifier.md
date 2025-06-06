# MLHandActionClassifier

**Framework**: Create ML  
**Kind**: struct

A task that creates a hand action classification model by training with videos of people’s hand movements that you provide.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
struct MLHandActionClassifier
```

## Topics

### Training a hand action classifier asynchronously
- [static func train(trainingData: MLHandActionClassifier.DataSource, parameters: MLHandActionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLHandActionClassifier>](mlhandactionclassifier/train(trainingdata:parameters:sessionparameters:).md)
  Begins an asynchronous hand action classifier’s training session.
- [static func makeTrainingSession(trainingData: MLHandActionClassifier.DataSource, parameters: MLHandActionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandActionClassifier>](mlhandactionclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:).md)
  Creates an asynchronous hand action classifier’s training session.
- [static func resume(MLTrainingSession<MLHandActionClassifier>) throws -> MLJob<MLHandActionClassifier>](mlhandactionclassifier/resume(_:).md)
  Begins or continues an asynchronous hand action classifier’s training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandActionClassifier>](mlhandactionclassifier/restoretrainingsession(sessionparameters:).md)
  Recreates an asynchronous hand action classifier’s training session by restoring its saved state from the file system.
### Creating a hand action classifier from a checkpoint
- [init(checkpoint: MLCheckpoint) throws](mlhandactionclassifier/init(checkpoint:).md)
  Creates a hand action classifier from a training session checkpoint.
### Training a hand action classifier synchronously
- [init(trainingData: MLHandActionClassifier.DataSource, parameters: MLHandActionClassifier.ModelParameters) throws](mlhandactionclassifier/init(trainingdata:parameters:).md)
  Creates a hand action classifier by starting a synchronous training session.
### Evaluating a hand action classifier
- [var trainingMetrics: MLClassifierMetrics](mlhandactionclassifier/trainingmetrics.md)
  Measurements of the hand action classifier’s performance on the training dataset.
- [var validationMetrics: MLClassifierMetrics](mlhandactionclassifier/validationmetrics.md)
  Measurements of the hand action classifier’s performance on the validation dataset.
- [func evaluation(on: MLHandActionClassifier.DataSource) throws -> MLClassifierMetrics](mlhandactionclassifier/evaluation(on:).md)
  Generates metrics describing the hand action classifier’s performance on labeled videos.
### Testing a hand action classifier
- [func prediction(from: URL) throws -> [MLHandActionClassifier.Prediction]](mlhandactionclassifier/prediction(from:).md)
  Generates a hand action prediction for a video.
- [func predictions(from: [URL]) throws -> [[MLHandActionClassifier.Prediction]]](mlhandactionclassifier/predictions(from:).md)
  Generates an array of hand action predictions for each video in a URL array.
- [MLHandActionClassifier.Prediction](mlhandactionclassifier/prediction.md)
  A collection of predictions, each paired with its confidence, for a range of video frames.
### Saving a hand action classifier
- [func write(to: URL, metadata: MLModelMetadata?) throws](mlhandactionclassifier/write(to:metadata:).md)
  Exports the hand action classifier as a CoreML model file.
- [func write(toFile: String, metadata: MLModelMetadata?) throws](mlhandactionclassifier/write(tofile:metadata:).md)
  Exports the hand action classifier as a Core ML model file.
### Inspecting a hand action classifier model
- [var model: MLModel](mlhandactionclassifier/model.md)
  The underlying Core ML model of the hand action classifier stored in memory.
- [let modelParameters: MLHandActionClassifier.ModelParameters](mlhandactionclassifier/modelparameters-swift.property.md)
  The hand action model’s configuration parameters.
### Describing a hand action classifier
- [var description: String](mlhandactionclassifier/description.md)
  A text representation of the hand action classifier.
- [var debugDescription: String](mlhandactionclassifier/debugdescription.md)
  A text representation of the hand action classifier suitable for debugging.
- [var playgroundDescription: Any](mlhandactionclassifier/playgrounddescription.md)
  A description of the hand action classifier that’s viewable in a playground.
### Supporting types
- [MLHandActionClassifier.DataSource](mlhandactionclassifier/datasource.md)
  A hand action classifier dataset that contains annotated videos or hand joint location data.
- [MLHandActionClassifier.ModelParameters](mlhandactionclassifier/modelparameters-swift.struct.md)
  A set of parameters that affect the training process of a hand action classifier task.
### Structures
- [MLHandActionClassifier.VideoAugmentationOptions](mlhandactionclassifier/videoaugmentationoptions.md)
  Options a hand action classification training session can use to generate additional training data from the videos you provide.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlhandactionclassifier/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlhandactionclassifier/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlhandactionclassifier/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [Creating an Action Classifier Model](creating-an-action-classifier-model.md)
  Train a machine learning model to recognize a person’s body movements.
- [Detecting Human Actions in a Live Video Feed](detecting_human_actions_in_a_live_video_feed.md)
  Identify body movements by sending a person’s pose data from a series of video frames to an action-classification model.
- [struct MLActionClassifier](mlactionclassifier.md)
  A model you train with videos to classify a person’s body movements.
- [struct MLStyleTransfer](mlstyletransfer.md)
  A model you train to apply an image’s style to other images or videos.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier)*