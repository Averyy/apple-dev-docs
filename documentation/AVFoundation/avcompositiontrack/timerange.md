# timeRange

**Framework**: AVFoundation  
**Kind**: property

The time range of the track within the overall timeline of the asset.

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

- [var naturalTimeScale: CMTimeScale](avcompositiontrack/naturaltimescale.md)
  The natural time scale of the media that a track references.
- [var estimatedDataRate: Float](avcompositiontrack/estimateddatarate.md)
  The estimated data rate, in bits per second, of the media that the track references.
- [func samplePresentationTime(forTrackTime: CMTime) -> CMTime](avcompositiontrack/samplepresentationtime(fortracktime:).md)
  Maps the specified track time through the appropriate time mapping and returns the resulting sample presentation time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontrack/timerange)*