# segmentConfigurations

**Framework**: AVFoundation  
**Kind**: property

Array of AVPlannedSegmentConfigurations, each element specifying the configuration of a planned segment, ordered in output PTS order.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

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