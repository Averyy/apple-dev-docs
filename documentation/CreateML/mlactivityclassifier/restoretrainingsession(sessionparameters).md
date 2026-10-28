# restoreTrainingSession(sessionParameters:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Type Method

Creates an asynchronous training session for an activity classifier by restoring an existing training session’s state from its parameters.

**Availability**:
- macOS 11.0+

## Declaration

```swift
static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLActivityClassifier>
```

## Return Value

An [`MLTrainingSession`](../mltrainingsession.md) that represents the activity classifier training session.

## Parameters

- `sessionParameters`: The [`MLTrainingSessionParameters`](../mltrainingsessionparameters.md) instance you used to create the training session with `MLActivityClassifier/makeTrainingSession(trainingData:featureColumns:labelColumn:recordingFileColumn:parameters:sessionParameters:)-(DataSource,_,_,_,_,_)` or [`makeTrainingSession(trainingData:featureColumns:labelColumn:recordingFileColumn:parameters:sessionParameters:)`](./maketrainingsession%28trainingdata,featurecolumns,labelcolumn,recordingfilecolumn,parameters,sessionparameters%29-3ic8k.md).

## See Also

### Training an activity classifier asynchronously
- [static train(trainingData:featureColumns:labelColumn:recordingFileColumn:parameters:sessionParameters:)](./train%28trainingdata,featurecolumns,labelcolumn,recordingfilecolumn,parameters,sessionparameters%29.md)
  Begins an asynchronous activity classifier training session with a training dataset represented by a data source.
- [static makeTrainingSession(trainingData:featureColumns:labelColumn:recordingFileColumn:parameters:sessionParameters:)](./maketrainingsession%28trainingdata,featurecolumns,labelcolumn,recordingfilecolumn,parameters,sessionparameters%29.md)
  Creates an asynchronous training session for an activity classifier.
- [static func resume(MLTrainingSession<MLActivityClassifier>) throws -> MLJob<MLActivityClassifier>](./resume%28_%29.md)
  Begins or continues an asynchronous activity classifier training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/restoretrainingsession(sessionparameters:))*