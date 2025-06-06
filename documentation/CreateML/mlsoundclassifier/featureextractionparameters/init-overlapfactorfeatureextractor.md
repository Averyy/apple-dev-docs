# init(overlapFactor:featureExtractor:)

**Framework**: Create ML  
**Kind**: init

Creates the parameters for a feature-extraction session with a default time window size.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(overlapFactor: Double = __Defaults.overlapFactor, featureExtractor: MLSoundClassifier.ModelParameters.FeatureExtractorType = __Defaults.featureExtractor)
```

#### Discussion

The initializer sets [`featureExtractionTimeWindowSize`](mlsoundclassifier/featureextractionparameters/featureextractiontimewindowsize.md) to a default value.

## Parameters

- `overlapFactor`: A portion of overlap between consecutive audio analysis windows. The value must be in   the range  .
- `featureExtractor`: An algorithm type the session uses to extract features from audio files.

## See Also

- [init(overlapFactor: Double, featureExtractor: MLSoundClassifier.ModelParameters.FeatureExtractorType, featureExtractionTimeWindowSize: TimeInterval?)](mlsoundclassifier/featureextractionparameters/init(overlapfactor:featureextractor:featureextractiontimewindowsize:).md)
  Creates the parameters for a feature-extraction session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/init(overlapfactor:featureextractor:))*