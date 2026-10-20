# insertEmptyTimeRange(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Adds or extends an empty time range within all tracks of the composition.

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
func insertEmptyTimeRange(_ timeRange: CMTimeRange)
```

```objc
- (void) insertEmptyTimeRange:(CMTimeRange) timeRange;
```

#### Discussion

Inserting an empty time range pushes out existing content by the time range’s duration. Use this method to reserve a time range in the composition for a subsequently created track to present its media.

## Parameters

- `timeRange`: The empty time range to insert.

## See Also

### Managing time ranges
- [func removeTimeRange(CMTimeRange)](./removetimerange%28_%29.md)
  Removes a specified time range from all tracks of the composition.
- [func scaleTimeRange(CMTimeRange, toDuration: CMTime)](./scaletimerange%28_,toduration%29.md)
  Changes the duration of all tracks in a given time range.
- [func insertTimeRange(CMTimeRange, of: AVAsset, at: CMTime, completionHandler: ((any Error)?) -> Void)](./inserttimerange%28_,of,at,completionhandler%29.md)
  Inserts all tracks of an asset for a time range into a composition.
- [func insertTimeRange(CMTimeRange, of: AVAsset, at: CMTime) throws](./inserttimerange%28_,of,at%29.md)
  Inserts all the tracks within a given time range of a specified asset into the composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/insertemptytimerange(_:))*