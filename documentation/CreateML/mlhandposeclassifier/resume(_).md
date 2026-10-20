# resume(_:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Type Method

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

An [`MLJob`](../mljob.md) that represents the hand pose training session.

## Parameters

- `session`: An [`MLTrainingSession`](../mltrainingsession.md) instance that represents the training session.

## See Also

### Training a hand pose classifier asynchronously
- [static func train(trainingData: MLHandPoseClassifier.DataSource, parameters: MLHandPoseClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLHandPoseClassifier>](./train%28trainingdata,parameters,sessionparameters%29.md)
  Begins an asynchronous hand pose classifier’s training session.
- [static func makeTrainingSession(trainingData: MLHandPoseClassifier.DataSource, parameters: MLHandPoseClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandPoseClassifier>](./maketrainingsession%28trainingdata,parameters,sessionparameters%29.md)
  Creates an asynchronous hand pose classifier’s training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandPoseClassifier>](./restoretrainingsession%28sessionparameters%29.md)
  Recreates an asynchronous hand pose classifier’s training session by restoring its saved state from the file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/resume(_:))*