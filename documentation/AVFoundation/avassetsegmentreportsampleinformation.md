# AVAssetSegmentReportSampleInformation

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that provides information about sample data in a track.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class AVAssetSegmentReportSampleInformation
```

```objc
@interface AVAssetSegmentReportSampleInformation : NSObject
```

## Topics

### Inspecting the information
- [var presentationTimeStamp: CMTime](./avassetsegmentreportsampleinformation/presentationtimestamp.md)
  The presentation timestamp (PTS) of a sample.
- [var offset: Int](./avassetsegmentreportsampleinformation/offset.md)
  The offset of a sample in the segment.
- [var length: Int](./avassetsegmentreportsampleinformation/length.md)
  The length of the sample data.
- [var isSyncSample: Bool](./avassetsegmentreportsampleinformation/issyncsample.md)
  A Boolean value that indicates whether the sample is a key frame.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Inspecting a report
- [var trackID: CMPersistentTrackID](./avassetsegmenttrackreport/trackid.md)
  A persistent unique identifier for a track.
- [var mediaType: AVMediaType](./avassetsegmenttrackreport/mediatype.md)
  The type of media a track contains.
- [var duration: CMTime](./avassetsegmenttrackreport/duration.md)
  The duration of a track.
- [var earliestPresentationTimeStamp: CMTime](./avassetsegmenttrackreport/earliestpresentationtimestamp.md)
  The earliest presentation timestamp (PTS) for this track.
- [var firstVideoSampleInformation: AVAssetSegmentReportSampleInformation?](./avassetsegmenttrackreport/firstvideosampleinformation.md)
  Information about the first video sample in a track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetsegmentreportsampleinformation)*