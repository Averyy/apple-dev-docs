# train(trainingData:annotationType:parameters:sessionParameters:)

**Framework**: Create ML  
**Kind**: method

Begins an asynchronous object-detector training session.

**Availability**:
- macOS 11.0+

## Declaration

```swift
static func train(trainingData: MLObjectDetector.DataSource, annotationType: MLObjectDetector.AnnotationType, parameters: MLObjectDetector.ModelParameters = ModelParameters(), sessionParameters: MLTrainingSessionParameters = __Defaults.sessionParameters) throws -> MLJob<MLObjectDetector>
```

#### Return Value

An [`MLJob`](mljob.md) that represents the object-detector training session.

#### Discussion

- trainingData: The annotated images the task uses to train the object detector.
- annotationType: The format your data source uses for its image annotations.
- sessionParameters: An [`MLTrainingSessionParameters`](mltrainingsessionparameters.md) instance you use to configure the training session.

## See Also

- [static func makeTrainingSession(trainingData: MLObjectDetector.DataSource, annotationType: MLObjectDetector.AnnotationType, parameters: MLObjectDetector.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLObjectDetector>](mlobjectdetector/maketrainingsession(trainingdata:annotationtype:parameters:sessionparameters:).md)
  Creates an asynchronous object-detector training session.
- [static func resume(MLTrainingSession<MLObjectDetector>) throws -> MLJob<MLObjectDetector>](mlobjectdetector/resume(_:).md)
  Begins or continues an asynchronous object-detector training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLObjectDetector>](mlobjectdetector/restoretrainingsession(sessionparameters:).md)
  Creates an asynchronous training session for an object detector by restoring an existing training session’s state from its parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/train(trainingdata:annotationtype:parameters:sessionparameters:))*