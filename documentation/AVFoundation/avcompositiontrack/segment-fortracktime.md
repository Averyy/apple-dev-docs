# segment(forTrackTime:)

**Framework**: AVFoundation  
**Kind**: method

Returns a segment whose target time range contains, or is closest to, the specified track time.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func segment(forTrackTime trackTime: CMTime) -> AVCompositionTrackSegment?
```

#### Return Value

The [`AVCompositionTrackSegment`](avcompositiontracksegment.md) associated with the track time.

## Parameters

- `trackTime`: The track time of the segment to return.

## See Also

- [var segments: [AVCompositionTrackSegment]](avcompositiontrack/segments.md)
  The time mappings from the track’s media samples to its timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontrack/segment(fortracktime:))*