# insertEmptyTimeRange(_:)

**Framework**: AVFoundation  
**Kind**: method

Adds an empty time range to a track.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func insertEmptyTimeRange(_ timeRange: CMTimeRange)
```

#### Discussion

You can’t add empty time ranges to the end of a track.

## Parameters

- `timeRange`: A time range to insert.

## See Also

- [func insertTimeRange(CMTimeRange, of: AVAssetTrack, at: CMTime, copySampleData: Bool) throws](avmutablemovietrack/inserttimerange(_:of:at:copysampledata:).md)
  Inserts a portion of an asset track into the target movie.
- [func removeTimeRange(CMTimeRange)](avmutablemovietrack/removetimerange(_:).md)
  Removes the specified time range from a track.
- [func scaleTimeRange(CMTimeRange, toDuration: CMTime)](avmutablemovietrack/scaletimerange(_:toduration:).md)
  Changes the duration of a time range in a track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/insertemptytimerange(_:))*