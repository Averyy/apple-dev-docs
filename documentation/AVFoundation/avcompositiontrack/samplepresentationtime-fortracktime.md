# samplePresentationTime(forTrackTime:)

**Framework**: AVFoundation  
**Kind**: method

Maps the specified track time through the appropriate time mapping and returns the resulting sample presentation time.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func samplePresentationTime(forTrackTime trackTime: CMTime) -> CMTime
```

#### Return Value

The sample presentation time corresponding to the specified time; otherwise [`invalid`](https://developer.apple.com/documentation/coremedia/cmtime/1400807-invalid) if the time is out of range.

## Parameters

- `trackTime`: The track time for which to request the sample presentation time.

## See Also

- [var timeRange: CMTimeRange](avcompositiontrack/timerange.md)
  The time range of the track within the overall timeline of the asset.
- [var naturalTimeScale: CMTimeScale](avcompositiontrack/naturaltimescale.md)
  The natural time scale of the media that a track references.
- [var estimatedDataRate: Float](avcompositiontrack/estimateddatarate.md)
  The estimated data rate, in bits per second, of the media that the track references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontrack/samplepresentationtime(fortracktime:))*