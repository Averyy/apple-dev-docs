# resume(_:)

**Framework**: Create ML  
**Kind**: method

Begins or continues an asynchronous hand action classifier’s training session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
static func resume(_ session: MLTrainingSession<MLHandActionClassifier>) throws -> MLJob<MLHandActionClassifier>
```

#### Return Value

An [`MLJob`](mljob.md) that represents the hand action training session.

## Parameters

- `session`: An   instance that represents the   training session.

## See Also

- [static func train(trainingData: MLHandActionClassifier.DataSource, parameters: MLHandActionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLHandActionClassifier>](mlhandactionclassifier/train(trainingdata:parameters:sessionparameters:).md)
  Begins an asynchronous hand action classifier’s training session.
- [static func makeTrainingSession(trainingData: MLHandActionClassifier.DataSource, parameters: MLHandActionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandActionClassifier>](mlhandactionclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:).md)
  Creates an asynchronous hand action classifier’s training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandActionClassifier>](mlhandactionclassifier/restoretrainingsession(sessionparameters:).md)
  Recreates an asynchronous hand action classifier’s training session by restoring its saved state from the file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/resume(_:))*