# restoreTrainingSession(sessionParameters:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Type Method

Creates an asynchronous training session for an object detector by restoring an existing training session’s state from its parameters.

**Availability**:
- macOS 11.0+

## Declaration

```swift
static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLObjectDetector>
```

## Return Value

An [`MLTrainingSession`](../mltrainingsession.md) that represents the object-detector training session.

## Discussion

Use [`resume(_:)`](./resume%28_%29.md) to start the [`MLTrainingSession`](../mltrainingsession.md) instance you get from this method.

## Parameters

- `sessionParameters`: The [`MLTrainingSessionParameters`](../mltrainingsessionparameters.md) instance you used to create the training session with [`makeTrainingSession(trainingData:annotationType:parameters:sessionParameters:)`](./maketrainingsession%28trainingdata,annotationtype,parameters,sessionparameters%29.md).

## See Also

### Training an object detector asynchronously
- [static func train(trainingData: MLObjectDetector.DataSource, annotationType: MLObjectDetector.AnnotationType, parameters: MLObjectDetector.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLObjectDetector>](./train%28trainingdata,annotationtype,parameters,sessionparameters%29.md)
  Begins an asynchronous object-detector training session.
- [static func makeTrainingSession(trainingData: MLObjectDetector.DataSource, annotationType: MLObjectDetector.AnnotationType, parameters: MLObjectDetector.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLObjectDetector>](./maketrainingsession%28trainingdata,annotationtype,parameters,sessionparameters%29.md)
  Creates an asynchronous object-detector training session.
- [static func resume(MLTrainingSession<MLObjectDetector>) throws -> MLJob<MLObjectDetector>](./resume%28_%29.md)
  Begins or continues an asynchronous object-detector training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/restoretrainingsession(sessionparameters:))*