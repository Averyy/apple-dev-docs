# segments

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

Segments representing different content types within the timeline. All segments should be contiguous and collectively cover the entire timeline duration without gaps or overlaps. Each segment defines a specific portion of content (such as main program, advertisements, or bonus material) with its own playback characteristics. Must be key-value observable.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
@property (nonatomic, copy, readonly) NSArray<AVPlaybackUserInterfaceTimelineSegment *> * segments;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacetimecontrollable-62fq2/segments)*