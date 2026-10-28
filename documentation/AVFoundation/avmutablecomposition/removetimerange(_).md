# removeTimeRange(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Removes a specified time range from all tracks of the composition.

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
func removeTimeRange(_ timeRange: CMTimeRange)
```

```objc
- (void) removeTimeRange:(CMTimeRange) timeRange;
```

## Discussion

After removing, existing content after the time range moves forward in the composition timeline.

Removing a time range doesn’t remove any existing tracks from the composition, even if removing it results in an empty track. Instead, it removes or truncates track segments that intersect with the time range.

## Parameters

- `timeRange`: The time range to remove.

## See Also

### Managing time ranges
- [func scaleTimeRange(CMTimeRange, toDuration: CMTime)](./scaletimerange%28_,toduration%29.md)
  Changes the duration of all tracks in a given time range.
- [func insertEmptyTimeRange(CMTimeRange)](./insertemptytimerange%28_%29.md)
  Adds or extends an empty time range within all tracks of the composition.
- [func insertTimeRange(CMTimeRange, of: AVAsset, at: CMTime, completionHandler: ((any Error)?) -> Void)](./inserttimerange%28_,of,at,completionhandler%29.md)
  Inserts all tracks of an asset for a time range into a composition.
- [func insertTimeRange(CMTimeRange, of: AVAsset, at: CMTime) throws](./inserttimerange%28_,of,at%29.md)
  Inserts all the tracks within a given time range of a specified asset into the composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/removetimerange(_:))*