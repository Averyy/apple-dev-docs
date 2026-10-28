# timeRange

**Framework**: Sound Analysis  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) CMTimeRange timeRange;
```

## Discussion

The time range’s [`CMTime`](../../CoreMedia/cmtime.md) values are the number of audio frames at the analyzer’s sample rate. Use these time indices to determine where, in time, the result corresponds to the original audio.

A result’s time range typically refers to audio older than its most recent audio because the request gathers the data into blocks before sending them to the model.

## See Also

### Inspecting the Result
- [var classifications: [SNClassification]](./classifications.md)
  A sorted array of the request’s top classification candidates.
- [class SNClassification](../snclassification.md)
  A type that pairs a sound classifier’s prediction with its confidence in that prediction.
- [func classification(forIdentifier: String) -> SNClassification?](./classification%28foridentifier%29.md)
  Returns the classification for an identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snclassificationresult/timerange)*