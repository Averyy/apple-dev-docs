# train(trainingData:parameters:sessionParameters:)

**Framework**: Create ML  
**Kind**: method

Begins an asynchronous action classifier training session.

**Availability**:
- macOS 11.0+

## Declaration

```swift
static func train(trainingData: MLActionClassifier.DataSource, parameters: MLActionClassifier.ModelParameters = ModelParameters(), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLJob<MLActionClassifier>
```

#### Return Value

An [`MLJob`](mljob.md) that represents the action classifier training session.

#### Discussion

- trainingData: A collection of labeled videos represented by a data source.
- sessionParameters: An [`MLTrainingSessionParameters`](mltrainingsessionparameters.md) instance you use to configure the training session.

## See Also

- [static func makeTrainingSession(trainingData: MLActionClassifier.DataSource, parameters: MLActionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLActionClassifier>](mlactionclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:).md)
  Creates an asynchronous training session for an action classifier.
- [static func resume(MLTrainingSession<MLActionClassifier>) throws -> MLJob<MLActionClassifier>](mlactionclassifier/resume(_:).md)
  Begins or continues an asynchronous action classifier training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLActionClassifier>](mlactionclassifier/restoretrainingsession(sessionparameters:).md)
  Creates an asynchronous training session for an action classifier by restoring an existing training session’s state from its parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/train(trainingdata:parameters:sessionparameters:))*