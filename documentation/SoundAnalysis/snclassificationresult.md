# SNClassificationResult

**Framework**: Sound Analysis  
**Kind**: class

A result that contains the highest-ranking classifications in a time range.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class SNClassificationResult
```

#### Overview

An `SNClassificationResult` represents the predictions that a sound classification model made for a time span in an audio file or stream. Each result contains one or more classification predictions and a time range within the audio data.

An audio analyzer, such as [`SNAudioFileAnalyzer`](snaudiofileanalyzer.md) and [`SNAudioStreamAnalyzer`](snaudiostreamanalyzer.md), produces an `SNClassificationResult` each time it recognizes a sound for any of its [`SNClassifySoundRequest`](snclassifysoundrequest.md) instances.

## Topics

### Inspecting the Result
- [var timeRange: CMTimeRange](snclassificationresult/timerange.md)
  The time span that corresponds to the result’s classifications.
- [var classifications: [SNClassification]](snclassificationresult/classifications.md)
  A sorted array of the request’s top classification candidates.
- [class SNClassification](snclassification.md)
  A type that pairs a sound classifier’s prediction with its confidence in that prediction.
- [func classification(forIdentifier: String) -> SNClassification?](snclassificationresult/classification(foridentifier:).md)
  Returns the classification for an identifier.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [SNResult](snresult.md)

## See Also

- [Classifying Live Audio Input with a Built-in Sound Classifier](classifying-live-audio-input-with-a-built-in-sound-classifier.md)
  Detect and identify hundreds of sounds by using a trained classifier.
- [class SNClassifySoundRequest](snclassifysoundrequest.md)
  A request that classifies sound using a Core ML model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snclassificationresult)*