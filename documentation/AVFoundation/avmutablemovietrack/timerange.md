# timeRange

**Framework**: AVFoundation  
**Kind**: property

The time range of the track within the overall timeline of the asset.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var timeRange: CMTimeRange { get }
```

#### Discussion

If the start of the time range is greater than [`zero`](https://developer.apple.com/documentation/CoreMedia/CMTime/zero), the track doesn’t initially have media data to present. This condition may occur when the media delays an audio track to align the start of audio with a specific video frame. You can test for this as the example below shows:

```swift
if track.timeRange.start > .zero {
    // Delayed start.
}
```

## See Also

- [var timescale: CMTimeScale](avmutablemovietrack/timescale.md)
  The time scale for tracks that contain the `moov` atom.
- [var naturalTimeScale: CMTimeScale](avmutablemovietrack/naturaltimescale.md)
  The natural time scale of the media that a track references.
- [var estimatedDataRate: Float](avmutablemovietrack/estimateddatarate.md)
  The estimated data rate, in bits per second, of the media that the track references.
- [func samplePresentationTime(forTrackTime: CMTime) -> CMTime](avmutablemovietrack/samplepresentationtime(fortracktime:).md)
  Maps the specified track time through the appropriate time mapping and returns the resulting sample presentation time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/timerange)*