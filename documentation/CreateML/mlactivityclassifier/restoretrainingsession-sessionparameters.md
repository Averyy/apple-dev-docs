# restoreTrainingSession(sessionParameters:)

**Framework**: Create ML  
**Kind**: method

Creates an asynchronous training session for an activity classifier by restoring an existing training session’s state from its parameters.

**Availability**:
- macOS 11.0+

## Declaration

```swift
static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLActivityClassifier>
```

#### Return Value

An [`MLTrainingSession`](mltrainingsession.md) that represents the activity classifier training session.

## Parameters

- `sessionParameters`: The   instance you used to create the training session   using   .

## See Also

- [static train(trainingData:featureColumns:labelColumn:recordingFileColumn:parameters:sessionParameters:)](mlactivityclassifier/train(trainingdata:featurecolumns:labelcolumn:recordingfilecolumn:parameters:sessionparameters:).md)
  Begins an asynchronous activity classifier training session with a training dataset represented by a data source.
- [static makeTrainingSession(trainingData:featureColumns:labelColumn:recordingFileColumn:parameters:sessionParameters:)](mlactivityclassifier/maketrainingsession(trainingdata:featurecolumns:labelcolumn:recordingfilecolumn:parameters:sessionparameters:).md)
  Creates an asynchronous training session for an activity classifier.
- [static func resume(MLTrainingSession<MLActivityClassifier>) throws -> MLJob<MLActivityClassifier>](mlactivityclassifier/resume(_:).md)
  Begins or continues an asynchronous activity classifier training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/restoretrainingsession(sessionparameters:))*