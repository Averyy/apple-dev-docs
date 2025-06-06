# track(withTrackID:)

**Framework**: AVFoundation  
**Kind**: method

Returns a track that contains the specified identifier.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- watchOS 1.0+

## Declaration

```swift
func track(withTrackID trackID: CMPersistentTrackID) -> AVFragmentedAssetTrack?
```

#### Return Value

A fragmented asset track, or `nil` if no track with the specified identifier is available.

#### Discussion

Apple discourages the use of this method in iOS 15, tvOS 15, and macOS 12 or later. Load a track asynchronously using [`loadTrack(withTrackID:completionHandler:)`](avfragmentedasset/loadtrack(withtrackid:completionhandler:).md) instead.

You may call this method without blocking the current thread after you’ve asynchronously loaded the [`tracks`](avasset/tracks.md) property.

## Parameters

- `trackID`: The identifier of the track to return.

## See Also

- [var tracks: [AVFragmentedAssetTrack]](avfragmentedasset/tracks.md)
  The tracks an asset contains.
- [func tracks(withMediaType: AVMediaType) -> [AVFragmentedAssetTrack]](avfragmentedasset/tracks(withmediatype:).md)
  Returns tracks that present media of a specified type.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVFragmentedAssetTrack]](avfragmentedasset/tracks(withmediacharacteristic:).md)
  Returns tracks that present media of a specified characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avfragmentedasset/track(withtrackid:))*