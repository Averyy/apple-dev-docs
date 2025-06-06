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
func track(withTrackID trackID: CMPersistentTrackID) -> AVAssetTrack?
```

#### Return Value

An asset track, or `nil` if there is no track with the identifier.

#### Discussion

You can call this method without blocking the current thread when the data in the [`tracks`](avasset/tracks.md) property is already loaded.

## Parameters

- `trackID`: The identifier of the track to retrieve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/track(withtrackid:))*