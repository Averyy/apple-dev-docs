# isAuxiliaryContent

**Framework**: AVKit  
**Kind**: property

Indicates whether this segment consists of auxiliary or main content. Returns YES for auxiliary content, such as advertisements, interludes, or bonus material, and NO for main content, such as the main program material.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
var isAuxiliaryContent: Bool { get }
```

## See Also

- [var timeRange: CMTimeRange](avinterfacetimelinesegment/timerange.md)
  The time range defining the segment’s position and duration within the overall timeline.
- [var identifier: String?](avinterfacetimelinesegment/identifier.md)
  Optional external identifier for tracking or analytics purposes. May correspond to advertisement IDs, chapter markers, or other external systems.
- [var isMarked: Bool](avinterfacetimelinesegment/ismarked.md)
  Indicates whether this segment should be visually highlighted or marked in the timeline UI.
- [var requiresLinearPlayback: Bool](avinterfacetimelinesegment/requireslinearplayback.md)
  Indicates whether this segment must be played sequentially without seeking or skipping. Typically used for advertisements or important announcements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacetimelinesegment/isauxiliarycontent)*