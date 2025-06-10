# makeTrainingSession(trainingData:annotationType:parameters:sessionParameters:)

**Framework**: Create ML  
**Kind**: method

Creates an asynchronous object-detector training session.

**Availability**:
- macOS 11.0+

## Declaration

```swift
static func makeTrainingSession(trainingData: MLObjectDetector.DataSource, annotationType: MLObjectDetector.AnnotationType, parameters: MLObjectDetector.ModelParameters = ModelParameters(), sessionParameters: MLTrainingSessionParameters = __Defaults.sessionParameters) throws -> MLTrainingSession<MLObjectDetector>
```

#### Return Value

An [`MLTrainingSession`](mltrainingsession.md) that represents the object-detector training session.

#### Discussion

Use [`resume(_:)`](mlobjectdetector/resume(_:).md) to start the [`MLTrainingSession`](mltrainingsession.md) instance you get from this method.

## Parameters

- `trainingData`: The annotated images the task uses to train the object detector.
- `annotationType`: The format type of the image annotations in the data source.
- `parameters`: An   instance you use to set the model   configuration settings for the training session.
- `sessionParameters`: An   instance you use to configure the training session.

## See Also

- [static func train(trainingData: MLObjectDetector.DataSource, annotationType: MLObjectDetector.AnnotationType, parameters: MLObjectDetector.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLObjectDetector>](mlobjectdetector/train(trainingdata:annotationtype:parameters:sessionparameters:).md)
  Begins an asynchronous object-detector training session.
- [static func resume(MLTrainingSession<MLObjectDetector>) throws -> MLJob<MLObjectDetector>](mlobjectdetector/resume(_:).md)
  Begins or continues an asynchronous object-detector training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLObjectDetector>](mlobjectdetector/restoretrainingsession(sessionparameters:).md)
  Creates an asynchronous training session for an object detector by restoring an existing training session’s state from its parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/maketrainingsession(trainingdata:annotationtype:parameters:sessionparameters:))*