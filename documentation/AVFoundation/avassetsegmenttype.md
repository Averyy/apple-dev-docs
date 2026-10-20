# AVAssetSegmentType

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Constants that define the type of a segment.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum AVAssetSegmentType
```

```c
enum AVAssetSegmentType : NSInteger;
```

## Topics

### Segment types
- [AVAssetSegmentType.initialization](./avassetsegmenttype/initialization.md)
  An initialization segment type.
- [AVAssetSegmentType.separable](./avassetsegmenttype/separable.md)
  A separable segment type.
### Initializers
- [init?(rawValue: Int)](./avassetsegmenttype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Inspecting a report
- [var segmentType: AVAssetSegmentType](./avassetsegmentreport/segmenttype.md)
  The type of segment data.
- [var trackReports: [AVAssetSegmentTrackReport]](./avassetsegmentreport/trackreports.md)
  The reports for the segment’s track data.
- [class AVAssetSegmentTrackReport](./avassetsegmenttrackreport.md)
  An object that provides information on a track in segment data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetsegmenttype)*