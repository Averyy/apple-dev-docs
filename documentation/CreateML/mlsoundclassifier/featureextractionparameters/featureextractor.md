# featureExtractor

**Framework**: Create ML  
**Kind**: property

The algorithm type the session uses to extract features from audio files.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var featureExtractor: MLSoundClassifier.ModelParameters.FeatureExtractorType
```

## See Also

- [var overlapFactor: Double](mlsoundclassifier/featureextractionparameters/overlapfactor.md)
  The proportion of overlap that the feature-extraction session uses to analyze two consecutive windows in the audio data.
- [var featureExtractionTimeWindowSize: TimeInterval](mlsoundclassifier/featureextractionparameters/featureextractiontimewindowsize.md)
  A time duration, in seconds, that determines how much audio data the feature-extraction session reads each time it samples an audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/featureextractor)*