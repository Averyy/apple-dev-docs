# assemblyTrackID

**Framework**: AVFoundation  
**Kind**: property

This is the track ID of this track when it is included in the assemblyComposition the planner passes to the completion handler to assemble all planned segments of all tracks into a single AVComposition.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var assemblyTrackID: CMPersistentTrackID { get }
```

#### Discussion

The assemblyTrackID serves the purpose as a unique identifier of the track in the incremental writing session. This does not necessarily match the trackID of the source asset. The client is responsible for remembering the relationship between assemblyTrackID and the trackID in the source asset.

## See Also

- [var mediaType: AVMediaType](avassettrackplan/mediatype.md)
  The media type of this track.
- [var segmentConfigurations: [AVPlannedSegmentConfiguration]](avassettrackplan/segmentconfigurations.md)
  Array of AVPlannedSegmentConfigurations, each element specifying the configuration of a planned segment, ordered in output PTS order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrackplan/assemblytrackid)*