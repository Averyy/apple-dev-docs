# insertTimeRange(_:of:at:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Inserts all the tracks within a given time range of a specified asset into the composition.

**Availability**:
- iOS 4.0+ - Deprecated in 18.0
- iPadOS 4.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.7+ - Deprecated in 15.0
- tvOS 9.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 1.0+ - Deprecated in 11.0

> **Deprecated**: Use [`insertTimeRange(_:of:at:isolation:)`](./inserttimerange%28_,of,at,isolation%29.md) instead.

## Declaration

```swift
func insertTimeRange(_ timeRange: CMTimeRange, of asset: AVAsset, at startTime: CMTime) throws
```

```objc
- (BOOL) insertTimeRange:(CMTimeRange) timeRange ofAsset:(AVAsset *) asset atTime:(CMTime) startTime error:(NSError **) outError;
```

## Discussion

This method may add new tracks to ensure that all tracks of the asset are represented in the inserted time range.

Existing content at the specified start time is pushed out by the duration of the time range.

Media data for the inserted time range is presented at its natural duration; you can scale it to a different duration using [`scaleTimeRange(_:toDuration:)`](./scaletimerange%28_,toduration%29.md).

## Parameters

- `timeRange`: The time range of the asset to be inserted.
- `asset`: An asset that contains the tracks to be inserted.
- `startTime`: The time at which the inserted tracks should be presented by the receiver.

## See Also

### Managing time ranges
- [func removeTimeRange(CMTimeRange)](./removetimerange%28_%29.md)
  Removes a specified time range from all tracks of the composition.
- [func scaleTimeRange(CMTimeRange, toDuration: CMTime)](./scaletimerange%28_,toduration%29.md)
  Changes the duration of all tracks in a given time range.
- [func insertEmptyTimeRange(CMTimeRange)](./insertemptytimerange%28_%29.md)
  Adds or extends an empty time range within all tracks of the composition.
- [func insertTimeRange(CMTimeRange, of: AVAsset, at: CMTime, completionHandler: ((any Error)?) -> Void)](./inserttimerange%28_,of,at,completionhandler%29.md)
  Inserts all tracks of an asset for a time range into a composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/inserttimerange(_:of:at:))*