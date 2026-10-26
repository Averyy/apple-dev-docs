# timeRange

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The time range representing the total duration and bounds of the media content. This defines the overall playable timeline, with all segments and seekable ranges falling within this range. For on-demand content, `start` is typically zero and `duration` is the total length of the content. For live content without DVR, set [`timeRange`](./timerange.md) to a zero-duration range at the current live edge and advance it as the edge moves; [`seekableTimeRanges`](./seekabletimeranges.md) must be nil or empty. For live content with DVR, set [`timeRange`](./timerange.md) to the available DVR window and advance both `start` and `end` as the window rolls. Use [`seekableTimeRanges`](./seekabletimeranges.md) to indicate which portion is seekable. The duration is always a finite, non-negative value. Must be key-value observable.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
@property (nonatomic, readonly) CMTimeRange timeRange;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacetimecontrollable-62fq2/timerange)*