# resume(_:)

**Framework**: Create ML  
**Kind**: method

Begins or continues an asynchronous image classifier training session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static func resume(_ session: MLTrainingSession<MLImageClassifier>) throws -> MLJob<MLImageClassifier>
```

#### Return Value

An [`MLJob`](mljob.md) that represents the image classifier training session.

## Parameters

- `session`: An   instance that represents the training session.

## See Also

- [static func makeTrainingSession(trainingData: MLImageClassifier.DataSource, parameters: MLImageClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLImageClassifier>](mlimageclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:).md)
  Creates or restores a training session.
- [static func train(trainingData: MLImageClassifier.DataSource, parameters: MLImageClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLImageClassifier>](mlimageclassifier/train(trainingdata:parameters:sessionparameters:).md)
  Begins an asynchronous image classifier training session with a training dataset represented by a data source.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLImageClassifier>](mlimageclassifier/restoretrainingsession(sessionparameters:).md)
  Creates an asynchronous training session for an image classifier by restoring an existing training session’s state from its parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/resume(_:))*