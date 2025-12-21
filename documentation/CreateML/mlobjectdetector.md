# MLObjectDetector

**Framework**: Create ML  
**Kind**: struct

A model you train to classify one or more objects within an image.

**Availability**:
- macOS 10.15+

## Declaration

```swift
struct MLObjectDetector
```

## Mentions

- [Building an object detector data source](building-an-object-detector-data-source.md)

#### Overview

Use an [`MLObjectDetector`](mlobjectdetector.md) task to train a machine learning model that can identify items, or , within an image. For example, you can train an object detector to recognize breakfast items on a table, such as bananas, croissants, and beverages.

You create an object detector training it with a combination of images and annotations for each object within an image. Then save it as a Core ML model and use it in your app to recognize similar items.

## Topics

### Creating a data source
- [Building an object detector data source](building-an-object-detector-data-source.md)
  Arrange your training data for an object detector in one of several different structured ways.
### Training an object detector asynchronously
- [static func train(trainingData: MLObjectDetector.DataSource, annotationType: MLObjectDetector.AnnotationType, parameters: MLObjectDetector.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLObjectDetector>](mlobjectdetector/train(trainingdata:annotationtype:parameters:sessionparameters:).md)
  Begins an asynchronous object-detector training session.
- [static func makeTrainingSession(trainingData: MLObjectDetector.DataSource, annotationType: MLObjectDetector.AnnotationType, parameters: MLObjectDetector.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLObjectDetector>](mlobjectdetector/maketrainingsession(trainingdata:annotationtype:parameters:sessionparameters:).md)
  Creates an asynchronous object-detector training session.
- [static func resume(MLTrainingSession<MLObjectDetector>) throws -> MLJob<MLObjectDetector>](mlobjectdetector/resume(_:).md)
  Begins or continues an asynchronous object-detector training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLObjectDetector>](mlobjectdetector/restoretrainingsession(sessionparameters:).md)
  Creates an asynchronous training session for an object detector by restoring an existing training session’s state from its parameters.
### Creating an object detector from a checkpoint
- [init(checkpoint: MLCheckpoint) throws](mlobjectdetector/init(checkpoint:).md)
  Creates an object detector from a training session checkpoint.
### Training an object detector synchronously
- [init(trainingData: MLObjectDetector.DataSource, parameters: MLObjectDetector.ModelParameters, annotationType: MLObjectDetector.AnnotationType) throws](mlobjectdetector/init(trainingdata:parameters:annotationtype:).md)
  Creates an object detector with a data source.
- [init(trainingData: MLDataTable, imageColumn: String, annotationColumn: String, annotationType: MLObjectDetector.AnnotationType, parameters: MLObjectDetector.ModelParameters) throws](mlobjectdetector/init(trainingdata:imagecolumn:annotationcolumn:annotationtype:parameters:).md)
  Creates an object detector with a data table.
### Evaluating an object detector
- [func evaluation(on: MLObjectDetector.DataSource) -> MLObjectDetectorMetrics](mlobjectdetector/evaluation(on:).md)
  Generates metrics by evaluating the object detector’s performance using annotated images in a data source.
- [func evaluation(on: MLDataTable, imageColumn: String, annotationColumn: String) -> MLObjectDetectorMetrics](mlobjectdetector/evaluation(on:imagecolumn:annotationcolumn:).md)
  Generates metrics by evaluating the object detector’s performance using annotated images in a data table.
- [var trainingMetrics: MLObjectDetectorMetrics](mlobjectdetector/trainingmetrics.md)
  Measurements of the object detector’s performance on the training dataset.
- [var validationMetrics: MLObjectDetectorMetrics](mlobjectdetector/validationmetrics.md)
  Measurements of the object detector’s performance on the validation dataset.
### Testing an object detector
- [func prediction(from: URL) throws -> MLObjectDetector.DetectedObjects](mlobjectdetector/prediction(from:).md)
  Locates objects in an image and generates an annotation for each object it detects.
- [func predictions(from: [URL]) throws -> [MLObjectDetector.DetectedObjects]](mlobjectdetector/predictions(from:).md)
  Locates objects in an array of images and generates an array of annotation collections, one for each input image.
- [MLObjectDetector.DetectedObjects](mlobjectdetector/detectedobjects.md)
  An array of annotations that represent the items an object detector found in an image.
- [MLObjectDetector.ObjectAnnotation](mlobjectdetector/objectannotation.md)
  The label, location, and confidence score of an item the object detector found in an image.
### Saving an object detector
- [func write(to: URL, metadata: MLModelMetadata?) throws](mlobjectdetector/write(to:metadata:).md)
  Exports the object detector as a Core ML model file.
- [func write(toFile: String, metadata: MLModelMetadata?) throws](mlobjectdetector/write(tofile:metadata:).md)
  Exports the object detector as a Core ML model file.
### Inspecting an object detector model
- [var model: MLModel](mlobjectdetector/model.md)
  The object detector’s underlying Core ML model instance.
- [let modelParameters: MLObjectDetector.ModelParameters](mlobjectdetector/modelparameters-swift.property.md)
  The model configuration parameters the object detector used during its training session.
### Describing an object detector
- [var description: String](mlobjectdetector/description.md)
  A text representation of the object detector.
- [var debugDescription: String](mlobjectdetector/debugdescription.md)
  A text representation of the object detector that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlobjectdetector/playgrounddescription.md)
  A description of the object detector within a playground.
### Supporting types
- [MLObjectDetector.DataSource](mlobjectdetector/datasource.md)
  A data source for an object detector.
- [MLObjectDetector.AnnotationType](mlobjectdetector/annotationtype.md)
  The available types of image annotations.
- [MLObjectDetector.ModelParameters](mlobjectdetector/modelparameters-swift.struct.md)
  Parameters that affect the process of training an object detection model.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlobjectdetector/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlobjectdetector/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlobjectdetector/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Creating an Image Classifier Model](creating-an-image-classifier-model.md)
  Train a machine learning model to classify images, and add it to your Core ML app.
- [struct MLImageClassifier](mlimageclassifier.md)
  A model you train to classify images.
- [struct MLHandPoseClassifier](mlhandposeclassifier.md)
  A task that creates a hand pose classification model by training with images of people’s hands that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector)*