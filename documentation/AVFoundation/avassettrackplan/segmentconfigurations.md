# segmentConfigurations

**Framework**: AVFoundation  
**Kind**: property

An array of AVPlannedSegmentConfigurations, each element specifying the configuration of a planned segment, ordered in output PTS order.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var segmentConfigurations: [AVPlannedSegmentConfiguration] { get }
```

## See Also

- [var mediaType: AVMediaType](avassettrackplan/mediatype.md)
  The media type of this track.
- [var assemblyTrackID: CMPersistentTrackID](avassettrackplan/assemblytrackid.md)
  This is the track ID of this track when it is included in the assemblyComposition the planner passes to the completion handler to assemble all planned segments of all tracks into a single AVComposition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrackplan/segmentconfigurations)*