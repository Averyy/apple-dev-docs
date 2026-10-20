# restoreTrainingSession(sessionParameters:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Type Method

Creates an asynchronous training session for a sound classifier by restoring an existing training session’s state from its parameters.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLSoundClassifier>
```

#### Return Value

An [`MLTrainingSession`](../mltrainingsession.md) that represents the sound classifier training session.

## Parameters

- `sessionParameters`: The [`MLTrainingSessionParameters`](../mltrainingsessionparameters.md) instance you used to create the training session using [`makeTrainingSession(trainingData:parameters:sessionParameters:)`](./maketrainingsession%28trainingdata,parameters,sessionparameters%29.md).

## See Also

### Training a sound classifier asynchronously
- [static train(trainingData:parameters:sessionParameters:)](./train%28trainingdata,parameters,sessionparameters%29.md)
  Begins an asynchronous sound classifier training session with a training dataset represented by a data source.
- [static func makeTrainingSession(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLSoundClassifier>](./maketrainingsession%28trainingdata,parameters,sessionparameters%29.md)
  Creates an asynchronous training session for a sound classifier.
- [static func resume(MLTrainingSession<MLSoundClassifier>) throws -> MLJob<MLSoundClassifier>](./resume%28_%29.md)
  Begins or continues an asynchronous training session for a sound classifier.
- [static func extractFeatures(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.FeatureExtractionParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLSoundClassifier.DataSource>](./extractfeatures%28trainingdata,parameters,sessionparameters%29.md)
  Begins an asynchronous session that extracts sound features from a data source of sound files.
- [MLSoundClassifier.FeatureExtractionParameters](./featureextractionparameters.md)
  Parameters that affect the process of extracting sound features from audio files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/restoretrainingsession(sessionparameters:))*