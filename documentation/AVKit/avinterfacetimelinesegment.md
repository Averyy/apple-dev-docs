# AVInterfaceTimelineSegment

**Framework**: AVKit  
**Kind**: class

Represents a contiguous segment of timeline content with specific playback characteristics.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
class AVInterfaceTimelineSegment
```

#### Overview

Timeline segments divide media content into distinct regions, each with its own classification and behavior rules. Segments are typically used to distinguish between primary content and auxiliary content such as advertisements or bonus material, and to control whether users can seek or skip through specific portions of the timeline.

## Topics

### Creating a timeline segment
- [init(timeRange: CMTimeRange, auxiliaryContent: Bool, marked: Bool, requiresLinearPlayback: Bool, identifier: String?)](avinterfacetimelinesegment/init(timerange:auxiliarycontent:marked:requireslinearplayback:identifier:).md)
  Initializes a new timeline segment with the specified characteristics.
### Inspecting the segment
- [var timeRange: CMTimeRange](avinterfacetimelinesegment/timerange.md)
  The time range defining the segment’s position and duration within the overall timeline.
- [var identifier: String?](avinterfacetimelinesegment/identifier.md)
  Optional external identifier for tracking or analytics purposes. May correspond to advertisement IDs, chapter markers, or other external systems.
- [var isAuxiliaryContent: Bool](avinterfacetimelinesegment/isauxiliarycontent.md)
  Indicates whether this segment consists of auxiliary or main content. Returns YES for auxiliary content, such as advertisements, interludes, or bonus material, and NO for main content, such as the main program material.
- [var isMarked: Bool](avinterfacetimelinesegment/ismarked.md)
  Indicates whether this segment should be visually highlighted or marked in the timeline UI.
- [var requiresLinearPlayback: Bool](avinterfacetimelinesegment/requireslinearplayback.md)
  Indicates whether this segment must be played sequentially without seeking or skipping. Typically used for advertisements or important announcements.
### Initializers
- [init?(coder: NSCoder)](avinterfacetimelinesegment/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol AVInterfaceTimeControllable](avinterfacetimecontrollable-63tkp.md)
  Provides time control and navigation capabilities for media content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacetimelinesegment)*