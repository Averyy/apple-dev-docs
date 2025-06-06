# removeTimeRange(_:)

**Framework**: AVFoundation  
**Kind**: method

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

## Parameters

- `timeRange`: The time range to remove.

## See Also

- [var segments: [AVCompositionTrackSegment]!](avmutablecompositiontrack/segments.md)
  The track segments that a composition track contains.
- [func insertEmptyTimeRange(CMTimeRange)](avmutablecompositiontrack/insertemptytimerange(_:).md)
  Adds or extends an empty time range within the track.
- [func insertTimeRange(CMTimeRange, of: AVAssetTrack, at: CMTime) throws](avmutablecompositiontrack/inserttimerange(_:of:at:).md)
  Inserts a time range of media from a source track into a composition track.
- [func insertTimeRanges([NSValue], of: [AVAssetTrack], at: CMTime) throws](avmutablecompositiontrack/inserttimeranges(_:of:at:).md)
  Inserts the time ranges of multiple source tracks into a track of a composition.
- [func scaleTimeRange(CMTimeRange, toDuration: CMTime)](avmutablecompositiontrack/scaletimerange(_:toduration:).md)
  Changes the duration of a time range of the track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/removetimerange(_:))*