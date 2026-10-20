# train(trainingData:annotationType:parameters:sessionParameters:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Type Method

Begins an asynchronous object-detector training session.

**Availability**:
- macOS 11.0+

## Declaration

```swift
static func train(trainingData: MLObjectDetector.DataSource, annotationType: MLObjectDetector.AnnotationType, parameters: MLObjectDetector.ModelParameters = ModelParameters(), sessionParameters: MLTrainingSessionParameters = __Defaults.sessionParameters) throws -> MLJob<MLObjectDetector>
```

#### Return Value

An [`MLJob`](../mljob.md) that represents the object-detector training session.

## Parameters

- `trainingData`: The annotated images the task uses to train the object detector.
- `annotationType`: The format your data source uses for its image annotations.
- `parameters`: An [`MLObjectDetector.ModelParameters`](./modelparameters-swift.struct.md) instance you use to set the model configuration settings for the training session.
- `sessionParameters`: An [`MLTrainingSessionParameters`](../mltrainingsessionparameters.md) instance you use to configure the training session.

## See Also

### Training an object detector asynchronously
- [static func makeTrainingSession(trainingData: MLObjectDetector.DataSource, annotationType: MLObjectDetector.AnnotationType, parameters: MLObjectDetector.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLObjectDetector>](./maketrainingsession%28trainingdata,annotationtype,parameters,sessionparameters%29.md)
  Creates an asynchronous object-detector training session.
- [static func resume(MLTrainingSession<MLObjectDetector>) throws -> MLJob<MLObjectDetector>](./resume%28_%29.md)
  Begins or continues an asynchronous object-detector training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLObjectDetector>](./restoretrainingsession%28sessionparameters%29.md)
  Creates an asynchronous training session for an object detector by restoring an existing training session’s state from its parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/train(trainingdata:annotationtype:parameters:sessionparameters:))*