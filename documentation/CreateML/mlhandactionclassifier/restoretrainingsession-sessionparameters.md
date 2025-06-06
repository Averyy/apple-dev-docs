# restoreTrainingSession(sessionParameters:)

**Framework**: Create ML  
**Kind**: method

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

An [`MLTrainingSession`](mltrainingsession.md) that represents the hand action classifier training session.

#### Discussion

- sessionParameters: The same [`MLTrainingSessionParameters`](mltrainingsessionparameters.md) instance that created an existing training session.

## See Also

- [static func train(trainingData: MLHandActionClassifier.DataSource, parameters: MLHandActionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLHandActionClassifier>](mlhandactionclassifier/train(trainingdata:parameters:sessionparameters:).md)
  Begins an asynchronous hand action classifier’s training session.
- [static func makeTrainingSession(trainingData: MLHandActionClassifier.DataSource, parameters: MLHandActionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandActionClassifier>](mlhandactionclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:).md)
  Creates an asynchronous hand action classifier’s training session.
- [static func resume(MLTrainingSession<MLHandActionClassifier>) throws -> MLJob<MLHandActionClassifier>](mlhandactionclassifier/resume(_:).md)
  Begins or continues an asynchronous hand action classifier’s training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/restoretrainingsession(sessionparameters:))*