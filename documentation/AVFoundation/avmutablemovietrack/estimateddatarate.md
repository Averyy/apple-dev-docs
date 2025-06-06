# estimatedDataRate

**Framework**: AVFoundation  
**Kind**: property

The estimated data rate, in bits per second, of the media that the track references.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var estimatedDataRate: Float { get }
```

## See Also

- [var timeRange: CMTimeRange](avmutablemovietrack/timerange.md)
  The time range of the track within the overall timeline of the asset.
- [var timescale: CMTimeScale](avmutablemovietrack/timescale.md)
  The time scale for tracks that contain the `moov` atom.
- [var naturalTimeScale: CMTimeScale](avmutablemovietrack/naturaltimescale.md)
  The natural time scale of the media that a track references.
- [func samplePresentationTime(forTrackTime: CMTime) -> CMTime](avmutablemovietrack/samplepresentationtime(fortracktime:).md)
  Maps the specified track time through the appropriate time mapping and returns the resulting sample presentation time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/estimateddatarate)*