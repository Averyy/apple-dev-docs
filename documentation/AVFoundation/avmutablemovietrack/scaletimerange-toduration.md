# scaleTimeRange(_:toDuration:)

**Framework**: AVFoundation  
**Kind**: method

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

## Parameters

- `timeRange`: The time range to change.
- `duration`: The new duration for the time range.

## See Also

- [func insertTimeRange(CMTimeRange, of: AVAssetTrack, at: CMTime, copySampleData: Bool) throws](avmutablemovietrack/inserttimerange(_:of:at:copysampledata:).md)
  Inserts a portion of an asset track into the target movie.
- [func insertEmptyTimeRange(CMTimeRange)](avmutablemovietrack/insertemptytimerange(_:).md)
  Adds an empty time range to a track.
- [func removeTimeRange(CMTimeRange)](avmutablemovietrack/removetimerange(_:).md)
  Removes the specified time range from a track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/scaletimerange(_:toduration:))*