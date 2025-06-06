# estimatedDataRate

**Framework**: AVFoundation  
**Kind**: property

The estimated data rate, in bits per second, of the media that the track references.

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
var estimatedDataRate: Float { get }
```

## See Also

- [var timeRange: CMTimeRange](avcompositiontrack/timerange.md)
  The time range of the track within the overall timeline of the asset.
- [var naturalTimeScale: CMTimeScale](avcompositiontrack/naturaltimescale.md)
  The natural time scale of the media that a track references.
- [func samplePresentationTime(forTrackTime: CMTime) -> CMTime](avcompositiontrack/samplepresentationtime(fortracktime:).md)
  Maps the specified track time through the appropriate time mapping and returns the resulting sample presentation time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontrack/estimateddatarate)*