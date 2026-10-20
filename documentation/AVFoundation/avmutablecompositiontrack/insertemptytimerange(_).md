# insertEmptyTimeRange(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Adds or extends an empty time range within the track.

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
func insertEmptyTimeRange(_ timeRange: CMTimeRange)
```

```objc
- (void) insertEmptyTimeRange:(CMTimeRange) timeRange;
```

## Parameters

- `timeRange`: The empty time range to insert.

## See Also

### Managing time ranges
- [var segments: [AVCompositionTrackSegment]!](./segments.md)
  The track segments that a composition track contains.
- [func insertTimeRange(CMTimeRange, of: AVAssetTrack, at: CMTime) throws](./inserttimerange%28_,of,at%29.md)
  Inserts a time range of media from a source track into a composition track.
- [func insertTimeRanges([NSValue], of: [AVAssetTrack], at: CMTime) throws](./inserttimeranges%28_,of,at%29.md)
  Inserts the time ranges of multiple source tracks into a track of a composition.
- [func removeTimeRange(CMTimeRange)](./removetimerange%28_%29.md)
  Removes a time range of media from a composition track.
- [func scaleTimeRange(CMTimeRange, toDuration: CMTime)](./scaletimerange%28_,toduration%29.md)
  Changes the duration of a time range of the track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/insertemptytimerange(_:))*