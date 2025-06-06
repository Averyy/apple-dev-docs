# AVAssetSegmentTrackReport

**Framework**: AVFoundation  
**Kind**: class

An object that provides information on a track in segment data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class AVAssetSegmentTrackReport
```

## Topics

### Inspecting a Report
- [var trackID: CMPersistentTrackID](avassetsegmenttrackreport/trackid.md)
  A persistent unique identifier for a track.
- [var mediaType: AVMediaType](avassetsegmenttrackreport/mediatype.md)
  The type of media a track contains.
- [var duration: CMTime](avassetsegmenttrackreport/duration.md)
  The duration of a track.
- [var earliestPresentationTimeStamp: CMTime](avassetsegmenttrackreport/earliestpresentationtimestamp.md)
  The earliest presentation timestamp (PTS) for this track.
- [var firstVideoSampleInformation: AVAssetSegmentReportSampleInformation?](avassetsegmenttrackreport/firstvideosampleinformation.md)
  Information about the first video sample in a track.
- [class AVAssetSegmentReportSampleInformation](avassetsegmentreportsampleinformation.md)
  An object that provides information about sample data in a track.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var segmentType: AVAssetSegmentType](avassetsegmentreport/segmenttype.md)
  The type of segment data.
- [enum AVAssetSegmentType](avassetsegmenttype.md)
  Constants that define the type of a segment.
- [var trackReports: [AVAssetSegmentTrackReport]](avassetsegmentreport/trackreports.md)
  The reports for the segment’s track data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetsegmenttrackreport)*