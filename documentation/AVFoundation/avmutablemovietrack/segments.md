# segments

**Framework**: AVFoundation  
**Kind**: property

The time mappings from the track’s media samples to its timeline.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var segments: [AVAssetTrackSegment] { get }
```

## See Also

- [func segment(forTrackTime: CMTime) -> AVAssetTrackSegment?](avmutablemovietrack/segment(fortracktime:).md)
  Returns a segment whose target time range contains, or is closest to, the specified track time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/segments)*