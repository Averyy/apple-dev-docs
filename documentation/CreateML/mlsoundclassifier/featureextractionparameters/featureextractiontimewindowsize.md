# featureExtractionTimeWindowSize

**Framework**: Create ML  
**Kind**: property

A time duration, in seconds, that determines how much audio data the feature-extraction session reads each time it samples an audio file.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var featureExtractionTimeWindowSize: TimeInterval { get set }
```

#### Discussion

The time-window size defaults to `0.975` seconds and must be in the range `[0.5, 15.0]`.

Feature-extraction sessions that use [`MLSoundClassifier.ModelParameters.FeatureExtractorType.vggish(revision:)`](mlsoundclassifier/modelparameters-swift.struct/featureextractortype/vggish(revision:).md) ignore this value and always use a time-window size of `0.975` seconds.

## See Also

- [var overlapFactor: Double](mlsoundclassifier/featureextractionparameters/overlapfactor.md)
  The proportion of overlap that the feature-extraction session uses to analyze two consecutive windows in the audio data.
- [var featureExtractor: MLSoundClassifier.ModelParameters.FeatureExtractorType](mlsoundclassifier/featureextractionparameters/featureextractor.md)
  The algorithm type the session uses to extract features from audio files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/featureextractionparameters/featureextractiontimewindowsize)*