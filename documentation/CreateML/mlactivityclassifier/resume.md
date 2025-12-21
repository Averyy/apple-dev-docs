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

- [static train(trainingData:featureColumns:labelColumn:recordingFileColumn:parameters:sessionParameters:)](mlactivityclassifier/train(trainingdata:featurecolumns:labelcolumn:recordingfilecolumn:parameters:sessionparameters:).md)
  Begins an asynchronous activity classifier training session with a training dataset represented by a data source.
- [static makeTrainingSession(trainingData:featureColumns:labelColumn:recordingFileColumn:parameters:sessionParameters:)](mlactivityclassifier/maketrainingsession(trainingdata:featurecolumns:labelcolumn:recordingfilecolumn:parameters:sessionparameters:).md)
  Creates an asynchronous training session for an activity classifier.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLActivityClassifier>](mlactivityclassifier/restoretrainingsession(sessionparameters:).md)
  Creates an asynchronous training session for an activity classifier by restoring an existing training session’s state from its parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/resume(_:))*