# timeRange

**Framework**: Sound Analysis  
**Kind**: property

The time span that corresponds to the result’s classifications.

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
var timeRange: CMTimeRange { get }
```

#### Discussion

The time range’s doc://com.apple.documentation/documentation/coremedia/cmtime-u58 values are the number of audio frames at the analyzer’s sample rate. Use these time indices to determine where, in time, the result corresponds to the original audio.

A result’s time range typically refers to audio older than its most recent audio because the request gathers the data into blocks before sending them to the model.

## See Also

- [var classifications: [SNClassification]](snclassificationresult/classifications.md)
  A sorted array of the request’s top classification candidates.
- [class SNClassification](snclassification.md)
  A type that pairs a sound classifier’s prediction with its confidence in that prediction.
- [func classification(forIdentifier: String) -> SNClassification?](snclassificationresult/classification(foridentifier:).md)
  Returns the classification for an identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snclassificationresult/timerange)*