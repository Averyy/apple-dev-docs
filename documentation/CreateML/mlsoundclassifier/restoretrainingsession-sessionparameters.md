# restoreTrainingSession(sessionParameters:)

**Framework**: Create ML  
**Kind**: method

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

An [`MLTrainingSession`](mltrainingsession.md) that represents the sound classifier training session.

## Parameters

- `sessionParameters`: The   instance you used to create the training session   using  .

## See Also

- [static func train(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLSoundClassifier>](mlsoundclassifier/train(trainingdata:parameters:sessionparameters:)-5hdqg.md)
  Begins an asynchronous sound classifier training session with a training dataset represented by a data source.
- [static func train(trainingData: [String : [URL]], parameters: MLSoundClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLSoundClassifier>](mlsoundclassifier/train(trainingdata:parameters:sessionparameters:)-6z4c8.md)
  Begins an asynchronous sound classifier training session with a training dataset represented by a dictionary.
- [static func makeTrainingSession(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLSoundClassifier>](mlsoundclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:).md)
  Creates an asynchronous training session for a sound classifier.
- [static func resume(MLTrainingSession<MLSoundClassifier>) throws -> MLJob<MLSoundClassifier>](mlsoundclassifier/resume(_:).md)
  Begins or continues an asynchronous training session for a sound classifier.
- [static func extractFeatures(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.FeatureExtractionParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLSoundClassifier.DataSource>](mlsoundclassifier/extractfeatures(trainingdata:parameters:sessionparameters:).md)
  Begins an asynchronous session that extracts sound features from a data source of sound files.
- [MLSoundClassifier.FeatureExtractionParameters](mlsoundclassifier/featureextractionparameters.md)
  Parameters that affect the process of extracting sound features from audio files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/restoretrainingsession(sessionparameters:))*