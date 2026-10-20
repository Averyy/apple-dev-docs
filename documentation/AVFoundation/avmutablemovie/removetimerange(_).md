# removeTimeRange(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Removes the specified time range from a movie.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func removeTimeRange(_ timeRange: CMTimeRange)
```

```objc
- (void) removeTimeRange:(CMTimeRange) timeRange;
```

## Parameters

- `timeRange`: The time range to be removed.

## See Also

### Managing time ranges
- [func insertEmptyTimeRange(CMTimeRange)](./insertemptytimerange%28_%29.md)
  Adds an empty time range to a movie.
- [func insertTimeRange(CMTimeRange, of: AVAsset, at: CMTime, copySampleData: Bool) throws](./inserttimerange%28_,of,at,copysampledata%29.md)
  Inserts all of the tracks in a specified time range of an asset into a movie.
- [func scale(CMTimeRange, toDuration: CMTime)](./scale%28_,toduration%29.md)
  Changes the duration of a time range in a movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/removetimerange(_:))*