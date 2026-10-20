# naturalTimeScale

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The natural time scale of the media that a track references.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var naturalTimeScale: CMTimeScale { get }
```

## See Also

### Accessing temporal information
- [var timeRange: CMTimeRange](./timerange.md)
  The time range of the track within the overall timeline of the asset.
- [var timescale: CMTimeScale](./timescale.md)
  The time scale for tracks that contain the `moov` atom.
- [var estimatedDataRate: Float](./estimateddatarate.md)
  The estimated data rate, in bits per second, of the media that the track references.
- [func samplePresentationTime(forTrackTime: CMTime) -> CMTime](./samplepresentationtime%28fortracktime%29.md)
  Maps the specified track time through the appropriate time mapping and returns the resulting sample presentation time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/naturaltimescale)*