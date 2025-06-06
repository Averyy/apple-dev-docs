# makeTrainingSession(trainingData:parameters:sessionParameters:)

**Framework**: Create ML  
**Kind**: method

Creates an asynchronous hand pose classifier’s training session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
static func makeTrainingSession(trainingData: MLHandPoseClassifier.DataSource, parameters: MLHandPoseClassifier.ModelParameters = .init(), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLTrainingSession<MLHandPoseClassifier>
```

#### Return Value

An [`MLTrainingSession`](mltrainingsession.md) that represents the action classifier training session.

## Parameters

- `trainingData`: An   instance.
- `parameters`: An    instance you use to configure the model for the training session.
- `sessionParameters`: An   instance you use   to configure the training session.

## See Also

- [static func train(trainingData: MLHandPoseClassifier.DataSource, parameters: MLHandPoseClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLHandPoseClassifier>](mlhandposeclassifier/train(trainingdata:parameters:sessionparameters:).md)
  Begins an asynchronous hand pose classifier’s training session.
- [static func resume(MLTrainingSession<MLHandPoseClassifier>) throws -> MLJob<MLHandPoseClassifier>](mlhandposeclassifier/resume(_:).md)
  Begins or continues an asynchronous hand pose classifier’s training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandPoseClassifier>](mlhandposeclassifier/restoretrainingsession(sessionparameters:).md)
  Recreates an asynchronous hand pose classifier’s training session by restoring its saved state from the file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:))*