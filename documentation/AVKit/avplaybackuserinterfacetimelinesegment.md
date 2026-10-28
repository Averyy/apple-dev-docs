# AVPlaybackUserInterfaceTimelineSegment

**Framework**: AVKit  
**Kind**: class  
**Role**: Class

Represents a contiguous segment of timeline content with specific playback characteristics.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
class AVPlaybackUserInterfaceTimelineSegment
```

```objc
@interface AVPlaybackUserInterfaceTimelineSegment : NSObject
```

## Overview

Timeline segments divide media content into distinct regions, each with its own classification and behavior rules. Segments are typically used to distinguish between primary content and auxiliary content such as advertisements or bonus material, and to control whether users can seek or skip through specific portions of the timeline.

## Topics

### Initializers
- [init?(coder: NSCoder)](./avplaybackuserinterfacetimelinesegment/init%28coder%29.md)
- [init(timeRange: CMTimeRange, segmentType: AVPlaybackUserInterfaceTimelineSegmentType, marked: Bool, requiresLinearPlayback: Bool, identifier: String?)](./avplaybackuserinterfacetimelinesegment/init%28timerange,segmenttype,marked,requireslinearplayback,identifier%29.md)
  Initializes a new timeline segment with the specified characteristics.
### Instance Properties
- [var identifier: String?](./avplaybackuserinterfacetimelinesegment/identifier.md)
  Optional external identifier for tracking or analytics purposes. May correspond to advertisement IDs, chapter markers, or other external systems.
- [var isMarked: Bool](./avplaybackuserinterfacetimelinesegment/ismarked.md)
  Indicates whether this segment should be visually highlighted or marked in the timeline UI.
- [var requiresLinearPlayback: Bool](./avplaybackuserinterfacetimelinesegment/requireslinearplayback.md)
  Indicates whether this segment must be played sequentially without seeking or skipping. Typically used for advertisements or important announcements.
- [var segmentType: AVPlaybackUserInterfaceTimelineSegmentType](./avplaybackuserinterfacetimelinesegment/segmenttype.md)
  The type of content within this segment, indicating whether it is primary program content or a specific category of auxiliary content.
- [var timeRange: CMTimeRange](./avplaybackuserinterfacetimelinesegment/timerange.md)
  The time range defining the segment’s position and duration within the overall timeline.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Timeline and segments
- [protocol AVPlaybackUserInterfaceTimeControllable](./avplaybackuserinterfacetimecontrollable-50vcy.md)
  Provides time control and navigation capabilities for media content.
- [class AVPlaybackUserInterfacePlaybackPosition](./avplaybackuserinterfaceplaybackposition.md)
  A snapshot comprising a playback position recorded at a known host time and the rate of position advancement.
- [enum AVPlaybackUserInterfaceTimelineSegmentType](./avplaybackuserinterfacetimelinesegmenttype.md)
  Describes the type of content within a timeline segment.
- [AVPlaybackUserInterfaceTimeControllable](./avplaybackuserinterfacetimecontrollable-62fq2.md)
  Provides time control and navigation capabilities for media content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacetimelinesegment)*