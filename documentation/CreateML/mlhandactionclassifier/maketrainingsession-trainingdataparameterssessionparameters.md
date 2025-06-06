# makeTrainingSession(trainingData:parameters:sessionParameters:)

**Framework**: Create ML  
**Kind**: method

Creates an asynchronous hand action classifier’s training session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
static func makeTrainingSession(trainingData: MLHandActionClassifier.DataSource, parameters: MLHandActionClassifier.ModelParameters = .init(), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLTrainingSession<MLHandActionClassifier>
```

#### Return Value

An [`MLTrainingSession`](mltrainingsession.md) that represents the action classifier training session.

#### Discussion

- sessionParameters: An [`MLTrainingSessionParameters`](mltrainingsessionparameters.md) instance you use to configure the training session.

## Parameters

- `trainingData`: An   instance.

## See Also

- [static func train(trainingData: MLHandActionClassifier.DataSource, parameters: MLHandActionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLHandActionClassifier>](mlhandactionclassifier/train(trainingdata:parameters:sessionparameters:).md)
  Begins an asynchronous hand action classifier’s training session.
- [static func resume(MLTrainingSession<MLHandActionClassifier>) throws -> MLJob<MLHandActionClassifier>](mlhandactionclassifier/resume(_:).md)
  Begins or continues an asynchronous hand action classifier’s training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandActionClassifier>](mlhandactionclassifier/restoretrainingsession(sessionparameters:).md)
  Recreates an asynchronous hand action classifier’s training session by restoring its saved state from the file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:))*