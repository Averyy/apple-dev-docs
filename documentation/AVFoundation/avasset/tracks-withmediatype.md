# tracks(withMediaType:)

**Framework**: AVFoundation  
**Kind**: method

Returns tracks that contain media of a specified type.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- watchOS 1.0+

## Declaration

```swift
func tracks(withMediaType mediaType: AVMediaType) -> [AVAssetTrack]
```

#### Return Value

An array of tracks, which is empty if there are no tracks with the media type.

#### Discussion

\You can call this method without blocking the current thread when the data in the [`tracks`](avasset/tracks.md) property is already loaded.

## Parameters

- `mediaType`: The media type of the tracks to return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/tracks(withmediatype:))*