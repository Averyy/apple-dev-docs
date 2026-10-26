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
func track(withTrackID trackID: CMPersistentTrackID) -> AVAssetTrack?
```

```objc
- (AVAssetTrack *) trackWithTrackID:(CMPersistentTrackID) trackID;
```

#### Return Value

An asset track, or `nil` if there is no track with the identifier.

#### Discussion

You can call this method without blocking the current thread when the data in the [`tracks`](./tracks.md) property is already loaded.

## Parameters

- `trackID`: The identifier of the track to retrieve.

## See Also

### Accessing tracks
- [tracks](./tracks.md)
  The tracks an asset contains.
- [- tracksWithMediaType:](./tracks%28withmediatype%29.md)
  Returns tracks that contain media of a specified type.
- [- tracksWithMediaCharacteristic:](./tracks%28withmediacharacteristic%29.md)
  Returns an array of asset tracks matching the specified media characteristic.
- [- unusedTrackID](./unusedtrackid%28%29.md)
  Returns an identifier that no other tracks in the asset use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/track(withtrackid:))*