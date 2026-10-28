# restoreTrainingSession(sessionParameters:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Type Method

Creates an asynchronous training session for a style transfer model by restoring an existing training session’s state from its parameters.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLStyleTransfer>
```

## Return Value

An [`MLTrainingSession`](../mltrainingsession.md) that represents the style transfer model-training session.

## Parameters

- `sessionParameters`: The [`MLTrainingSessionParameters`](../mltrainingsessionparameters.md) instance you used to create the training session using [`makeTrainingSession(trainingData:parameters:sessionParameters:)`](./maketrainingsession%28trainingdata,parameters,sessionparameters%29.md).

## See Also

### Training a style transfer model asynchronously
- [static func train(trainingData: MLStyleTransfer.DataSource, parameters: MLStyleTransfer.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLStyleTransfer>](./train%28trainingdata,parameters,sessionparameters%29.md)
  Begins an asynchronous style transfer model-training session.
- [static func makeTrainingSession(trainingData: MLStyleTransfer.DataSource, parameters: MLStyleTransfer.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLStyleTransfer>](./maketrainingsession%28trainingdata,parameters,sessionparameters%29.md)
  Creates an asynchronous training session for a style transfer model.
- [static func resume(MLTrainingSession<MLStyleTransfer>) throws -> MLJob<MLStyleTransfer>](./resume%28_%29.md)
  Begins or continues an asynchronous style transfer model-training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlstyletransfer/restoretrainingsession(sessionparameters:))*