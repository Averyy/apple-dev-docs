# AVPlayerItemSegment.SegmentType

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the type of segment.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
enum SegmentType
```

```c
enum AVPlayerItemSegmentType : NSInteger;
```

## Topics

### Segment types
- [AVPlayerItemSegment.SegmentType.primary](./segmenttype-swift.enum/primary.md)
  A segment that represents playback of a primary item.
- [AVPlayerItemSegment.SegmentType.interstitial](./segmenttype-swift.enum/interstitial.md)
  A segment that represents playback of an interstitial event.
### Initializers
- [init?(rawValue: Int)](./segmenttype-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Identifying the type
- [var segmentType: AVPlayerItemSegment.SegmentType](./segmenttype-swift.property.md)
  The type content this segment represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemsegment/segmenttype-swift.enum)*