# earliestPresentationTimeStamp

**Framework**: AVFoundation  
**Kind**: property

The earliest presentation timestamp (PTS) for this track.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var earliestPresentationTimeStamp: CMTime { get }
```

#### Discussion

The value is [`invalid`](https://developer.apple.com/documentation/coremedia/cmtime/1400807-invalid) if there’s no information available.

## See Also

- [var trackID: CMPersistentTrackID](avassetsegmenttrackreport/trackid.md)
  A persistent unique identifier for a track.
- [var mediaType: AVMediaType](avassetsegmenttrackreport/mediatype.md)
  The type of media a track contains.
- [var duration: CMTime](avassetsegmenttrackreport/duration.md)
  The duration of a track.
- [var firstVideoSampleInformation: AVAssetSegmentReportSampleInformation?](avassetsegmenttrackreport/firstvideosampleinformation.md)
  Information about the first video sample in a track.
- [class AVAssetSegmentReportSampleInformation](avassetsegmentreportsampleinformation.md)
  An object that provides information about sample data in a track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetsegmenttrackreport/earliestpresentationtimestamp)*