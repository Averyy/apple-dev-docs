# insertTimeRange(_:of:at:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Inserts a time range of media from a source track into a composition track.

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
func insertTimeRange(_ timeRange: CMTimeRange, of track: AVAssetTrack, at startTime: CMTime) throws
```

```objc
- (BOOL) insertTimeRange:(CMTimeRange) timeRange ofTrack:(AVAssetTrack *) track atTime:(CMTime) startTime error:(NSError **) outError;
```

#### Discussion

The time range you insert presents at its natural duration and rate. If necessary, you can scale it to a different duration by calling the [`scaleTimeRange(_:toDuration:)`](./scaletimerange%28_,toduration%29.md) method.

## Parameters

- `timeRange`: The time range of media in the source track to add.
- `track`: The source asset track that contains the media to add.
- `startTime`: A start time within the composition track to insert the time range.

## See Also

### Managing time ranges
- [var segments: [AVCompositionTrackSegment]!](./segments.md)
  The track segments that a composition track contains.
- [func insertEmptyTimeRange(CMTimeRange)](./insertemptytimerange%28_%29.md)
  Adds or extends an empty time range within the track.
- [func insertTimeRanges([NSValue], of: [AVAssetTrack], at: CMTime) throws](./inserttimeranges%28_,of,at%29.md)
  Inserts the time ranges of multiple source tracks into a track of a composition.
- [func removeTimeRange(CMTimeRange)](./removetimerange%28_%29.md)
  Removes a time range of media from a composition track.
- [func scaleTimeRange(CMTimeRange, toDuration: CMTime)](./scaletimerange%28_,toduration%29.md)
  Changes the duration of a time range of the track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/inserttimerange(_:of:at:))*