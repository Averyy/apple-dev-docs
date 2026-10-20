# restoreTrainingSession(sessionParameters:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Type Method

Recreates an asynchronous hand action classifier’s training session by restoring its saved state from the file system.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandActionClassifier>
```

#### Return Value

An [`MLTrainingSession`](../mltrainingsession.md) that represents the hand action classifier training session.

## Parameters

- `sessionParameters`: The same [`MLTrainingSessionParameters`](../mltrainingsessionparameters.md) instance that created an existing training session.

## See Also

### Training a hand action classifier asynchronously
- [static func train(trainingData: MLHandActionClassifier.DataSource, parameters: MLHandActionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLHandActionClassifier>](./train%28trainingdata,parameters,sessionparameters%29.md)
  Begins an asynchronous hand action classifier’s training session.
- [static func makeTrainingSession(trainingData: MLHandActionClassifier.DataSource, parameters: MLHandActionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandActionClassifier>](./maketrainingsession%28trainingdata,parameters,sessionparameters%29.md)
  Creates an asynchronous hand action classifier’s training session.
- [static func resume(MLTrainingSession<MLHandActionClassifier>) throws -> MLJob<MLHandActionClassifier>](./resume%28_%29.md)
  Begins or continues an asynchronous hand action classifier’s training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/restoretrainingsession(sessionparameters:))*