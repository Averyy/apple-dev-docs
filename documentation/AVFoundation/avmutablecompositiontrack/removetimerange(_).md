# removeTimeRange(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Removes a time range of media from a composition track.

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
func removeTimeRange(_ timeRange: CMTimeRange)
```

```objc
- (void) removeTimeRange:(CMTimeRange) timeRange;
```

## Parameters

- `timeRange`: The time range to remove.

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
- [func scaleTimeRange(CMTimeRange, toDuration: CMTime)](./scaletimerange%28_,toduration%29.md)
  Changes the duration of a time range of the track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/removetimerange(_:))*