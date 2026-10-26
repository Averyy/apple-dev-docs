# currentSegment

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The segment containing the current playback position. This property automatically updates as playback progresses through different timeline segments. Use this to determine the current content type (primary vs. secondary) and any special playback characteristics that apply to the current position. Must be key-value observable.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
@property (nonatomic, copy, readonly) AVPlaybackUserInterfaceTimelineSegment * currentSegment;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacetimecontrollable-62fq2/currentsegment)*