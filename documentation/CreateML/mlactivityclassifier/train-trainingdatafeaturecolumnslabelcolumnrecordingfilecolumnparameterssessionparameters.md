# train(trainingData:featureColumns:labelColumn:recordingFileColumn:parameters:sessionParameters:)

**Framework**: Create ML  
**Kind**: method

Begins an asynchronous activity classifier training session with a training dataset represented by a data source.

**Availability**:
- macOS 11.0+

## Declaration

```swift
static func train(trainingData: MLActivityClassifier.DataSource, featureColumns: [String], labelColumn: String, recordingFileColumn: String, parameters: MLActivityClassifier.ModelParameters = ModelParameters(validationData: nil), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLJob<MLActivityClassifier>
```

#### Return Value

An [`MLJob`](mljob.md) that represents the activity classifier training session.

## Parameters

- `trainingData`: An [`MLActivityClassifier.DataSource`](mlactivityclassifier/datasource.md) instance.
- `featureColumns`: The names of the columns in an annotation file that contain sensor data.
- `labelColumn`: The name of the column in an annotation file that contains the activity labels if `trainingData` uses [`MLActivityClassifier.DataSource.directoryWithDataAndAnnotation(at:annotationFileName:timeStampColumn:labelStartTimeColumn:labelEndTimeColumn:)`](mlactivityclassifier/datasource/directorywithdataandannotation(at:annotationfilename:timestampcolumn:labelstarttimecolumn:labelendtimecolumn:).md). The initializer ignores this parameter if `trainingData` uses [`MLActivityClassifier.DataSource.labeledDirectories(at:)`](mlactivityclassifier/datasource/labeleddirectories(at:).md).
- `recordingFileColumn`: The name of the column in an annotation file that contains the data filenames if `trainingData` uses [`MLActivityClassifier.DataSource.directoryWithDataAndAnnotation(at:annotationFileName:timeStampColumn:labelStartTimeColumn:labelEndTimeColumn:)`](mlactivityclassifier/datasource/directorywithdataandannotation(at:annotationfilename:timestampcolumn:labelstarttimecolumn:labelendtimecolumn:).md). The initializer ignores this parameter if `trainingData` uses [`MLActivityClassifier.DataSource.labeledDirectories(at:)`](mlactivityclassifier/datasource/labeleddirectories(at:).md).
- `parameters`: An [`MLActivityClassifier.ModelParameters`](mlactivityclassifier/modelparameters-swift.struct.md) instance you use to configure the model for the training session.
- `sessionParameters`: An [`MLTrainingSessionParameters`](mltrainingsessionparameters.md) instance you use to configure the training session.

## See Also

- [static makeTrainingSession(trainingData:featureColumns:labelColumn:recordingFileColumn:parameters:sessionParameters:)](mlactivityclassifier/maketrainingsession(trainingdata:featurecolumns:labelcolumn:recordingfilecolumn:parameters:sessionparameters:).md)
  Creates an asynchronous training session for an activity classifier.
- [static func resume(MLTrainingSession<MLActivityClassifier>) throws -> MLJob<MLActivityClassifier>](mlactivityclassifier/resume(_:).md)
  Begins or continues an asynchronous activity classifier training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLActivityClassifier>](mlactivityclassifier/restoretrainingsession(sessionparameters:).md)
  Creates an asynchronous training session for an activity classifier by restoring an existing training session’s state from its parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/train(trainingdata:featurecolumns:labelcolumn:recordingfilecolumn:parameters:sessionparameters:))*