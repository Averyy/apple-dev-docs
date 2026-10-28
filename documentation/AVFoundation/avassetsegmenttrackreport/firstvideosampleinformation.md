# firstVideoSampleInformation

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, nullable) AVAssetSegmentReportSampleInformation * firstVideoSampleInformation;
```

## Discussion

The value is `nil` if this track isn’t a video track, or if sample information isn’t available.

## See Also

### Inspecting a report
- [var trackID: CMPersistentTrackID](./trackid.md)
  A persistent unique identifier for a track.
- [var mediaType: AVMediaType](./mediatype.md)
  The type of media a track contains.
- [var duration: CMTime](./duration.md)
  The duration of a track.
- [var earliestPresentationTimeStamp: CMTime](./earliestpresentationtimestamp.md)
  The earliest presentation timestamp (PTS) for this track.
- [class AVAssetSegmentReportSampleInformation](../avassetsegmentreportsampleinformation.md)
  An object that provides information about sample data in a track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetsegmenttrackreport/firstvideosampleinformation)*