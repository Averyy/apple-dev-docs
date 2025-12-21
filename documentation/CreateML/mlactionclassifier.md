# MLActionClassifier

**Framework**: Create ML  
**Kind**: struct

A model you train with videos to classify a person’s body movements.

**Availability**:
- macOS 11.0+

## Declaration

```swift
struct MLActionClassifier
```

## Topics

### Training an action classifier asynchronously
- [static func train(trainingData: MLActionClassifier.DataSource, parameters: MLActionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLActionClassifier>](mlactionclassifier/train(trainingdata:parameters:sessionparameters:).md)
  Begins an asynchronous action classifier training session.
- [static func makeTrainingSession(trainingData: MLActionClassifier.DataSource, parameters: MLActionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLActionClassifier>](mlactionclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:).md)
  Creates an asynchronous training session for an action classifier.
- [static func resume(MLTrainingSession<MLActionClassifier>) throws -> MLJob<MLActionClassifier>](mlactionclassifier/resume(_:).md)
  Begins or continues an asynchronous action classifier training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLActionClassifier>](mlactionclassifier/restoretrainingsession(sessionparameters:).md)
  Creates an asynchronous training session for an action classifier by restoring an existing training session’s state from its parameters.
### Creating an action classifier from a checkpoint
- [init(checkpoint: MLCheckpoint) throws](mlactionclassifier/init(checkpoint:).md)
  Creates an action classifier from a training session checkpoint.
### Training an action classifier synchronously
- [init(trainingData: MLActionClassifier.DataSource, parameters: MLActionClassifier.ModelParameters) throws](mlactionclassifier/init(trainingdata:parameters:).md)
  Creates an action classifier with a training dataset represented by a data source.
### Evaluating an action classifier
- [func evaluation(on: MLActionClassifier.DataSource) throws -> MLClassifierMetrics](mlactionclassifier/evaluation(on:).md)
  Generates metrics describing the action classifier’s performance on labeled videos represented by a data source.
- [var trainingMetrics: MLClassifierMetrics](mlactionclassifier/trainingmetrics.md)
  Measurements of the action classifier’s performance on the training dataset.
- [var validationMetrics: MLClassifierMetrics](mlactionclassifier/validationmetrics.md)
  Measurements of the action classifier’s performance on the validation dataset.
### Testing an action classifier
- [func prediction(from: URL) throws -> [MLActionClassifier.Prediction]](mlactionclassifier/prediction(from:).md)
  Generates a prediction for each action the classifier recognizes in the video.
- [func predictions(from: [URL]) throws -> [[MLActionClassifier.Prediction]]](mlactionclassifier/predictions(from:).md)
  Generates a sequence of predictions for each video input.
- [MLActionClassifier.Prediction](mlactionclassifier/prediction.md)
  A collection of predictions, each paired with its confidence, for a range of video frames.
### Saving an action classifier
- [func write(to: URL, metadata: MLModelMetadata?) throws](mlactionclassifier/write(to:metadata:).md)
  Exports the action classifier as a Core ML model file to a location in the file system.
- [func write(toFile: String, metadata: MLModelMetadata?) throws](mlactionclassifier/write(tofile:metadata:).md)
  Exports the action classifier as a Core ML model file to the file path.
### Inspecting an action classifier model
- [var model: MLModel](mlactionclassifier/model.md)
  The underlying Core ML model of the action classifier stored in memory.
- [let modelParameters: MLActionClassifier.ModelParameters](mlactionclassifier/modelparameters-swift.property.md)
  The model configuration parameters the action classifier used during its training session.
### Describing an action classifier
- [var description: String](mlactionclassifier/description.md)
  A text representation of the action classifier.
- [var debugDescription: String](mlactionclassifier/debugdescription.md)
  A text representation of the action classifier that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlactionclassifier/playgrounddescription.md)
  A description of the action classifier shown in a playground.
### Supporting types
- [MLActionClassifier.DataSource](mlactionclassifier/datasource.md)
  A data source for an action classifier.
- [MLActionClassifier.ModelParameters](mlactionclassifier/modelparameters-swift.struct.md)
  Parameters that affect the training process of an action classifier.
- [MLActionClassifier.VideoAugmentationOptions](mlactionclassifier/videoaugmentationoptions.md)
  The video augmentations for an action classifier training session.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlactionclassifier/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlactionclassifier/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlactionclassifier/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Creating an Action Classifier Model](creating-an-action-classifier-model.md)
  Train a machine learning model to recognize a person’s body movements.
- [Detecting human actions in a live video feed](detecting-human-actions-in-a-live-video-feed.md)
  Identify body movements by sending a person’s pose data from a series of video frames to an action-classification model.
- [struct MLHandActionClassifier](mlhandactionclassifier.md)
  A task that creates a hand action classification model by training with videos of people’s hand movements that you provide.
- [struct MLStyleTransfer](mlstyletransfer.md)
  A model you train to apply an image’s style to other images or videos.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier)*