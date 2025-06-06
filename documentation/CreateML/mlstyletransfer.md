# MLStyleTransfer

**Framework**: Create ML  
**Kind**: struct

A model you train to apply an image’s style to other images or videos.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct MLStyleTransfer
```

## Topics

### Training a style transfer model asynchronously
- [static func train(trainingData: MLStyleTransfer.DataSource, parameters: MLStyleTransfer.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLStyleTransfer>](mlstyletransfer/train(trainingdata:parameters:sessionparameters:).md)
  Begins an asynchronous style transfer model-training session.
- [static func makeTrainingSession(trainingData: MLStyleTransfer.DataSource, parameters: MLStyleTransfer.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLStyleTransfer>](mlstyletransfer/maketrainingsession(trainingdata:parameters:sessionparameters:).md)
  Creates an asynchronous training session for a style transfer model.
- [static func resume(MLTrainingSession<MLStyleTransfer>) throws -> MLJob<MLStyleTransfer>](mlstyletransfer/resume(_:).md)
  Begins or continues an asynchronous style transfer model-training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLStyleTransfer>](mlstyletransfer/restoretrainingsession(sessionparameters:).md)
  Creates an asynchronous training session for a style transfer model by restoring an existing training session’s state from its parameters.
### Creating a style transfer model from a checkpoint
- [init(checkpoint: MLCheckpoint) throws](mlstyletransfer/init(checkpoint:).md)
  Creates a style transfer model from a training session checkpoint.
### Training a style transfer model synchronously
- [init(trainingData: MLStyleTransfer.DataSource, parameters: MLStyleTransfer.ModelParameters) throws](mlstyletransfer/init(trainingdata:parameters:).md)
  Creates a style transfer model with a training dataset represented by a data source.
### Stylizing an image
- [func stylize(image: CGImage) throws -> CGImage?](mlstyletransfer/stylize(image:).md)
  Applies the style the model learned to an image.
### Saving a style transfer model
- [func write(to: URL, metadata: MLModelMetadata?) throws](mlstyletransfer/write(to:metadata:).md)
  Exports the style transfer model as a Core ML model file to a location in the file system.
- [func write(toFile: String, metadata: MLModelMetadata?) throws](mlstyletransfer/write(tofile:metadata:).md)
  Exports the style transfer model as a Core ML model file to the file path.
### Downloading model assets
- [static func downloadAssets() throws](mlstyletransfer/downloadassets.md)
  Initiates a download of the mlmodel assets required for Style Transfer training. This will be performed automatically if needed at training time, but can be run independently prior to training.
### Describing a style transfer model
- [var description: String](mlstyletransfer/description.md)
  A text representation of the style transfer model.
- [var debugDescription: String](mlstyletransfer/debugdescription.md)
  A text representation of the style transfer model that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlstyletransfer/playgrounddescription.md)
  A description of the style transfer model shown in a playground.
### Supporting types
- [MLStyleTransfer.DataSource](mlstyletransfer/datasource.md)
  A data source for a style transfer model.
- [MLStyleTransfer.ModelParameters](mlstyletransfer/modelparameters.md)
  Parameters that affect the training process of a style transfer model.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlstyletransfer/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlstyletransfer/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlstyletransfer/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Creating an Action Classifier Model](creating-an-action-classifier-model.md)
  Train a machine learning model to recognize a person’s body movements.
- [Detecting Human Actions in a Live Video Feed](detecting_human_actions_in_a_live_video_feed.md)
  Identify body movements by sending a person’s pose data from a series of video frames to an action-classification model.
- [struct MLActionClassifier](mlactionclassifier.md)
  A model you train with videos to classify a person’s body movements.
- [struct MLHandActionClassifier](mlhandactionclassifier.md)
  A task that creates a hand action classification model by training with videos of people’s hand movements that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlstyletransfer)*