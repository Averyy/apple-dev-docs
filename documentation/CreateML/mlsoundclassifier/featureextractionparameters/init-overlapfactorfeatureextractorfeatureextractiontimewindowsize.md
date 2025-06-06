# init(overlapFactor:featureExtractor:featureExtractionTimeWindowSize:)

**Framework**: Create ML  
**Kind**: init

Creates the parameters for a feature-extraction session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
init(overlapFactor: Double = __Defaults.overlapFactor, featureExtractor: MLSoundClassifier.ModelParameters.FeatureExtractorType = __Defaults.featureExtractor, featureExtractionTimeWindowSize: TimeInterval?)
```

## Parameters

- `overlapFactor`: A portion of overlap between consecutive audio analysis windows. The value must be in   the range  .
- `featureExtractor`: An algorithm type the session uses to extract features from audio files.
- `featureExtractionTimeWindowSize`: A time duration, in seconds, the feature-extraction session uses for   each audio sample it reads from an audio file in a dataset. The value must be in the range   .

## See Also

- [init(overlapFactor: Double, featureExtractor: MLSoundClassifier.ModelParameters.FeatureExtractorType)](mlsoundclassifier/featureextractionparameters/init(overlapfactor:featureextractor:).md)
  Creates the parameters for a feature-extraction session with a default time window size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/init(overlapfactor:featureextractor:featureextractiontimewindowsize:))*