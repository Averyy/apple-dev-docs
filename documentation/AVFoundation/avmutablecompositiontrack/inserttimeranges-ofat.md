# insertTimeRanges(_:of:at:)

**Framework**: AVFoundation  
**Kind**: method

Inserts the time ranges of multiple source tracks into a track of a composition.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func insertTimeRanges(_ timeRanges: [NSValue], of tracks: [AVAssetTrack], at startTime: CMTime) throws
```

## Parameters

- `timeRanges`: The time ranges of media in the source tracks to insert.
- `tracks`: The source asset tracks that contain the media to insert.
- `startTime`: A start time within composition the track to insert the time range.

## See Also

- [var segments: [AVCompositionTrackSegment]!](avmutablecompositiontrack/segments.md)
  The track segments that a composition track contains.
- [func insertEmptyTimeRange(CMTimeRange)](avmutablecompositiontrack/insertemptytimerange(_:).md)
  Adds or extends an empty time range within the track.
- [func insertTimeRange(CMTimeRange, of: AVAssetTrack, at: CMTime) throws](avmutablecompositiontrack/inserttimerange(_:of:at:).md)
  Inserts a time range of media from a source track into a composition track.
- [func removeTimeRange(CMTimeRange)](avmutablecompositiontrack/removetimerange(_:).md)
  Removes a time range of media from a composition track.
- [func scaleTimeRange(CMTimeRange, toDuration: CMTime)](avmutablecompositiontrack/scaletimerange(_:toduration:).md)
  Changes the duration of a time range of the track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/inserttimeranges(_:of:at:))*