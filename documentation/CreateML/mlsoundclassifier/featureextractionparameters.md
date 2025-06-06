# MLSoundClassifier.FeatureExtractionParameters

**Framework**: Create ML  
**Kind**: struct

Parameters that affect the process of extracting sound features from audio files.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct FeatureExtractionParameters
```

## Topics

### Creating feature extraction parameters
- [init(overlapFactor: Double, featureExtractor: MLSoundClassifier.ModelParameters.FeatureExtractorType, featureExtractionTimeWindowSize: TimeInterval?)](mlsoundclassifier/featureextractionparameters/init(overlapfactor:featureextractor:featureextractiontimewindowsize:).md)
  Creates the parameters for a feature-extraction session.
- [init(overlapFactor: Double, featureExtractor: MLSoundClassifier.ModelParameters.FeatureExtractorType)](mlsoundclassifier/featureextractionparameters/init(overlapfactor:featureextractor:).md)
  Creates the parameters for a feature-extraction session with a default time window size.
### Accessing feature extraction parameters
- [var overlapFactor: Double](mlsoundclassifier/featureextractionparameters/overlapfactor.md)
  The proportion of overlap that the feature-extraction session uses to analyze two consecutive windows in the audio data.
- [var featureExtractor: MLSoundClassifier.ModelParameters.FeatureExtractorType](mlsoundclassifier/featureextractionparameters/featureextractor.md)
  The algorithm type the session uses to extract features from audio files.
- [var featureExtractionTimeWindowSize: TimeInterval](mlsoundclassifier/featureextractionparameters/featureextractiontimewindowsize.md)
  A time duration, in seconds, that determines how much audio data the feature-extraction session reads each time it samples an audio file.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [static func train(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLSoundClassifier>](mlsoundclassifier/train(trainingdata:parameters:sessionparameters:)-5hdqg.md)
  Begins an asynchronous sound classifier training session with a training dataset represented by a data source.
- [static func train(trainingData: [String : [URL]], parameters: MLSoundClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLSoundClassifier>](mlsoundclassifier/train(trainingdata:parameters:sessionparameters:)-6z4c8.md)
  Begins an asynchronous sound classifier training session with a training dataset represented by a dictionary.
- [static func makeTrainingSession(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLSoundClassifier>](mlsoundclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:).md)
  Creates an asynchronous training session for a sound classifier.
- [static func resume(MLTrainingSession<MLSoundClassifier>) throws -> MLJob<MLSoundClassifier>](mlsoundclassifier/resume(_:).md)
  Begins or continues an asynchronous training session for a sound classifier.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLSoundClassifier>](mlsoundclassifier/restoretrainingsession(sessionparameters:).md)
  Creates an asynchronous training session for a sound classifier by restoring an existing training session’s state from its parameters.
- [static func extractFeatures(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.FeatureExtractionParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLSoundClassifier.DataSource>](mlsoundclassifier/extractfeatures(trainingdata:parameters:sessionparameters:).md)
  Begins an asynchronous session that extracts sound features from a data source of sound files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters)*