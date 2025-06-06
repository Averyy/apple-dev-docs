# tracks(withMediaCharacteristic:)

**Framework**: AVFoundation  
**Kind**: method

Returns an array of asset tracks matching the specified media characteristic.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- watchOS 1.0+

## Declaration

```swift
func tracks(withMediaCharacteristic mediaCharacteristic: AVMediaCharacteristic) -> [AVAssetTrack]
```

#### Return Value

An array of tracks, which is empty if there are no tracks with the media characteristic.

#### Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load tracks asynchronously using [`loadTracks(withMediaCharacteristic:completionHandler:)`](avasset/loadtracks(withmediacharacteristic:completionhandler:).md) instead.

You can call this method without blocking the current thread when the data in the [`tracks`](avasset/tracks.md) property is already loaded.

## Parameters

- `mediaCharacteristic`: The media characteristic of the tracks to return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/tracks(withmediacharacteristic:))*