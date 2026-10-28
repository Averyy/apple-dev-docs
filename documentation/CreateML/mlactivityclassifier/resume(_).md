# resume(_:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Type Method

Begins or continues an asynchronous activity classifier training session.

**Availability**:
- macOS 11.0+

## Declaration

```swift
static func resume(_ session: MLTrainingSession<MLActivityClassifier>) throws -> MLJob<MLActivityClassifier>
```

## Return Value

An [`MLJob`](../mljob.md) that represents the activity classifier training session.

## Parameters

- `session`: An [`MLTrainingSession`](../mltrainingsession.md) instance that represents the training session.

## See Also

### Training an activity classifier asynchronously
- [static train(trainingData:featureColumns:labelColumn:recordingFileColumn:parameters:sessionParameters:)](./train%28trainingdata,featurecolumns,labelcolumn,recordingfilecolumn,parameters,sessionparameters%29.md)
  Begins an asynchronous activity classifier training session with a training dataset represented by a data source.
- [static makeTrainingSession(trainingData:featureColumns:labelColumn:recordingFileColumn:parameters:sessionParameters:)](./maketrainingsession%28trainingdata,featurecolumns,labelcolumn,recordingfilecolumn,parameters,sessionparameters%29.md)
  Creates an asynchronous training session for an activity classifier.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLActivityClassifier>](./restoretrainingsession%28sessionparameters%29.md)
  Creates an asynchronous training session for an activity classifier by restoring an existing training session’s state from its parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/resume(_:))*