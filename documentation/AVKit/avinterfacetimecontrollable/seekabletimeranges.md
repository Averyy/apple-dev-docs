# seekableTimeRanges

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

An array of time ranges within the timeline where seeking operations are permitted. Each range is represented as an NSValue wrapping a CMTimeRange structure, defining portions of the timeline where users can jump to specific time positions during playback. If nil, the entire content defined by timeRange is considered seekable. When provided, each range must be a subset of the overall timeRange and should not overlap with other seekable ranges. An empty array means the entire content defined by timeRange is not seekable. Seekable ranges typically exclude segments where requiresLinearPlayback is YES, such as advertisements, mandatory content, or licensing-restricted portions. The array should contain ranges in chronological order for optimal performance. Must be key-value observable.

## Declaration

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<NSValue *> * seekableTimeRanges;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacetimecontrollable/seekabletimeranges)*