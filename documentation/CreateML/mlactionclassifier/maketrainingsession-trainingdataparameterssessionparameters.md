# makeTrainingSession(trainingData:parameters:sessionParameters:)

**Framework**: Create ML  
**Kind**: method

Creates an asynchronous training session for an action classifier.

**Availability**:
- macOS 11.0+

## Declaration

```swift
static func makeTrainingSession(trainingData: MLActionClassifier.DataSource, parameters: MLActionClassifier.ModelParameters = .init(), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLTrainingSession<MLActionClassifier>
```

#### Return Value

An [`MLTrainingSession`](mltrainingsession.md) that represents the action classifier training session.

#### Discussion

- trainingData: A collection of labeled videos represented by a data source.
- sessionParameters: An [`MLTrainingSessionParameters`](mltrainingsessionparameters.md) instance you use to configure the training session.

## See Also

- [static func train(trainingData: MLActionClassifier.DataSource, parameters: MLActionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLActionClassifier>](mlactionclassifier/train(trainingdata:parameters:sessionparameters:).md)
  Begins an asynchronous action classifier training session.
- [static func resume(MLTrainingSession<MLActionClassifier>) throws -> MLJob<MLActionClassifier>](mlactionclassifier/resume(_:).md)
  Begins or continues an asynchronous action classifier training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLActionClassifier>](mlactionclassifier/restoretrainingsession(sessionparameters:).md)
  Creates an asynchronous training session for an action classifier by restoring an existing training session’s state from its parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:))*