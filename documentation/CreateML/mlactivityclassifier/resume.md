# resume(_:)

**Framework**: Create ML  
**Kind**: method

Begins or continues an asynchronous activity classifier training session.

**Availability**:
- macOS 11.0+

## Declaration

```swift
static func resume(_ session: MLTrainingSession<MLActivityClassifier>) throws -> MLJob<MLActivityClassifier>
```

#### Return Value

An [`MLJob`](mljob.md) that represents the activity classifier training session.

## Parameters

- `session`: An   instance that represents the training session.

## See Also

- [static func train(trainingData: MLActivityClassifier.DataSource, featureColumns: [String], labelColumn: String, recordingFileColumn: String, parameters: MLActivityClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLActivityClassifier>](mlactivityclassifier/train(trainingdata:featurecolumns:labelcolumn:recordingfilecolumn:parameters:sessionparameters:)-6oapt.md)
  Begins an asynchronous activity classifier training session with a training dataset represented by a data source.
- [static func train(trainingData: MLDataTable, featureColumns: [String], labelColumn: String, recordingFileColumn: String, parameters: MLActivityClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLActivityClassifier>](mlactivityclassifier/train(trainingdata:featurecolumns:labelcolumn:recordingfilecolumn:parameters:sessionparameters:)-43yhp.md)
  Begins an asynchronous activity classifier training session with a training dataset represented by a data table.
- [static func makeTrainingSession(trainingData: MLDataTable, featureColumns: [String], labelColumn: String, recordingFileColumn: String, parameters: MLActivityClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLActivityClassifier>](mlactivityclassifier/maketrainingsession(trainingdata:featurecolumns:labelcolumn:recordingfilecolumn:parameters:sessionparameters:)-3ic8k.md)
  Creates an asynchronous training session for an activity classifier.
- [static func makeTrainingSession(trainingData: MLActivityClassifier.DataSource, featureColumns: [String], labelColumn: String, recordingFileColumn: String, parameters: MLActivityClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLActivityClassifier>](mlactivityclassifier/maketrainingsession(trainingdata:featurecolumns:labelcolumn:recordingfilecolumn:parameters:sessionparameters:)-dk66.md)
  Creates an asynchronous training session for an activity classifier.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLActivityClassifier>](mlactivityclassifier/restoretrainingsession(sessionparameters:).md)
  Creates an asynchronous training session for an activity classifier by restoring an existing training session’s state from its parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/resume(_:))*