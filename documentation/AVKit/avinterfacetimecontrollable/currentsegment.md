# currentSegment

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The segment containing the current playback position. This property automatically updates as playback progresses through different timeline segments. Use this to determine the current content type (primary vs. secondary) and any special playback characteristics that apply to the current position. Must be key-value observable.

## Declaration

```objc
@property (nonatomic, strong, readonly) AVInterfaceTimelineSegment * currentSegment;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacetimecontrollable/currentsegment)*