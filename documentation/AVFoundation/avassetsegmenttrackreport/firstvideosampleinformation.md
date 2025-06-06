# firstVideoSampleInformation

**Framework**: AVFoundation  
**Kind**: property

Information about the first video sample in a track.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var firstVideoSampleInformation: AVAssetSegmentReportSampleInformation? { get }
```

#### Discussion

The value is `nil` if this track isn’t a video track, or if sample information isn’t available.

## See Also

- [var trackID: CMPersistentTrackID](avassetsegmenttrackreport/trackid.md)
  A persistent unique identifier for a track.
- [var mediaType: AVMediaType](avassetsegmenttrackreport/mediatype.md)
  The type of media a track contains.
- [var duration: CMTime](avassetsegmenttrackreport/duration.md)
  The duration of a track.
- [var earliestPresentationTimeStamp: CMTime](avassetsegmenttrackreport/earliestpresentationtimestamp.md)
  The earliest presentation timestamp (PTS) for this track.
- [class AVAssetSegmentReportSampleInformation](avassetsegmentreportsampleinformation.md)
  An object that provides information about sample data in a track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetsegmenttrackreport/firstvideosampleinformation)*