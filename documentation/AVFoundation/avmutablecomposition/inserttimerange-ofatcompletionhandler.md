# insertTimeRange(_:of:at:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Inserts all tracks of an asset for a time range into a composition.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func insertTimeRange(_ timeRange: CMTimeRange, of asset: AVAsset, at startTime: CMTime, completionHandler: @escaping ((any Error)?) -> Void)
```

#### Discussion

If necessary, a composition adds new tracks to ensure that it inserts all tracks in the source asset for the time range. Inserting a time range pushes out existing content at the specified start time by the time range’s duration.

The composition presents the media data for the inserted time range at its natural duration and rate. You can scale it to a different duration, which changes the presentation rate, by calling [`scaleTimeRange(_:toDuration:)`](avmutablecomposition/scaletimerange(_:toduration:).md).

## Parameters

- `timeRange`: The time range of the asset’s tracks to insert into the composition.
- `asset`: The source asset that contains the tracks to insert.
- `startTime`: A time in the composition to present the inserted tracks.
- `completionHandler`: A callback the system invokes when the insertion is complete. If an error occurs, the system passes the callback an error object that describes the failure.

## See Also

- [func removeTimeRange(CMTimeRange)](avmutablecomposition/removetimerange(_:).md)
  Removes a specified time range from all tracks of the composition.
- [func scaleTimeRange(CMTimeRange, toDuration: CMTime)](avmutablecomposition/scaletimerange(_:toduration:).md)
  Changes the duration of all tracks in a given time range.
- [func insertEmptyTimeRange(CMTimeRange)](avmutablecomposition/insertemptytimerange(_:).md)
  Adds or extends an empty time range within all tracks of the composition.
- [func insertTimeRange(CMTimeRange, of: AVAsset, at: CMTime) throws](avmutablecomposition/inserttimerange(_:of:at:).md)
  Inserts all the tracks within a given time range of a specified asset into the composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/inserttimerange(_:of:at:completionhandler:))*