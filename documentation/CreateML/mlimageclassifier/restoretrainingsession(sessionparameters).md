# restoreTrainingSession(sessionParameters:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Type Method

Creates an asynchronous training session for an image classifier by restoring an existing training session’s state from its parameters.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLImageClassifier>
```

## Return Value

An [`MLTrainingSession`](../mltrainingsession.md) that represents the image classifier training session.

## Parameters

- `sessionParameters`: Training session parameters. See `MLTrainingSessionParameters` for the defaults.

## See Also

### Training an image classifier asynchronously
- [static func makeTrainingSession(trainingData: MLImageClassifier.DataSource, parameters: MLImageClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLImageClassifier>](./maketrainingsession%28trainingdata,parameters,sessionparameters%29.md)
  Creates or restores a training session.
- [static func train(trainingData: MLImageClassifier.DataSource, parameters: MLImageClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLImageClassifier>](./train%28trainingdata,parameters,sessionparameters%29.md)
  Begins an asynchronous image classifier training session with a training dataset represented by a data source.
- [static func resume(MLTrainingSession<MLImageClassifier>) throws -> MLJob<MLImageClassifier>](./resume%28_%29.md)
  Begins or continues an asynchronous image classifier training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/restoretrainingsession(sessionparameters:))*