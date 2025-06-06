# resume(_:)

**Framework**: Create ML  
**Kind**: method

Begins or continues an asynchronous hand pose classifier’s training session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
static func resume(_ session: MLTrainingSession<MLHandPoseClassifier>) throws -> MLJob<MLHandPoseClassifier>
```

#### Return Value

An [`MLJob`](mljob.md) that represents the hand pose training session.

## Parameters

- `session`: An   instance that represents the   training session.

## See Also

- [static func train(trainingData: MLHandPoseClassifier.DataSource, parameters: MLHandPoseClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLHandPoseClassifier>](mlhandposeclassifier/train(trainingdata:parameters:sessionparameters:).md)
  Begins an asynchronous hand pose classifier’s training session.
- [static func makeTrainingSession(trainingData: MLHandPoseClassifier.DataSource, parameters: MLHandPoseClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandPoseClassifier>](mlhandposeclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:).md)
  Creates an asynchronous hand pose classifier’s training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandPoseClassifier>](mlhandposeclassifier/restoretrainingsession(sessionparameters:).md)
  Recreates an asynchronous hand pose classifier’s training session by restoring its saved state from the file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/resume(_:))*