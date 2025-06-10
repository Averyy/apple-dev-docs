# samplePresentationTime(forTrackTime:)

**Framework**: AVFoundation  
**Kind**: method

Maps the specified track time through the appropriate time mapping and returns the resulting sample presentation time.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func samplePresentationTime(forTrackTime trackTime: CMTime) -> CMTime
```

#### Return Value

The sample presentation time corresponding to the specified time; otherwise [`invalid`](https://developer.apple.com/documentation/CoreMedia/CMTime/invalid) if the time is out of range.

## Parameters

- `trackTime`: The track time for which to request the sample presentation time.

## See Also

- [var timeRange: CMTimeRange](avmutablemovietrack/timerange.md)
  The time range of the track within the overall timeline of the asset.
- [var timescale: CMTimeScale](avmutablemovietrack/timescale.md)
  The time scale for tracks that contain the `moov` atom.
- [var naturalTimeScale: CMTimeScale](avmutablemovietrack/naturaltimescale.md)
  The natural time scale of the media that a track references.
- [var estimatedDataRate: Float](avmutablemovietrack/estimateddatarate.md)
  The estimated data rate, in bits per second, of the media that the track references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/samplepresentationtime(fortracktime:))*