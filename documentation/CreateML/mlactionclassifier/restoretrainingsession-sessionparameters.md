# restoreTrainingSession(sessionParameters:)

**Framework**: Create ML  
**Kind**: method

Creates an asynchronous training session for an action classifier by restoring an existing training session’s state from its parameters.

**Availability**:
- macOS 11.0+

## Declaration

```swift
static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLActionClassifier>
```

#### Return Value

An [`MLTrainingSession`](mltrainingsession.md) that represents the action classifier training session.

#### Discussion

- sessionParameters: The [`MLTrainingSessionParameters`](mltrainingsessionparameters.md) instance you used to create the training session using [`makeTrainingSession(trainingData:parameters:sessionParameters:)`](mlactionclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:).md).

## See Also

- [static func train(trainingData: MLActionClassifier.DataSource, parameters: MLActionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLActionClassifier>](mlactionclassifier/train(trainingdata:parameters:sessionparameters:).md)
  Begins an asynchronous action classifier training session.
- [static func makeTrainingSession(trainingData: MLActionClassifier.DataSource, parameters: MLActionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLActionClassifier>](mlactionclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:).md)
  Creates an asynchronous training session for an action classifier.
- [static func resume(MLTrainingSession<MLActionClassifier>) throws -> MLJob<MLActionClassifier>](mlactionclassifier/resume(_:).md)
  Begins or continues an asynchronous action classifier training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/restoretrainingsession(sessionparameters:))*