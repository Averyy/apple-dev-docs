# scaleTimeRange(_:toDuration:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Changes the duration of a time range in a track.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func scaleTimeRange(_ timeRange: CMTimeRange, toDuration duration: CMTime)
```

```objc
- (void) scaleTimeRange:(CMTimeRange) timeRange toDuration:(CMTime) duration;
```

## Parameters

- `timeRange`: The time range to change.
- `duration`: The new duration for the time range.

## See Also

### Managing time ranges
- [func insertTimeRange(CMTimeRange, of: AVAssetTrack, at: CMTime, copySampleData: Bool) throws](./inserttimerange%28_,of,at,copysampledata%29.md)
  Inserts a portion of an asset track into the target movie.
- [func insertEmptyTimeRange(CMTimeRange)](./insertemptytimerange%28_%29.md)
  Adds an empty time range to a track.
- [func removeTimeRange(CMTimeRange)](./removetimerange%28_%29.md)
  Removes the specified time range from a track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/scaletimerange(_:toduration:))*