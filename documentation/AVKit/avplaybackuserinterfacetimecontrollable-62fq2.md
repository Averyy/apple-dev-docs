# AVPlaybackUserInterfaceTimeControllable

**Framework**: AVKit  
**Kind**: protocol  
**Role**: Protocol

Provides time control and navigation capabilities for media content.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
@protocol AVPlaybackUserInterfaceTimeControllable <NSObject>
```

## Topics

### Instance Properties
- [currentSegment](./avplaybackuserinterfacetimecontrollable-62fq2/currentsegment.md)
  The segment containing the current playback position. This property automatically updates as playback progresses through different timeline segments. Use this to determine the current content type (primary vs. secondary) and any special playback characteristics that apply to the current position. Must be key-value observable.
- [playbackPosition](./avplaybackuserinterfacetimecontrollable-62fq2/playbackposition.md)
  A snapshot of the current playback position. Must be updated — with a fresh `hostTime` — on play, pause, seek, scan, and buffering state changes. Must be key-value observable.
- [seekableTimeRanges](./avplaybackuserinterfacetimecontrollable-62fq2/seekabletimeranges.md)
  An array of time ranges within the timeline where seeking operations are permitted. Each range is represented as an NSValue wrapping a CMTimeRange structure, defining portions of the timeline where users can jump to specific time positions during playback. If `nil`, the entire content defined by timeRange is considered seekable. When provided, each range must be a subset of the overall timeRange and should not overlap with other seekable ranges. An empty array means the entire content defined by timeRange is not seekable. Seekable ranges typically exclude segments where requiresLinearPlayback is YES, such as advertisements, mandatory content, or licensing-restricted portions. The array should contain ranges in chronological order for optimal performance. Must be key-value observable.
- [segments](./avplaybackuserinterfacetimecontrollable-62fq2/segments.md)
  Segments representing different content types within the timeline. All segments should be contiguous and collectively cover the entire timeline duration without gaps or overlaps. Each segment defines a specific portion of content (such as main program, advertisements, or bonus material) with its own playback characteristics. Must be key-value observable.
- [timeRange](./avplaybackuserinterfacetimecontrollable-62fq2/timerange.md)
  The time range representing the total duration and bounds of the media content. This defines the overall playable timeline, with all segments and seekable ranges falling within this range. For on-demand content, `start` is typically zero and `duration` is the total length of the content. For live content without DVR, set [`timeRange`](./avplaybackuserinterfacetimecontrollable-62fq2/timerange.md) to a zero-duration range at the current live edge and advance it as the edge moves; [`seekableTimeRanges`](./avplaybackuserinterfacetimecontrollable-62fq2/seekabletimeranges.md) must be nil or empty. For live content with DVR, set [`timeRange`](./avplaybackuserinterfacetimecontrollable-62fq2/timerange.md) to the available DVR window and advance both `start` and `end` as the window rolls. Use [`seekableTimeRanges`](./avplaybackuserinterfacetimecontrollable-62fq2/seekabletimeranges.md) to indicate which portion is seekable. The duration is always a finite, non-negative value. Must be key-value observable.
### Instance Methods
- [- seekToPosition:tolerance:](./avplaybackuserinterfacetimecontrollable-62fq2/seektoposition_tolerance_.md)
  Requests a seek to the specified position.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [AVPlaybackUserInterfaceControllable](./avplaybackuserinterfacecontrollable-7ti30.md)

## See Also

### Timeline and segments
- [class AVPlaybackUserInterfacePlaybackPosition](./avplaybackuserinterfaceplaybackposition.md)
  A snapshot comprising a playback position recorded at a known host time and the rate of position advancement.
- [class AVPlaybackUserInterfaceTimelineSegment](./avplaybackuserinterfacetimelinesegment.md)
  Represents a contiguous segment of timeline content with specific playback characteristics.
- [enum AVPlaybackUserInterfaceTimelineSegmentType](./avplaybackuserinterfacetimelinesegmenttype.md)
  Describes the type of content within a timeline segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacetimecontrollable-62fq2)*