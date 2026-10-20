# MLSoundClassifier.FeatureExtractionParameters

**Framework**: Create ML  
**Kind**: struct  
**Role**: Structure

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
- [init(overlapFactor: Double, featureExtractor: MLSoundClassifier.ModelParameters.FeatureExtractorType, featureExtractionTimeWindowSize: TimeInterval?)](./featureextractionparameters/init%28overlapfactor,featureextractor,featureextractiontimewindowsize%29.md)
  Creates the parameters for a feature-extraction session.
- [init(overlapFactor: Double, featureExtractor: MLSoundClassifier.ModelParameters.FeatureExtractorType)](./featureextractionparameters/init%28overlapfactor,featureextractor%29.md)
  Creates the parameters for a feature-extraction session with a default time window size.
### Accessing feature extraction parameters
- [var overlapFactor: Double](./featureextractionparameters/overlapfactor.md)
  The proportion of overlap that the feature-extraction session uses to analyze two consecutive windows in the audio data.
- [var featureExtractor: MLSoundClassifier.ModelParameters.FeatureExtractorType](./featureextractionparameters/featureextractor.md)
  The algorithm type the session uses to extract features from audio files.
- [var featureExtractionTimeWindowSize: TimeInterval](./featureextractionparameters/featureextractiontimewindowsize.md)
  A time duration, in seconds, that determines how much audio data the feature-extraction session reads each time it samples an audio file.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Training a sound classifier asynchronously
- [static train(trainingData:parameters:sessionParameters:)](./train%28trainingdata,parameters,sessionparameters%29.md)
  Begins an asynchronous sound classifier training session with a training dataset represented by a data source.
- [static func makeTrainingSession(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLSoundClassifier>](./maketrainingsession%28trainingdata,parameters,sessionparameters%29.md)
  Creates an asynchronous training session for a sound classifier.
- [static func resume(MLTrainingSession<MLSoundClassifier>) throws -> MLJob<MLSoundClassifier>](./resume%28_%29.md)
  Begins or continues an asynchronous training session for a sound classifier.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLSoundClassifier>](./restoretrainingsession%28sessionparameters%29.md)
  Creates an asynchronous training session for a sound classifier by restoring an existing training session’s state from its parameters.
- [static func extractFeatures(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.FeatureExtractionParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLSoundClassifier.DataSource>](./extractfeatures%28trainingdata,parameters,sessionparameters%29.md)
  Begins an asynchronous session that extracts sound features from a data source of sound files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters)*