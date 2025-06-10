# makeTrainingSession(trainingData:parameters:sessionParameters:)

**Framework**: Create ML  
**Kind**: method

Creates an asynchronous training session for a style transfer model.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static func makeTrainingSession(trainingData: MLStyleTransfer.DataSource, parameters: MLStyleTransfer.ModelParameters = .init(), sessionParameters: MLTrainingSessionParameters = .init()) throws -> MLTrainingSession<MLStyleTransfer>
```

#### Return Value

An [`MLTrainingSession`](mltrainingsession.md) that represents the style transfer model-training session.

## Parameters

- `trainingData`: The style image and content images represented by a data source.
- `parameters`: An   instance you use to configure the model for the training   session.
- `sessionParameters`: An   instance you use to configure the training session.

## See Also

- [static func train(trainingData: MLStyleTransfer.DataSource, parameters: MLStyleTransfer.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLStyleTransfer>](mlstyletransfer/train(trainingdata:parameters:sessionparameters:).md)
  Begins an asynchronous style transfer model-training session.
- [static func resume(MLTrainingSession<MLStyleTransfer>) throws -> MLJob<MLStyleTransfer>](mlstyletransfer/resume(_:).md)
  Begins or continues an asynchronous style transfer model-training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLStyleTransfer>](mlstyletransfer/restoretrainingsession(sessionparameters:).md)
  Creates an asynchronous training session for a style transfer model by restoring an existing training session’s state from its parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlstyletransfer/maketrainingsession(trainingdata:parameters:sessionparameters:))*