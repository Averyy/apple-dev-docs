# timeRange

**Framework**: AVKit  
**Kind**: property  
**Required**: Yes

The time range representing the total duration and bounds of the media content.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
var timeRange: CMTimeRange { get }
```

#### Discussion

For on-demand content, `start` is typically zero and `duration` is the total length of the content.

For live content without DVR, set [`timeRange`](avplaybackuserinterfacetimecontrollable-50vcy/timerange.md) to a zero-duration range at the current live edge and advance it as the edge moves; [`seekableTimeRanges`](avplaybackuserinterfacetimecontrollable-50vcy/seekabletimeranges.md) must be nil or empty.

For live content with DVR, set [`timeRange`](avplaybackuserinterfacetimecontrollable-50vcy/timerange.md) to the available DVR window and advance both `start` and `end` as the window rolls. Use [`seekableTimeRanges`](avplaybackuserinterfacetimecontrollable-50vcy/seekabletimeranges.md) to indicate which portion is seekable.

The duration is always a finite, non-negative value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacetimecontrollable-50vcy/timerange)*