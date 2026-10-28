# makeTrainingSession(trainingData:featureColumns:labelColumn:recordingFileColumn:parameters:sessionParameters:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Type Method

Creates an asynchronous training session for an activity classifier.

**Availability**:
- macOS 11.0+ - Deprecated in 14.0

> **Deprecated**: Use makeTrainingSession(trainingData:parameters:sessionParameters:

## Declaration

```swift
static func makeTrainingSession(trainingData: MLDataTable, featureColumns: [String], labelColumn: String, recordingFileColumn: String, parameters: MLActivityClassifier.ModelParameters = ModelParameters(validationData: nil), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLTrainingSession<MLActivityClassifier>
```

**Other overloads**:

```swift
static func makeTrainingSession(trainingData: MLActivityClassifier.DataSource, featureColumns: [String], labelColumn: String, recordingFileColumn: String, parameters: MLActivityClassifier.ModelParameters = .init(), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLTrainingSession<MLActivityClassifier>
```

## Return Value

An [`MLTrainingSession`](../mltrainingsession.md) that represents the activity classifier training session.

## Parameters

- `trainingData`: An [`MLDataTable`](../mldatatable.md) instance that contains a collection of sensor data that groups data entries by activity label.
- `featureColumns`: The names of the columns in the data table that contain sensor data.
- `labelColumn`: The name of the column in the data table that contains activity labels.
- `recordingFileColumn`: The name of the column in the data table that contains data filenames.
- `parameters`: An [`MLActivityClassifier.ModelParameters`](./modelparameters-swift.struct.md) instance you use to configure the model for the training session.
- `sessionParameters`: An [`MLTrainingSessionParameters`](../mltrainingsessionparameters.md) instance you use to configure the training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/maketrainingsession(trainingdata:featurecolumns:labelcolumn:recordingfilecolumn:parameters:sessionparameters:)-3ic8k)*