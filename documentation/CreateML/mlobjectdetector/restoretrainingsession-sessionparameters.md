# restoreTrainingSession(sessionParameters:)

**Framework**: Create ML  
**Kind**: method

Creates an asynchronous training session for an object detector by restoring an existing training session’s state from its parameters.

**Availability**:
- macOS 11.0+

## Declaration

```swift
static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLObjectDetector>
```

#### Return Value

An [`MLTrainingSession`](mltrainingsession.md) that represents the object-detector training session.

#### Discussion

Use [`resume(_:)`](mlobjectdetector/resume(_:).md) to start the [`MLTrainingSession`](mltrainingsession.md) instance you get from this method.

## Parameters

- `sessionParameters`: The   instance you used to create the training session   with  .

## See Also

- [static func train(trainingData: MLObjectDetector.DataSource, annotationType: MLObjectDetector.AnnotationType, parameters: MLObjectDetector.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLObjectDetector>](mlobjectdetector/train(trainingdata:annotationtype:parameters:sessionparameters:).md)
  Begins an asynchronous object-detector training session.
- [static func makeTrainingSession(trainingData: MLObjectDetector.DataSource, annotationType: MLObjectDetector.AnnotationType, parameters: MLObjectDetector.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLObjectDetector>](mlobjectdetector/maketrainingsession(trainingdata:annotationtype:parameters:sessionparameters:).md)
  Creates an asynchronous object-detector training session.
- [static func resume(MLTrainingSession<MLObjectDetector>) throws -> MLJob<MLObjectDetector>](mlobjectdetector/resume(_:).md)
  Begins or continues an asynchronous object-detector training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/restoretrainingsession(sessionparameters:))*