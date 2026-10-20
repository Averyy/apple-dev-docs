# mediaType

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The media type of this track.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var mediaType: AVMediaType { get }
```

```objc
@property (readonly) AVMediaType mediaType;
```

## See Also

### Inspecting the track plan
- [var segmentConfigurations: [AVPlannedSegmentConfiguration]](./segmentconfigurations.md)
  Array of AVPlannedSegmentConfigurations, each element specifying the configuration of a planned segment, ordered in output PTS order.
- [var assemblyTrackID: CMPersistentTrackID](./assemblytrackid.md)
  This is the track ID of this track when it is included in the assemblyComposition the planner passes to the completion handler to assemble all planned segments of all tracks into a single AVComposition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrackplan/mediatype)*