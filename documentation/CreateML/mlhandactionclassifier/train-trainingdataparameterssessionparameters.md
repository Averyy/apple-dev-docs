# train(trainingData:parameters:sessionParameters:)

**Framework**: Create ML  
**Kind**: method

Begins an asynchronous hand action classifier’s training session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
static func train(trainingData: MLHandActionClassifier.DataSource, parameters: MLHandActionClassifier.ModelParameters = ModelParameters(), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLJob<MLHandActionClassifier>
```

#### Return Value

An [`MLJob`](mljob.md) that represents the hand action classifier’s training session.

## Parameters

- `trainingData`: An   instance.
- `parameters`: An    instance you use to configure the model for the training session.
- `sessionParameters`: An   instance you use   to configure the training session.

## See Also

- [static func makeTrainingSession(trainingData: MLHandActionClassifier.DataSource, parameters: MLHandActionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandActionClassifier>](mlhandactionclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:).md)
  Creates an asynchronous hand action classifier’s training session.
- [static func resume(MLTrainingSession<MLHandActionClassifier>) throws -> MLJob<MLHandActionClassifier>](mlhandactionclassifier/resume(_:).md)
  Begins or continues an asynchronous hand action classifier’s training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandActionClassifier>](mlhandactionclassifier/restoretrainingsession(sessionparameters:).md)
  Recreates an asynchronous hand action classifier’s training session by restoring its saved state from the file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/train(trainingdata:parameters:sessionparameters:))*