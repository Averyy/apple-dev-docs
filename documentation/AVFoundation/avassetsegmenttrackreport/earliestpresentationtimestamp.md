# earliestPresentationTimeStamp

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) CMTime earliestPresentationTimeStamp;
```

## Discussion

The value is [`invalid`](../../CoreMedia/cmtime/invalid.md) if there’s no information available.

## See Also

### Inspecting a report
- [var trackID: CMPersistentTrackID](./trackid.md)
  A persistent unique identifier for a track.
- [var mediaType: AVMediaType](./mediatype.md)
  The type of media a track contains.
- [var duration: CMTime](./duration.md)
  The duration of a track.
- [var firstVideoSampleInformation: AVAssetSegmentReportSampleInformation?](./firstvideosampleinformation.md)
  Information about the first video sample in a track.
- [class AVAssetSegmentReportSampleInformation](../avassetsegmentreportsampleinformation.md)
  An object that provides information about sample data in a track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetsegmenttrackreport/earliestpresentationtimestamp)*