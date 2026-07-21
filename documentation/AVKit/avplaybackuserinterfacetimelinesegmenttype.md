# AVPlaybackUserInterfaceTimelineSegmentType

**Framework**: AVKit  
**Kind**: enum

Describes the type of content within a timeline segment.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
enum AVPlaybackUserInterfaceTimelineSegmentType
```

## Topics

### Enumeration Cases
- [AVPlaybackUserInterfaceTimelineSegmentType.advertisement](avplaybackuserinterfacetimelinesegmenttype/advertisement.md)
  The segment contains an advertisement.
- [AVPlaybackUserInterfaceTimelineSegmentType.bonus](avplaybackuserinterfacetimelinesegmenttype/bonus.md)
  The segment contains bonus content, such as a post-credits scene or supplemental material.
- [AVPlaybackUserInterfaceTimelineSegmentType.credits](avplaybackuserinterfacetimelinesegmenttype/credits.md)
  The segment contains end credits.
- [AVPlaybackUserInterfaceTimelineSegmentType.intro](avplaybackuserinterfacetimelinesegmenttype/intro.md)
  The segment contains an opening title sequence.
- [AVPlaybackUserInterfaceTimelineSegmentType.other](avplaybackuserinterfacetimelinesegmenttype/other.md)
  The segment contains auxiliary content of an unspecified type.
- [AVPlaybackUserInterfaceTimelineSegmentType.primary](avplaybackuserinterfacetimelinesegmenttype/primary.md)
  The segment contains primary program content.
- [AVPlaybackUserInterfaceTimelineSegmentType.recap](avplaybackuserinterfacetimelinesegmenttype/recap.md)
  The segment contains a recap of previous content.
- [AVPlaybackUserInterfaceTimelineSegmentType.trailer](avplaybackuserinterfacetimelinesegmenttype/trailer.md)
  The segment contains a trailer or preview for other content.
### Initializers
- [init?(rawValue: Int)](avplaybackuserinterfacetimelinesegmenttype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol AVPlaybackUserInterfaceTimeControllable](avplaybackuserinterfacetimecontrollable-50vcy.md)
  Provides time control and navigation capabilities for media content.
- [class AVPlaybackUserInterfacePlaybackPosition](avplaybackuserinterfaceplaybackposition.md)
  A snapshot comprising a playback position recorded at a known host time and the rate of position advancement.
- [class AVPlaybackUserInterfaceTimelineSegment](avplaybackuserinterfacetimelinesegment.md)
  Represents a contiguous segment of timeline content with specific playback characteristics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacetimelinesegmenttype)*