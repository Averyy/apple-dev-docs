# assemblyTrackID

**Framework**: AVFoundation  
**Kind**: property

This is the track ID of this track when it is included in the assemblyComposition the planner passes to the completion handler to assemble all planned segments of all tracks into a single AVComposition.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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
  An array of AVPlannedSegmentConfigurations, each element specifying the configuration of a planned segment, ordered in output PTS order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrackplan/assemblytrackid)*