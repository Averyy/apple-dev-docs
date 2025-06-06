# scale(_:toDuration:)

**Framework**: AVFoundation  
**Kind**: method

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

## Parameters

- `timeRange`: The time range to be changed.
- `duration`: The new duration for the time range.

## See Also

- [func insertEmptyTimeRange(CMTimeRange)](avmutablemovie/insertemptytimerange(_:).md)
  Adds an empty time range to a movie.
- [func insertTimeRange(CMTimeRange, of: AVAsset, at: CMTime, copySampleData: Bool) throws](avmutablemovie/inserttimerange(_:of:at:copysampledata:).md)
  Inserts all of the tracks in a specified time range of an asset into a movie.
- [func removeTimeRange(CMTimeRange)](avmutablemovie/removetimerange(_:).md)
  Removes the specified time range from a movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/scale(_:toduration:))*