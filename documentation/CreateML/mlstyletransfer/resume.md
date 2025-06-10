# resume(_:)

**Framework**: Create ML  
**Kind**: method

Begins or continues an asynchronous style transfer model-training session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static func resume(_ session: MLTrainingSession<MLStyleTransfer>) throws -> MLJob<MLStyleTransfer>
```

#### Return Value

An [`MLJob`](mljob.md) that represents the style transfer model-training session.

## Parameters

- `session`: An   instance that represents the training session.

## See Also

- [static func train(trainingData: MLStyleTransfer.DataSource, parameters: MLStyleTransfer.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLStyleTransfer>](mlstyletransfer/train(trainingdata:parameters:sessionparameters:).md)
  Begins an asynchronous style transfer model-training session.
- [static func makeTrainingSession(trainingData: MLStyleTransfer.DataSource, parameters: MLStyleTransfer.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLStyleTransfer>](mlstyletransfer/maketrainingsession(trainingdata:parameters:sessionparameters:).md)
  Creates an asynchronous training session for a style transfer model.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLStyleTransfer>](mlstyletransfer/restoretrainingsession(sessionparameters:).md)
  Creates an asynchronous training session for a style transfer model by restoring an existing training session’s state from its parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlstyletransfer/resume(_:))*