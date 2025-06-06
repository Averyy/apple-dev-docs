# resume(_:)

**Framework**: Create ML  
**Kind**: method

Begins or continues an asynchronous object-detector training session.

**Availability**:
- macOS 11.0+

## Declaration

```swift
static func resume(_ session: MLTrainingSession<MLObjectDetector>) throws -> MLJob<MLObjectDetector>
```

#### Return Value

An [`MLJob`](mljob.md) that represents the object-detector training session.

#### Discussion

Use this method to start or resume a training session you get from [`makeTrainingSession(trainingData:annotationType:parameters:sessionParameters:)`](mlobjectdetector/maketrainingsession(trainingdata:annotationtype:parameters:sessionparameters:).md) or [`restoreTrainingSession(sessionParameters:)`](mlobjectdetector/restoretrainingsession(sessionparameters:).md).

- session: An [`MLTrainingSession`](mltrainingsession.md) instance that represents the training session.

## See Also

- [static func train(trainingData: MLObjectDetector.DataSource, annotationType: MLObjectDetector.AnnotationType, parameters: MLObjectDetector.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLObjectDetector>](mlobjectdetector/train(trainingdata:annotationtype:parameters:sessionparameters:).md)
  Begins an asynchronous object-detector training session.
- [static func makeTrainingSession(trainingData: MLObjectDetector.DataSource, annotationType: MLObjectDetector.AnnotationType, parameters: MLObjectDetector.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLObjectDetector>](mlobjectdetector/maketrainingsession(trainingdata:annotationtype:parameters:sessionparameters:).md)
  Creates an asynchronous object-detector training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLObjectDetector>](mlobjectdetector/restoretrainingsession(sessionparameters:).md)
  Creates an asynchronous training session for an object detector by restoring an existing training session’s state from its parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/resume(_:))*