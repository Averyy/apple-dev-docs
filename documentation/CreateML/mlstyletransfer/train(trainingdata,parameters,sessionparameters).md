# train(trainingData:parameters:sessionParameters:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Type Method

Begins an asynchronous style transfer model-training session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static func train(trainingData: MLStyleTransfer.DataSource, parameters: MLStyleTransfer.ModelParameters = .init(), sessionParameters: MLTrainingSessionParameters = .init()) throws -> MLJob<MLStyleTransfer>
```

## Return Value

An [`MLJob`](../mljob.md) that represents the style transfer model-training session.

## Parameters

- `trainingData`: The style image and content images represented by a data source.
- `parameters`: An [`MLStyleTransfer.ModelParameters`](./modelparameters.md) instance you use to configure the model for the training session.
- `sessionParameters`: An [`MLTrainingSessionParameters`](../mltrainingsessionparameters.md) instance you use to configure the training session.

## See Also

### Training a style transfer model asynchronously
- [static func makeTrainingSession(trainingData: MLStyleTransfer.DataSource, parameters: MLStyleTransfer.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLStyleTransfer>](./maketrainingsession%28trainingdata,parameters,sessionparameters%29.md)
  Creates an asynchronous training session for a style transfer model.
- [static func resume(MLTrainingSession<MLStyleTransfer>) throws -> MLJob<MLStyleTransfer>](./resume%28_%29.md)
  Begins or continues an asynchronous style transfer model-training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLStyleTransfer>](./restoretrainingsession%28sessionparameters%29.md)
  Creates an asynchronous training session for a style transfer model by restoring an existing training session’s state from its parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlstyletransfer/train(trainingdata:parameters:sessionparameters:))*