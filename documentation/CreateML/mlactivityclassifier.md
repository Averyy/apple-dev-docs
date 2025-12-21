# MLActivityClassifier

**Framework**: Create ML  
**Kind**: struct

A model you train to classify motion sensor data.

**Availability**:
- macOS 10.15+

## Declaration

```swift
struct MLActivityClassifier
```

#### Overview

An activity classifier is a machine-learning model that your app can use to categorize user , based on the motion of the user’s device.

You create an activity classifier by gathering a training dataset of a device’s motion sensors, such as the accelerometer and gyroscope on an Apple Watch. For example, you can create an activity classifier that recognizes a person waving, shaking hands, or throwing a ball by gathering the motion-sensor data from people performing those activities.

Evaluate your trained activity classifier by calling [`evaluation(on:featureColumns:labelColumn:recordingFileColumn:)`](mlactivityclassifier/evaluation(on:featurecolumns:labelcolumn:recordingfilecolumn:)-1ib5p.md) [`evaluation(on:)`](mlsoundclassifier/evaluation(on:)-7fmux.md) with a dataset that’s completely distinct from the training and validation datasets. Inspect the metrics the method returns and decide whether the activity classifier performs with enough accuracy. For example, you can assess how often the activity classifier confuses a person waving for shaking hands, or vice versa. If the classifier makes too many mistakes, you can train another classifier with different parameters, or with a training dataset that has more or better motion-sensor examples.

When you’re satisfied with an activity classifier, save it as a Core ML model file, and add it to your Xcode project. Use it to predict the user’s activity based on the motion-sensor data your app captures from the user’s device.

## Topics

### Training an activity classifier asynchronously
- [static train(trainingData:featureColumns:labelColumn:recordingFileColumn:parameters:sessionParameters:)](mlactivityclassifier/train(trainingdata:featurecolumns:labelcolumn:recordingfilecolumn:parameters:sessionparameters:).md)
  Begins an asynchronous activity classifier training session with a training dataset represented by a data source.
- [static makeTrainingSession(trainingData:featureColumns:labelColumn:recordingFileColumn:parameters:sessionParameters:)](mlactivityclassifier/maketrainingsession(trainingdata:featurecolumns:labelcolumn:recordingfilecolumn:parameters:sessionparameters:).md)
  Creates an asynchronous training session for an activity classifier.
- [static func resume(MLTrainingSession<MLActivityClassifier>) throws -> MLJob<MLActivityClassifier>](mlactivityclassifier/resume(_:).md)
  Begins or continues an asynchronous activity classifier training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLActivityClassifier>](mlactivityclassifier/restoretrainingsession(sessionparameters:).md)
  Creates an asynchronous training session for an activity classifier by restoring an existing training session’s state from its parameters.
### Creating an activity classifier from a checkpoint
- [init(checkpoint: MLCheckpoint) throws](mlactivityclassifier/init(checkpoint:).md)
  Creates an activity classifier from a training session checkpoint.
### Training an activity classifier synchronously
- [init(trainingData:featureColumns:labelColumn:recordingFileColumn:parameters:)](mlactivityclassifier/init(trainingdata:featurecolumns:labelcolumn:recordingfilecolumn:parameters:).md)
  Creates an activity classifier with a training dataset represented by a data source.
### Evaluating an activity classifier
- [func evaluation(on:featureColumns:labelColumn:recordingFileColumn:)](mlactivityclassifier/evaluation(on:featurecolumns:labelcolumn:recordingfilecolumn:).md)
  Generates metrics describing the activity classifier’s performance on labeled activities in a data source.
- [var trainingMetrics: MLClassifierMetrics](mlactivityclassifier/trainingmetrics.md)
  Measurements of the activity classifier’s performance on the training dataset.
- [var validationMetrics: MLClassifierMetrics](mlactivityclassifier/validationmetrics.md)
  Measurements of the activity classifier’s performance on the validation dataset.
- [func evaluation(on:featureColumns:labelColumn:recordingFileColumn:)](mlactivityclassifier/evaluation(on:featurecolumns:labelcolumn:recordingfilecolumn:).md)
  Generates metrics describing the activity classifier’s performance on labeled activities in a data source.
### Testing an activity classifier
- [func predictions(from:perWindowPrediction:)](mlactivityclassifier/predictions(from:perwindowprediction:).md)
  Predict activities from new observations.
### Saving an activity classifier
- [func write(to: URL, metadata: MLModelMetadata?) throws](mlactivityclassifier/write(to:metadata:).md)
  Exports the activity classifier as a Core ML model file.
- [func write(toFile: String, metadata: MLModelMetadata?) throws](mlactivityclassifier/write(tofile:metadata:).md)
  Exports the activity classifier as a Core ML model file.
### Inspecting an activity classifier model
- [var model: MLModel](mlactivityclassifier/model.md)
  The underlying Core ML model of the activity classifier stored in memory.
- [let modelParameters: MLActivityClassifier.ModelParameters](mlactivityclassifier/modelparameters-swift.property.md)
  The model configuration parameters the activity classifier used during its training session.
- [var featureColumns: [String]](mlactivityclassifier/featurecolumns.md)
  The names of the feature columns the activity classifier used during its training session.
- [var labelColumn: String](mlactivityclassifier/labelcolumn.md)
  The name of the label column the activity classifier used during its training session.
- [var recordingFileColumn: String](mlactivityclassifier/recordingfilecolumn.md)
  The name of the column that contains the data files the activity classifier used during its training session.
### Describing an activity classifier
- [var description: String](mlactivityclassifier/description.md)
  A text representation of the activity classifier.
- [var debugDescription: String](mlactivityclassifier/debugdescription.md)
  A text representation of the activity classifier that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlactivityclassifier/playgrounddescription.md)
  A description of the activity classifier shown in a playground.
### Supporting types
- [MLActivityClassifier.DataSource](mlactivityclassifier/datasource.md)
  A data source for an activity classifier.
- [MLActivityClassifier.ModelParameters](mlactivityclassifier/modelparameters-swift.struct.md)
  Model training parameters that direct the training process for an activity classifier model.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlactivityclassifier/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlactivityclassifier/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlactivityclassifier/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier)*