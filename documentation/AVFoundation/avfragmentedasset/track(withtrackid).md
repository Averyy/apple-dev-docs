# track(withTrackID:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns a track that contains the specified identifier.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Use [`loadTrack(withTrackID:completionHandler:)`](./loadtrack%28withtrackid,completionhandler%29.md) instead.

## Declaration

```swift
func track(withTrackID trackID: CMPersistentTrackID) -> AVFragmentedAssetTrack?
```

```objc
- (AVFragmentedAssetTrack *) trackWithTrackID:(CMPersistentTrackID) trackID;
```

## Return Value

A fragmented asset track, or `nil` if no track with the specified identifier is available.

## Discussion

Apple discourages the use of this method in iOS 15, tvOS 15, and macOS 12 or later. Load a track asynchronously using [`loadTrack(withTrackID:completionHandler:)`](./loadtrack%28withtrackid,completionhandler%29.md) instead.

You may call this method without blocking the current thread after you’ve asynchronously loaded the [`tracks`](../avasset/tracks.md) property.

## Parameters

- `trackID`: The identifier of the track to return.

## See Also

### Accessing tracks
- [var tracks: [AVFragmentedAssetTrack]](./tracks.md)
  The tracks an asset contains.
- [func tracks(withMediaType: AVMediaType) -> [AVFragmentedAssetTrack]](./tracks%28withmediatype%29.md)
  Returns tracks that present media of a specified type.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVFragmentedAssetTrack]](./tracks%28withmediacharacteristic%29.md)
  Returns tracks that present media of a specified characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avfragmentedasset/track(withtrackid:))*