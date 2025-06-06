# insertTimeRange(_:of:at:copySampleData:)

**Framework**: AVFoundation  
**Kind**: method

Inserts all of the tracks in a specified time range of an asset into a movie.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func insertTimeRange(_ timeRange: CMTimeRange, of asset: AVAsset, at startTime: CMTime, copySampleData: Bool) throws
```

#### Discussion

This method may add new tracks to the target movie to ensure that all tracks of the asset are represented in the inserted time range.

## Parameters

- `timeRange`: The time range of the asset to be inserted.
- `asset`: An   object indicating the source of the inserted media. This value can’t be  .
- `startTime`: The time in the target movie at which the media is to be inserted.
- `copySampleData`: A Boolean value that indicates whether sample data is to be copied from the source to the destination during edits.

## See Also

- [func insertEmptyTimeRange(CMTimeRange)](avmutablemovie/insertemptytimerange(_:).md)
  Adds an empty time range to a movie.
- [func scale(CMTimeRange, toDuration: CMTime)](avmutablemovie/scale(_:toduration:).md)
  Changes the duration of a time range in a movie.
- [func removeTimeRange(CMTimeRange)](avmutablemovie/removetimerange(_:).md)
  Removes the specified time range from a movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/inserttimerange(_:of:at:copysampledata:))*