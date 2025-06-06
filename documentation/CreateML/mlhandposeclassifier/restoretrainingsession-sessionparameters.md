# restoreTrainingSession(sessionParameters:)

**Framework**: Create ML  
**Kind**: method

Recreates an asynchronous hand pose classifier’s training session by restoring its saved state from the file system.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandPoseClassifier>
```

#### Return Value

An [`MLTrainingSession`](mltrainingsession.md) that represents the hand pose classifier training session.

## Parameters

- `sessionParameters`: The same   instance   that created an existing training session.

## See Also

- [static func train(trainingData: MLHandPoseClassifier.DataSource, parameters: MLHandPoseClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLHandPoseClassifier>](mlhandposeclassifier/train(trainingdata:parameters:sessionparameters:).md)
  Begins an asynchronous hand pose classifier’s training session.
- [static func makeTrainingSession(trainingData: MLHandPoseClassifier.DataSource, parameters: MLHandPoseClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandPoseClassifier>](mlhandposeclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:).md)
  Creates an asynchronous hand pose classifier’s training session.
- [static func resume(MLTrainingSession<MLHandPoseClassifier>) throws -> MLJob<MLHandPoseClassifier>](mlhandposeclassifier/resume(_:).md)
  Begins or continues an asynchronous hand pose classifier’s training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/restoretrainingsession(sessionparameters:))*