# segment(forTrackTime:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns a segment whose target time range contains, or is closest to, the specified track time.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func segment(forTrackTime trackTime: CMTime) -> AVAssetTrackSegment?
```

```objc
- (AVAssetTrackSegment *) segmentForTrackTime:(CMTime) trackTime;
```

## Return Value

The [`AVCompositionTrackSegment`](../avcompositiontracksegment.md) associated with the track time.

## Parameters

- `trackTime`: The track time of the segment to return.

## See Also

### Accessing track segments
- [var segments: [AVAssetTrackSegment]](./segments.md)
  The time mappings from the track’s media samples to its timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/segment(fortracktime:))*