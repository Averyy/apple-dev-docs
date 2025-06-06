# train(trainingData:parameters:sessionParameters:)

**Framework**: Create ML  
**Kind**: method

Begins an asynchronous hand pose classifier’s training session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
static func train(trainingData: MLHandPoseClassifier.DataSource, parameters: MLHandPoseClassifier.ModelParameters = ModelParameters(), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLJob<MLHandPoseClassifier>
```

#### Return Value

An [`MLJob`](mljob.md) that represents the hand pose classifier’s training session.

## Parameters

- `trainingData`: An   instance.
- `parameters`: An    instance you use to configure the model for the training session.
- `sessionParameters`: An   instance you use   to configure the training session.

## See Also

- [static func makeTrainingSession(trainingData: MLHandPoseClassifier.DataSource, parameters: MLHandPoseClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandPoseClassifier>](mlhandposeclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:).md)
  Creates an asynchronous hand pose classifier’s training session.
- [static func resume(MLTrainingSession<MLHandPoseClassifier>) throws -> MLJob<MLHandPoseClassifier>](mlhandposeclassifier/resume(_:).md)
  Begins or continues an asynchronous hand pose classifier’s training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandPoseClassifier>](mlhandposeclassifier/restoretrainingsession(sessionparameters:).md)
  Recreates an asynchronous hand pose classifier’s training session by restoring its saved state from the file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/train(trainingdata:parameters:sessionparameters:))*