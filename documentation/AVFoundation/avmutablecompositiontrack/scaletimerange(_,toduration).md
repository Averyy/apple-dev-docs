# scaleTimeRange(_:toDuration:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Changes the duration of a time range of the track.

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
func scaleTimeRange(_ timeRange: CMTimeRange, toDuration duration: CMTime)
```

```objc
- (void) scaleTimeRange:(CMTimeRange) timeRange toDuration:(CMTime) duration;
```

## Parameters

- `timeRange`: The time range to scale.
- `duration`: A new duration value.

## See Also

### Managing time ranges
- [var segments: [AVCompositionTrackSegment]!](./segments.md)
  The track segments that a composition track contains.
- [func insertEmptyTimeRange(CMTimeRange)](./insertemptytimerange%28_%29.md)
  Adds or extends an empty time range within the track.
- [func insertTimeRange(CMTimeRange, of: AVAssetTrack, at: CMTime) throws](./inserttimerange%28_,of,at%29.md)
  Inserts a time range of media from a source track into a composition track.
- [func insertTimeRanges([NSValue], of: [AVAssetTrack], at: CMTime) throws](./inserttimeranges%28_,of,at%29.md)
  Inserts the time ranges of multiple source tracks into a track of a composition.
- [func removeTimeRange(CMTimeRange)](./removetimerange%28_%29.md)
  Removes a time range of media from a composition track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/scaletimerange(_:toduration:))*