# tracks(withMediaCharacteristic:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns tracks that present media of a specified characteristic.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Use [`loadTracks(withMediaCharacteristic:completionHandler:)`](./loadtracks%28withmediacharacteristic,completionhandler%29.md) instead.

## Declaration

```swift
func tracks(withMediaCharacteristic mediaCharacteristic: AVMediaCharacteristic) -> [AVFragmentedAssetTrack]
```

```objc
- (NSArray<AVFragmentedAssetTrack *> *) tracksWithMediaCharacteristic:(AVMediaCharacteristic) mediaCharacteristic;
```

#### Return Value

An array of tracks of a specific media characteristic.

#### Discussion

Apple discourages the use of this method in iOS 15, tvOS 15, and macOS 12 or later. Load tracks asynchronously using [`loadTracks(withMediaCharacteristic:completionHandler:)`](./loadtracks%28withmediacharacteristic,completionhandler%29.md) instead.

You may call this method without blocking the current thread after you’ve asynchronously loaded the [`tracks`](../avasset/tracks.md) property.

## Parameters

- `mediaCharacteristic`: The media characteristic according to which the asset filters its asset tracks. For valid values, see [`AVMediaCharacteristic`](../avmediacharacteristic.md).

## See Also

### Accessing tracks
- [var tracks: [AVFragmentedAssetTrack]](./tracks.md)
  The tracks an asset contains.
- [func track(withTrackID: CMPersistentTrackID) -> AVFragmentedAssetTrack?](./track%28withtrackid%29.md)
  Returns a track that contains the specified identifier.
- [func tracks(withMediaType: AVMediaType) -> [AVFragmentedAssetTrack]](./tracks%28withmediatype%29.md)
  Returns tracks that present media of a specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avfragmentedasset/tracks(withmediacharacteristic:))*