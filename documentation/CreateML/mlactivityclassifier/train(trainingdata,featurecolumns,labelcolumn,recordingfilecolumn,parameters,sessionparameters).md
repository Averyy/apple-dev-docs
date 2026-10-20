# train(trainingData:featureColumns:labelColumn:recordingFileColumn:parameters:sessionParameters:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Type Method

Begins an asynchronous activity classifier training session with a training dataset represented by a data source.

**Availability**:
- macOS 11.0+

## Declaration

```swift
static func train(trainingData: MLActivityClassifier.DataSource, featureColumns: [String], labelColumn: String, recordingFileColumn: String, parameters: MLActivityClassifier.ModelParameters = ModelParameters(validationData: nil), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLJob<MLActivityClassifier>
```

**Other overloads**:

```swift
static func train(trainingData: MLDataTable, featureColumns: [String], labelColumn: String, recordingFileColumn: String, parameters: MLActivityClassifier.ModelParameters = ModelParameters(validationData: nil), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLJob<MLActivityClassifier>
```

#### Return Value

An [`MLJob`](../mljob.md) that represents the activity classifier training session.

## Parameters

- `trainingData`: An [`MLActivityClassifier.DataSource`](./datasource.md) instance.
- `featureColumns`: The names of the columns in an annotation file that contain sensor data.
- `labelColumn`: The name of the column in an annotation file that contains the activity labels if `trainingData` uses [`MLActivityClassifier.DataSource.directoryWithDataAndAnnotation(at:annotationFileName:timeStampColumn:labelStartTimeColumn:labelEndTimeColumn:)`](./datasource/directorywithdataandannotation%28at,annotationfilename,timestampcolumn,labelstarttimecolumn,labelendtimecolumn%29.md).

  The initializer ignores this parameter if `trainingData` uses [`MLActivityClassifier.DataSource.labeledDirectories(at:)`](./datasource/labeleddirectories%28at%29.md).
- `recordingFileColumn`: The name of the column in an annotation file that contains the data filenames if `trainingData` uses [`MLActivityClassifier.DataSource.directoryWithDataAndAnnotation(at:annotationFileName:timeStampColumn:labelStartTimeColumn:labelEndTimeColumn:)`](./datasource/directorywithdataandannotation%28at,annotationfilename,timestampcolumn,labelstarttimecolumn,labelendtimecolumn%29.md).

  The initializer ignores this parameter if `trainingData` uses [`MLActivityClassifier.DataSource.labeledDirectories(at:)`](./datasource/labeleddirectories%28at%29.md).
- `parameters`: An [`MLActivityClassifier.ModelParameters`](./modelparameters-swift.struct.md) instance you use to configure the model for the training session.
- `sessionParameters`: An [`MLTrainingSessionParameters`](../mltrainingsessionparameters.md) instance you use to configure the training session.

## See Also

### Training an activity classifier asynchronously
- [static makeTrainingSession(trainingData:featureColumns:labelColumn:recordingFileColumn:parameters:sessionParameters:)](./maketrainingsession%28trainingdata,featurecolumns,labelcolumn,recordingfilecolumn,parameters,sessionparameters%29.md)
  Creates an asynchronous training session for an activity classifier.
- [static func resume(MLTrainingSession<MLActivityClassifier>) throws -> MLJob<MLActivityClassifier>](./resume%28_%29.md)
  Begins or continues an asynchronous activity classifier training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLActivityClassifier>](./restoretrainingsession%28sessionparameters%29.md)
  Creates an asynchronous training session for an activity classifier by restoring an existing training session’s state from its parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/train(trainingdata:featurecolumns:labelcolumn:recordingfilecolumn:parameters:sessionparameters:))*