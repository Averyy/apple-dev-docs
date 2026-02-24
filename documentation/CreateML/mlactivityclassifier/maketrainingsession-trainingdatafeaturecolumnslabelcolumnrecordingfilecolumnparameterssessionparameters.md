# makeTrainingSession(trainingData:featureColumns:labelColumn:recordingFileColumn:parameters:sessionParameters:)

**Framework**: Create ML  
**Kind**: method

Creates an asynchronous training session for an activity classifier.

**Availability**:
- macOS 14.0+

## Declaration

```swift
static func makeTrainingSession(trainingData: MLActivityClassifier.DataSource, featureColumns: [String], labelColumn: String, recordingFileColumn: String, parameters: MLActivityClassifier.ModelParameters = .init(), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLTrainingSession<MLActivityClassifier>
```

#### Return Value

An [`MLTrainingSession`](mltrainingsession.md) that represents the activity classifier training session.

## Parameters

- `trainingData`: An [`MLDataTable`](mldatatable.md) instance that contains a collection of sensor data that groups data entries by activity label.
- `featureColumns`: The feature column names.
- `labelColumn`: The label column name,
- `recordingFileColumn`: The recording file column name.
- `parameters`: An [`MLActivityClassifier.ModelParameters`](mlactivityclassifier/modelparameters-swift.struct.md) instance you use to configure the model for the training session.
- `sessionParameters`: An [`MLTrainingSessionParameters`](mltrainingsessionparameters.md) instance you use to configure the training session.

## See Also

- [static train(trainingData:featureColumns:labelColumn:recordingFileColumn:parameters:sessionParameters:)](mlactivityclassifier/train(trainingdata:featurecolumns:labelcolumn:recordingfilecolumn:parameters:sessionparameters:).md)
  Begins an asynchronous activity classifier training session with a training dataset represented by a data source.
- [static func resume(MLTrainingSession<MLActivityClassifier>) throws -> MLJob<MLActivityClassifier>](mlactivityclassifier/resume(_:).md)
  Begins or continues an asynchronous activity classifier training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLActivityClassifier>](mlactivityclassifier/restoretrainingsession(sessionparameters:).md)
  Creates an asynchronous training session for an activity classifier by restoring an existing training session’s state from its parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/maketrainingsession(trainingdata:featurecolumns:labelcolumn:recordingfilecolumn:parameters:sessionparameters:))*