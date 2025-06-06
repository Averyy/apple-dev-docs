# removeTimeRange(_:)

**Framework**: AVFoundation  
**Kind**: method

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

## Parameters

- `timeRange`: The time range to be removed.

## See Also

- [func insertEmptyTimeRange(CMTimeRange)](avmutablemovie/insertemptytimerange(_:).md)
  Adds an empty time range to a movie.
- [func insertTimeRange(CMTimeRange, of: AVAsset, at: CMTime, copySampleData: Bool) throws](avmutablemovie/inserttimerange(_:of:at:copysampledata:).md)
  Inserts all of the tracks in a specified time range of an asset into a movie.
- [func scale(CMTimeRange, toDuration: CMTime)](avmutablemovie/scale(_:toduration:).md)
  Changes the duration of a time range in a movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/removetimerange(_:))*