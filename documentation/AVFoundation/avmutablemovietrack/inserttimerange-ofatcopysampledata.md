# insertTimeRange(_:of:at:copySampleData:)

**Framework**: AVFoundation  
**Kind**: method

Inserts a portion of an asset track into the target movie.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func insertTimeRange(_ timeRange: CMTimeRange, of track: AVAssetTrack, at startTime: CMTime, copySampleData: Bool) throws
```

## Parameters

- `timeRange`: The time range of the track to insert.
- `track`: An   object indicating the source of the inserted media. This value can’t be  .
- `startTime`: The time in the target track at which the media is to be inserted.
- `copySampleData`: A Boolean value that indicates whether sample data is to be copied from the source to the destination during edits. If  , the sample data is written to the location specified by the track property   if non-nil, or else by the movie property   if non-nil; if both are nil, the method fails and returns  . If  , sample data isn’t written and sample references to the samples in their original container are added as necessary.

## See Also

- [func insertEmptyTimeRange(CMTimeRange)](avmutablemovietrack/insertemptytimerange(_:).md)
  Adds an empty time range to a track.
- [func removeTimeRange(CMTimeRange)](avmutablemovietrack/removetimerange(_:).md)
  Removes the specified time range from a track.
- [func scaleTimeRange(CMTimeRange, toDuration: CMTime)](avmutablemovietrack/scaletimerange(_:toduration:).md)
  Changes the duration of a time range in a track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/inserttimerange(_:of:at:copysampledata:))*