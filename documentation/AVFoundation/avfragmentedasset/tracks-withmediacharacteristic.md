# tracks(withMediaCharacteristic:)

**Framework**: AVFoundation  
**Kind**: method

Returns tracks that present media of a specified characteristic.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- watchOS 1.0+

## Declaration

```swift
func tracks(withMediaCharacteristic mediaCharacteristic: AVMediaCharacteristic) -> [AVFragmentedAssetTrack]
```

#### Return Value

An array of tracks of a specific media characteristic.

#### Discussion

Apple discourages the use of this method in iOS 15, tvOS 15, and macOS 12 or later. Load tracks asynchronously using [`loadTracks(withMediaCharacteristic:completionHandler:)`](avfragmentedasset/loadtracks(withmediacharacteristic:completionhandler:).md) instead.

You may call this method without blocking the current thread after you’ve asynchronously loaded the [`tracks`](avasset/tracks.md) property.

## Parameters

- `mediaCharacteristic`: The media characteristic according to which the asset filters its asset tracks. For valid values, see  .

## See Also

- [var tracks: [AVFragmentedAssetTrack]](avfragmentedasset/tracks.md)
  The tracks an asset contains.
- [func track(withTrackID: CMPersistentTrackID) -> AVFragmentedAssetTrack?](avfragmentedasset/track(withtrackid:).md)
  Returns a track that contains the specified identifier.
- [func tracks(withMediaType: AVMediaType) -> [AVFragmentedAssetTrack]](avfragmentedasset/tracks(withmediatype:).md)
  Returns tracks that present media of a specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avfragmentedasset/tracks(withmediacharacteristic:))*