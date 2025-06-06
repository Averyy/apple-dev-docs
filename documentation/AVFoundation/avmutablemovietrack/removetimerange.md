# removeTimeRange(_:)

**Framework**: AVFoundation  
**Kind**: method

Removes the specified time range from a track.

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

- `timeRange`: The time range to remove.

## See Also

- [func insertTimeRange(CMTimeRange, of: AVAssetTrack, at: CMTime, copySampleData: Bool) throws](avmutablemovietrack/inserttimerange(_:of:at:copysampledata:).md)
  Inserts a portion of an asset track into the target movie.
- [func insertEmptyTimeRange(CMTimeRange)](avmutablemovietrack/insertemptytimerange(_:).md)
  Adds an empty time range to a track.
- [func scaleTimeRange(CMTimeRange, toDuration: CMTime)](avmutablemovietrack/scaletimerange(_:toduration:).md)
  Changes the duration of a time range in a track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/removetimerange(_:))*