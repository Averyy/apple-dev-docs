# resume(_:)

**Framework**: Create ML  
**Kind**: method

Begins or continues an asynchronous action classifier training session.

**Availability**:
- macOS 11.0+

## Declaration

```swift
static func resume(_ session: MLTrainingSession<MLActionClassifier>) throws -> MLJob<MLActionClassifier>
```

#### Return Value

An [`MLJob`](mljob.md) that represents the action classifier training session.

#### Discussion

- session: An [`MLTrainingSession`](mltrainingsession.md) instance that represents the training session.

## See Also

- [static func train(trainingData: MLActionClassifier.DataSource, parameters: MLActionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLActionClassifier>](mlactionclassifier/train(trainingdata:parameters:sessionparameters:).md)
  Begins an asynchronous action classifier training session.
- [static func makeTrainingSession(trainingData: MLActionClassifier.DataSource, parameters: MLActionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLActionClassifier>](mlactionclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:).md)
  Creates an asynchronous training session for an action classifier.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLActionClassifier>](mlactionclassifier/restoretrainingsession(sessionparameters:).md)
  Creates an asynchronous training session for an action classifier by restoring an existing training session’s state from its parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/resume(_:))*