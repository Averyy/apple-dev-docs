# MLHandPoseClassifier

**Framework**: Create ML  
**Kind**: struct

A task that creates a hand pose classification model by training with images of people’s hands that you provide.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
struct MLHandPoseClassifier
```

## Topics

### Training a hand pose classifier asynchronously
- [static func train(trainingData: MLHandPoseClassifier.DataSource, parameters: MLHandPoseClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLHandPoseClassifier>](mlhandposeclassifier/train(trainingdata:parameters:sessionparameters:).md)
  Begins an asynchronous hand pose classifier’s training session.
- [static func makeTrainingSession(trainingData: MLHandPoseClassifier.DataSource, parameters: MLHandPoseClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandPoseClassifier>](mlhandposeclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:).md)
  Creates an asynchronous hand pose classifier’s training session.
- [static func resume(MLTrainingSession<MLHandPoseClassifier>) throws -> MLJob<MLHandPoseClassifier>](mlhandposeclassifier/resume(_:).md)
  Begins or continues an asynchronous hand pose classifier’s training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandPoseClassifier>](mlhandposeclassifier/restoretrainingsession(sessionparameters:).md)
  Recreates an asynchronous hand pose classifier’s training session by restoring its saved state from the file system.
### Creating a hand pose classifier from a checkpoint
- [init(checkpoint: MLCheckpoint) throws](mlhandposeclassifier/init(checkpoint:).md)
  Creates a hand pose classifier from a training session checkpoint.
### Training a hand pose classifier synchronously
- [init(trainingData: MLHandPoseClassifier.DataSource, parameters: MLHandPoseClassifier.ModelParameters) throws](mlhandposeclassifier/init(trainingdata:parameters:).md)
  Creates a hand pose classifier by starting a synchronous training session.
### Evaluating a hand pose classifier
- [var trainingMetrics: MLClassifierMetrics](mlhandposeclassifier/trainingmetrics.md)
  Measurements of the hand pose classifier’s performance on the training dataset.
- [var validationMetrics: MLClassifierMetrics](mlhandposeclassifier/validationmetrics.md)
  Measurements of the hand pose classifier’s performance on the validation dataset.
- [func evaluation(on: MLHandPoseClassifier.DataSource) throws -> MLClassifierMetrics](mlhandposeclassifier/evaluation(on:).md)
  Generates metrics that describe the hand pose classifier’s performance with a dataset of labeled images.
### Testing a hand pose classifier
- [func prediction(from: URL) throws -> [(label: String, confidence: Double)]](mlhandposeclassifier/prediction(from:).md)
  Generates a hand pose prediction for an image.
- [func predictions(from: [URL]) throws -> [[(label: String, confidence: Double)]]](mlhandposeclassifier/predictions(from:).md)
  Generates an array of hand pose predictions for each image in a URL array.
### Saving a hand pose classifier
- [func write(to: URL, metadata: MLModelMetadata?) throws](mlhandposeclassifier/write(to:metadata:).md)
  Exports the hand pose classifier as a CoreML model file.
- [func write(toFile: String, metadata: MLModelMetadata?) throws](mlhandposeclassifier/write(tofile:metadata:).md)
  Exports the hand pose classifier as a Core ML model file.
### Inspecting a hand pose classifier model
- [var model: MLModel](mlhandposeclassifier/model.md)
  The underlying Core ML model of the hand pose classifier stored in memory.
- [let modelParameters: MLHandPoseClassifier.ModelParameters](mlhandposeclassifier/modelparameters-swift.property.md)
  The hand pose model’s configuration parameters.
### Describing a hand pose classifier
- [var description: String](mlhandposeclassifier/description.md)
  A text representation of the hand pose classifier.
- [var debugDescription: String](mlhandposeclassifier/debugdescription.md)
  A text representation of the hand pose classifier suitable for debugging.
- [var playgroundDescription: Any](mlhandposeclassifier/playgrounddescription.md)
  A description of the hand pose classifier that’s viewable in a playground.
### Supporting types
- [MLHandPoseClassifier.DataSource](mlhandposeclassifier/datasource.md)
  A hand pose classifier dataset that contains annotated images or hand joint location data.
- [MLHandPoseClassifier.ModelParameters](mlhandposeclassifier/modelparameters-swift.struct.md)
  A set of parameters that affect the training process of a hand pose classifier task.
### Structures
- [MLHandPoseClassifier.ImageAugmentationOptions](mlhandposeclassifier/imageaugmentationoptions.md)
  Options a hand pose classification training session can use to generate additional training data from the images you provide.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlhandposeclassifier/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlhandposeclassifier/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlhandposeclassifier/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [Creating an Image Classifier Model](creating-an-image-classifier-model.md)
  Train a machine learning model to classify images, and add it to your Core ML app.
- [struct MLImageClassifier](mlimageclassifier.md)
  A model you train to classify images.
- [struct MLObjectDetector](mlobjectdetector.md)
  A model you train to classify one or more objects within an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier)*