# insertTimeRange(_:of:at:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Inserts all tracks of an asset for a time range into a composition.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 9.0+ - Deprecated in 11.0

> **Deprecated**: Use [`insertTimeRange(_:of:at:isolation:)`](./inserttimerange%28_,of,at,isolation%29.md) instead.

## Declaration

```swift
func insertTimeRange(_ timeRange: CMTimeRange, of asset: AVAsset, at startTime: CMTime, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```objc
- (void) insertTimeRange:(CMTimeRange) timeRange ofAsset:(AVAsset *) asset atTime:(CMTime) startTime completionHandler:(void (^)(NSError *error)) completionHandler;
```

#### Discussion

If necessary, a composition adds new tracks to ensure that it inserts all tracks in the source asset for the time range. Inserting a time range pushes out existing content at the specified start time by the time range’s duration.

The composition presents the media data for the inserted time range at its natural duration and rate. You can scale it to a different duration, which changes the presentation rate, by calling [`scaleTimeRange(_:toDuration:)`](./scaletimerange%28_,toduration%29.md).

## Parameters

- `timeRange`: The time range of the asset’s tracks to insert into the composition.
- `asset`: The source asset that contains the tracks to insert.
- `startTime`: A time in the composition to present the inserted tracks.
- `completionHandler`: A callback the system invokes when the insertion is complete. If an error occurs, the system passes the callback an error object that describes the failure.

## See Also

### Managing time ranges
- [func removeTimeRange(CMTimeRange)](./removetimerange%28_%29.md)
  Removes a specified time range from all tracks of the composition.
- [func scaleTimeRange(CMTimeRange, toDuration: CMTime)](./scaletimerange%28_,toduration%29.md)
  Changes the duration of all tracks in a given time range.
- [func insertEmptyTimeRange(CMTimeRange)](./insertemptytimerange%28_%29.md)
  Adds or extends an empty time range within all tracks of the composition.
- [func insertTimeRange(CMTimeRange, of: AVAsset, at: CMTime) throws](./inserttimerange%28_,of,at%29.md)
  Inserts all the tracks within a given time range of a specified asset into the composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/inserttimerange(_:of:at:completionhandler:))*