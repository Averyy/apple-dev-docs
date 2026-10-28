# scaleTimeRange(_:toDuration:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Changes the duration of all tracks in a given time range.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func scaleTimeRange(_ timeRange: CMTimeRange, toDuration duration: CMTime)
```

```objc
- (void) scaleTimeRange:(CMTimeRange) timeRange toDuration:(CMTime) duration;
```

## Discussion

A composition presents each track segment affected by the scaling operation at a rate equal to `source.duration / target.duration` of its resulting time mapping.

## Parameters

- `timeRange`: The time range of the composition to scale.
- `duration`: The new time range duration.

## See Also

### Managing time ranges
- [func removeTimeRange(CMTimeRange)](./removetimerange%28_%29.md)
  Removes a specified time range from all tracks of the composition.
- [func insertEmptyTimeRange(CMTimeRange)](./insertemptytimerange%28_%29.md)
  Adds or extends an empty time range within all tracks of the composition.
- [func insertTimeRange(CMTimeRange, of: AVAsset, at: CMTime, completionHandler: ((any Error)?) -> Void)](./inserttimerange%28_,of,at,completionhandler%29.md)
  Inserts all tracks of an asset for a time range into a composition.
- [func insertTimeRange(CMTimeRange, of: AVAsset, at: CMTime) throws](./inserttimerange%28_,of,at%29.md)
  Inserts all the tracks within a given time range of a specified asset into the composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/scaletimerange(_:toduration:))*