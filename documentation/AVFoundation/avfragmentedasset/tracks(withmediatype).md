# tracks(withMediaType:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns tracks that present media of a specified type.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Use [`loadTracks(withMediaType:completionHandler:)`](./loadtracks%28withmediatype,completionhandler%29.md) instead.

## Declaration

```swift
func tracks(withMediaType mediaType: AVMediaType) -> [AVFragmentedAssetTrack]
```

```objc
- (NSArray<AVFragmentedAssetTrack *> *) tracksWithMediaType:(AVMediaType) mediaType;
```

#### Return Value

An array of tracks of a specific media characteristic.

#### Discussion

Apple discourages the use of this method in iOS 15, tvOS 15, and macOS 12 or later. Load tracks asynchronously using [`loadTracks(withMediaType:completionHandler:)`](./loadtracks%28withmediatype,completionhandler%29.md) instead.

You may call this method without blocking the current thread after you’ve asynchronously loaded the [`tracks`](../avasset/tracks.md) property.

## Parameters

- `mediaType`: The media type according to which the asset filters its tracks. For valid values see [`AVMediaType`](../avmediatype.md).

## See Also

### Accessing tracks
- [var tracks: [AVFragmentedAssetTrack]](./tracks.md)
  The tracks an asset contains.
- [func track(withTrackID: CMPersistentTrackID) -> AVFragmentedAssetTrack?](./track%28withtrackid%29.md)
  Returns a track that contains the specified identifier.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVFragmentedAssetTrack]](./tracks%28withmediacharacteristic%29.md)
  Returns tracks that present media of a specified characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avfragmentedasset/tracks(withmediatype:))*