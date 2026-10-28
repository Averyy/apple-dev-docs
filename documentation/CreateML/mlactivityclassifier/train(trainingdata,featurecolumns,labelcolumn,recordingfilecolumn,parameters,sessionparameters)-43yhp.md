# train(trainingData:featureColumns:labelColumn:recordingFileColumn:parameters:sessionParameters:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Type Method

Begins an asynchronous activity classifier training session with a training dataset represented by a data table.

**Availability**:
- macOS 11.0+ - Deprecated in 14.0

> **Deprecated**: Use train(trainingData:parameters:sessionParameters:)

## Declaration

```swift
static func train(trainingData: MLDataTable, featureColumns: [String], labelColumn: String, recordingFileColumn: String, parameters: MLActivityClassifier.ModelParameters = ModelParameters(validationData: nil), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLJob<MLActivityClassifier>
```

**Other overloads**:

```swift
static func train(trainingData: MLActivityClassifier.DataSource, featureColumns: [String], labelColumn: String, recordingFileColumn: String, parameters: MLActivityClassifier.ModelParameters = ModelParameters(validationData: nil), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLJob<MLActivityClassifier>
```

## Return Value

An [`MLJob`](../mljob.md) that represents the activity classifier training session.

## Parameters

- `trainingData`: An [`MLDataTable`](../mldatatable.md) instance that contains a collection of sensor data that groups data entries by activity label.
- `featureColumns`: The names of the columns in the data table that contain sensor data.
- `labelColumn`: The name of the column in the data table that contains activity labels.
- `recordingFileColumn`: The name of the column in the data table that contains data filenames.
- `parameters`: An [`MLActivityClassifier.ModelParameters`](./modelparameters-swift.struct.md) instance you use to configure the model for the training session.
- `sessionParameters`: An [`MLTrainingSessionParameters`](../mltrainingsessionparameters.md) instance you use to configure the training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/train(trainingdata:featurecolumns:labelcolumn:recordingfilecolumn:parameters:sessionparameters:)-43yhp)*