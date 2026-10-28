# AVInterfaceTimelineSegment

**Framework**: AVKit  
**Kind**: class  
**Role**: Class

Represents a contiguous segment of timeline content with specific playback characteristics.

## Declaration

```objc
@interface AVInterfaceTimelineSegment : NSObject
```

## Overview

Timeline segments divide media content into distinct regions, each with its own classification and behavior rules. Segments are typically used to distinguish between primary content and auxiliary content such as advertisements or bonus material, and to control whether users can seek or skip through specific portions of the timeline.

## Topics

### Instance Properties
- [auxiliaryContent](./avinterfacetimelinesegment/auxiliarycontent.md)
  Indicates whether this segment consists of auxiliary or main content. Returns YES for auxiliary content, such as advertisements, interludes, or bonus material, and NO for main content, such as the main program material.
- [identifier](./avinterfacetimelinesegment/identifier.md)
  Optional external identifier for tracking or analytics purposes. May correspond to advertisement IDs, chapter markers, or other external systems.
- [marked](./avinterfacetimelinesegment/marked.md)
  Indicates whether this segment should be visually highlighted or marked in the timeline UI.
- [requiresLinearPlayback](./avinterfacetimelinesegment/requireslinearplayback.md)
  Indicates whether this segment must be played sequentially without seeking or skipping. Typically used for advertisements or important announcements.
- [timeRange](./avinterfacetimelinesegment/timerange.md)
  The time range defining the segment’s position and duration within the overall timeline.
### Instance Methods
- [- initWithTimeRange:auxiliaryContent:marked:requiresLinearPlayback:identifier:](./avinterfacetimelinesegment/initwithtimerange_auxiliarycontent_marked_requireslinearplayback_identifier_.md)
  Initializes a new timeline segment with the specified characteristics.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacetimelinesegment)*