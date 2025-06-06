# insertEmptyTimeRange(_:)

**Framework**: AVFoundation  
**Kind**: method

Adds or extends an empty time range within all tracks of the composition.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func insertEmptyTimeRange(_ timeRange: CMTimeRange)
```

#### Discussion

Inserting an empty time range pushes out existing content by the time range’s duration. Use this method to reserve a time range in the composition for a subsequently created track to present its media.

## Parameters

- `timeRange`: The empty time range to insert.

## See Also

- [func removeTimeRange(CMTimeRange)](avmutablecomposition/removetimerange(_:).md)
  Removes a specified time range from all tracks of the composition.
- [func scaleTimeRange(CMTimeRange, toDuration: CMTime)](avmutablecomposition/scaletimerange(_:toduration:).md)
  Changes the duration of all tracks in a given time range.
- [func insertTimeRange(CMTimeRange, of: AVAsset, at: CMTime, completionHandler: ((any Error)?) -> Void)](avmutablecomposition/inserttimerange(_:of:at:completionhandler:).md)
  Inserts all tracks of an asset for a time range into a composition.
- [func insertTimeRange(CMTimeRange, of: AVAsset, at: CMTime) throws](avmutablecomposition/inserttimerange(_:of:at:).md)
  Inserts all the tracks within a given time range of a specified asset into the composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/insertemptytimerange(_:))*