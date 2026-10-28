# tracks(withMediaCharacteristic:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns an array of asset tracks matching the specified media characteristic.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Use [`loadTracks(withMediaCharacteristic:completionHandler:)`](./loadtracks%28withmediacharacteristic,completionhandler%29.md) instead

## Declaration

```swift
func tracks(withMediaCharacteristic mediaCharacteristic: AVMediaCharacteristic) -> [AVAssetTrack]
```

```objc
- (NSArray<AVAssetTrack *> *) tracksWithMediaCharacteristic:(AVMediaCharacteristic) mediaCharacteristic;
```

## Return Value

An array of tracks, which is empty if there are no tracks with the media characteristic.

## Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load tracks asynchronously using [`loadTracks(withMediaCharacteristic:completionHandler:)`](./loadtracks%28withmediacharacteristic,completionhandler%29.md) instead.

You can call this method without blocking the current thread when the data in the [`tracks`](./tracks.md) property is already loaded.

## Parameters

- `mediaCharacteristic`: The media characteristic of the tracks to return.

## See Also

### Accessing tracks
- [tracks](./tracks.md)
  The tracks an asset contains.
- [- trackWithTrackID:](./track%28withtrackid%29.md)
  Returns a track that contains the specified identifier.
- [- tracksWithMediaType:](./tracks%28withmediatype%29.md)
  Returns tracks that contain media of a specified type.
- [- unusedTrackID](./unusedtrackid%28%29.md)
  Returns an identifier that no other tracks in the asset use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/tracks(withmediacharacteristic:))*