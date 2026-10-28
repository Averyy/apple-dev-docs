# restoreTrainingSession(sessionParameters:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Type Method

Creates an asynchronous training session for an action classifier by restoring an existing training session’s state from its parameters.

**Availability**:
- macOS 11.0+

## Declaration

```swift
static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLActionClassifier>
```

## Return Value

An [`MLTrainingSession`](../mltrainingsession.md) that represents the action classifier training session.

## Parameters

- `sessionParameters`: The [`MLTrainingSessionParameters`](../mltrainingsessionparameters.md) instance you used to create the training session using [`makeTrainingSession(trainingData:parameters:sessionParameters:)`](./maketrainingsession%28trainingdata,parameters,sessionparameters%29.md).

## See Also

### Training an action classifier asynchronously
- [static func train(trainingData: MLActionClassifier.DataSource, parameters: MLActionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLActionClassifier>](./train%28trainingdata,parameters,sessionparameters%29.md)
  Begins an asynchronous action classifier training session.
- [static func makeTrainingSession(trainingData: MLActionClassifier.DataSource, parameters: MLActionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLActionClassifier>](./maketrainingsession%28trainingdata,parameters,sessionparameters%29.md)
  Creates an asynchronous training session for an action classifier.
- [static func resume(MLTrainingSession<MLActionClassifier>) throws -> MLJob<MLActionClassifier>](./resume%28_%29.md)
  Begins or continues an asynchronous action classifier training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/restoretrainingsession(sessionparameters:))*