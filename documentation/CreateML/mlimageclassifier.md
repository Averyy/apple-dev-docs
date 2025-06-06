# MLImageClassifier

**Framework**: Create ML  
**Kind**: struct

A model you train to classify images.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
struct MLImageClassifier
```

## Mentions

- [Improving Your Model’s Accuracy](improving-your-model-s-accuracy.md)
- [Creating an Image Classifier Model](creating-an-image-classifier-model.md)

#### Overview

Use an image classifier to train a machine learning model that you can include in your app to categorize images.

When you create the model, you give it a training dataset made up of labeled images, along with parameters that control the training process. For example, you can provide the model with images of elephants and giraffes, in two folders labeled `Elephant` and `Giraffe`, to train it to recognize these animals.

After training completes, you evaluate the trained model by showing it a testing dataset containing labeled images that the model hasn’t seen before. The metrics that come from this evaluation tell you whether the model performs well enough. For example, you can see how often the elephant and giraffe classifier mistakes a giraffe for an elephant. When the model makes too many mistakes, you can add more or better training data, or change the parameters, and try again.

When your model does perform well enough, you save it as a Core ML model file with the `mlmodel` extension. You can then import this model file into an app—like the [`Classifying Images with Vision and Core ML`](https://developer.apple.com/documentation/coreml/model_integration_samples/classifying_images_with_vision_and_core_ml) sample code project—that uses a Core ML model file to classify images.

## Topics

### Training an image classifier asynchronously
- [static func makeTrainingSession(trainingData: MLImageClassifier.DataSource, parameters: MLImageClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLImageClassifier>](mlimageclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:).md)
  Creates or restores a training session.
- [static func train(trainingData: MLImageClassifier.DataSource, parameters: MLImageClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLImageClassifier>](mlimageclassifier/train(trainingdata:parameters:sessionparameters:).md)
  Begins an asynchronous image classifier training session with a training dataset represented by a data source.
- [static func resume(MLTrainingSession<MLImageClassifier>) throws -> MLJob<MLImageClassifier>](mlimageclassifier/resume(_:).md)
  Begins or continues an asynchronous image classifier training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLImageClassifier>](mlimageclassifier/restoretrainingsession(sessionparameters:).md)
  Creates an asynchronous training session for an image classifier by restoring an existing training session’s state from its parameters.
### Creating an image classifier from a checkpoint
- [init(checkpoint: MLCheckpoint) throws](mlimageclassifier/init(checkpoint:).md)
  Creates an image classifier from a training session checkpoint.
### Training an image classifier synchronously
- [init(trainingData: MLImageClassifier.DataSource, parameters: MLImageClassifier.ModelParameters) throws](mlimageclassifier/init(trainingdata:parameters:)-4r6hr.md)
  Creates an image classifier with a training dataset represented by a data source.
- [init(trainingData: [String : [URL]], parameters: MLImageClassifier.ModelParameters) throws](mlimageclassifier/init(trainingdata:parameters:)-7j4w6.md)
  Creates an image classifier with a training dataset represented by a dictionary.
### Assessing model accuracy
- [var trainingMetrics: MLClassifierMetrics](mlimageclassifier/trainingmetrics.md)
  Measurements of the classifier’s performance on the training data set.
- [var validationMetrics: MLClassifierMetrics](mlimageclassifier/validationmetrics.md)
  Measurements of the image classifier’s performance on the validation dataset.
### Evaluating an image classifier
- [func evaluation(on: MLImageClassifier.DataSource) -> MLClassifierMetrics](mlimageclassifier/evaluation(on:)-9p8mi.md)
  Generates metrics describing the image classifier’s performance on labeled images represented by a data source.
- [func evaluation(on: [String : [URL]]) -> MLClassifierMetrics](mlimageclassifier/evaluation(on:)-7338q.md)
  Generates metrics describing the image classifier’s performance on labeled images represented by a dictionary.
### Testing an image classifier
- [func prediction(from: CGImage) throws -> String](mlimageclassifier/prediction(from:)-97cll.md)
  Generates a prediction for an image.
- [func prediction(from: URL) throws -> String](mlimageclassifier/prediction(from:)-7fitc.md)
  Generates a prediction for an image at the URL.
- [func predictions(from: [URL]) throws -> [String]](mlimageclassifier/predictions(from:).md)
  Generates predictions for an array of images.
### Saving an image classifier
- [func write(to: URL, metadata: MLModelMetadata?) throws](mlimageclassifier/write(to:metadata:).md)
  Exports the image classifier as a Core ML model file to a location in the file system.
- [func write(toFile: String, metadata: MLModelMetadata?) throws](mlimageclassifier/write(tofile:metadata:).md)
  Exports the image classifier as a Core ML model file to the file path.
### Inspecting an image classifier model
- [var model: MLModel](mlimageclassifier/model.md)
  The underlying Core ML model of the image classifier stored in memory.
- [let modelParameters: MLImageClassifier.ModelParameters](mlimageclassifier/modelparameters-swift.property.md)
  The model configuration parameters the image classifier used during its training session.
### Describing an image classifier
- [var description: String](mlimageclassifier/description.md)
  A text representation of the image classifier.
- [var debugDescription: String](mlimageclassifier/debugdescription.md)
  A text representation of the image classifier that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlimageclassifier/playgrounddescription.md)
  A description of the image classifier shown in a playground.
### Supporting types
- [MLImageClassifier.DataSource](mlimageclassifier/datasource.md)
  A data source for an image classifier.
- [MLImageClassifier.ModelParameters](mlimageclassifier/modelparameters-swift.struct.md)
  Parameters that affect the process of training an image classifier model.
### Structures
- [MLImageClassifier.CustomFeatureExtractor](mlimageclassifier/customfeatureextractor.md)
  A custom feature extractor a training session uses to train an image classifier.
- [MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/imageaugmentationoptions.md)
  The variations that the training process can use to generate more training data from the training data you provide.
### Enumerations
- [MLImageClassifier.FeatureExtractorType](mlimageclassifier/featureextractortype.md)
  The underlying base model that extracts image features for image classifier training session.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlimageclassifier/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlimageclassifier/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlimageclassifier/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Creating an Image Classifier Model](creating-an-image-classifier-model.md)
  Train a machine learning model to classify images, and add it to your Core ML app.
- [struct MLObjectDetector](mlobjectdetector.md)
  A model you train to classify one or more objects within an image.
- [struct MLHandPoseClassifier](mlhandposeclassifier.md)
  A task that creates a hand pose classification model by training with images of people’s hands that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier)*