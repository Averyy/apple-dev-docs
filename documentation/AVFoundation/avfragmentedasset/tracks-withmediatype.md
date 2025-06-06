# tracks(withMediaType:)

**Framework**: AVFoundation  
**Kind**: method

Returns tracks that present media of a specified type.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- watchOS 1.0+

## Declaration

```swift
func tracks(withMediaType mediaType: AVMediaType) -> [AVFragmentedAssetTrack]
```

#### Return Value

An array of tracks of a specific media characteristic.

#### Discussion

Apple discourages the use of this method in iOS 15, tvOS 15, and macOS 12 or later. Load tracks asynchronously using [`loadTracks(withMediaType:completionHandler:)`](avfragmentedasset/loadtracks(withmediatype:completionhandler:).md) instead.

You may call this method without blocking the current thread after you’ve asynchronously loaded the [`tracks`](avasset/tracks.md) property.

## Parameters

- `mediaType`: The media type according to which the asset filters its tracks. For valid values see  .

## See Also

- [var tracks: [AVFragmentedAssetTrack]](avfragmentedasset/tracks.md)
  The tracks an asset contains.
- [func track(withTrackID: CMPersistentTrackID) -> AVFragmentedAssetTrack?](avfragmentedasset/track(withtrackid:).md)
  Returns a track that contains the specified identifier.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVFragmentedAssetTrack]](avfragmentedasset/tracks(withmediacharacteristic:).md)
  Returns tracks that present media of a specified characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avfragmentedasset/tracks(withmediatype:))*