# tracks(withMediaType:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns tracks that contain media of a specified type.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Use [`loadTracks(withMediaType:completionHandler:)`](./loadtracks%28withmediatype,completionhandler%29.md)

## Declaration

```swift
func tracks(withMediaType mediaType: AVMediaType) -> [AVAssetTrack]
```

```objc
- (NSArray<AVAssetTrack *> *) tracksWithMediaType:(AVMediaType) mediaType;
```

#### Return Value

An array of tracks, which is empty if there are no tracks with the media type.

#### Discussion

\You can call this method without blocking the current thread when the data in the [`tracks`](./tracks.md) property is already loaded.

## Parameters

- `mediaType`: The media type of the tracks to return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/tracks(withmediatype:))*