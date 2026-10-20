# insertTimeRange(_:of:at:copySampleData:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) insertTimeRange:(CMTimeRange) timeRange ofTrack:(AVAssetTrack *) track atTime:(CMTime) startTime copySampleData:(BOOL) copySampleData error:(NSError **) outError;
```

## Parameters

- `timeRange`: The time range of the track to insert.
- `track`: An [`AVAssetTrack`](../avassettrack.md) object indicating the source of the inserted media. This value can’t be `nil`.
- `startTime`: The time in the target track at which the media is to be inserted.
- `copySampleData`: A Boolean value that indicates whether sample data is to be copied from the source to the destination during edits. If `YES`, the sample data is written to the location specified by the track property `mediaDataStorage` if non-nil, or else by the movie property `defaultMediaDataStorage` if non-nil; if both are nil, the method fails and returns `NO`. If `NO`, sample data isn’t written and sample references to the samples in their original container are added as necessary.

## See Also

### Managing time ranges
- [func insertEmptyTimeRange(CMTimeRange)](./insertemptytimerange%28_%29.md)
  Adds an empty time range to a track.
- [func removeTimeRange(CMTimeRange)](./removetimerange%28_%29.md)
  Removes the specified time range from a track.
- [func scaleTimeRange(CMTimeRange, toDuration: CMTime)](./scaletimerange%28_,toduration%29.md)
  Changes the duration of a time range in a track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/inserttimerange(_:of:at:copysampledata:))*