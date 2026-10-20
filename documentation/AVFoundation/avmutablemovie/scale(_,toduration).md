# scale(_:toDuration:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Changes the duration of a time range in a movie.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func scale(_ timeRange: CMTimeRange, toDuration duration: CMTime)
```

```objc
- (void) scaleTimeRange:(CMTimeRange) timeRange toDuration:(CMTime) duration;
```

## Parameters

- `timeRange`: The time range to be changed.
- `duration`: The new duration for the time range.

## See Also

### Managing time ranges
- [func insertEmptyTimeRange(CMTimeRange)](./insertemptytimerange%28_%29.md)
  Adds an empty time range to a movie.
- [func insertTimeRange(CMTimeRange, of: AVAsset, at: CMTime, copySampleData: Bool) throws](./inserttimerange%28_,of,at,copysampledata%29.md)
  Inserts all of the tracks in a specified time range of an asset into a movie.
- [func removeTimeRange(CMTimeRange)](./removetimerange%28_%29.md)
  Removes the specified time range from a movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/scale(_:toduration:))*