# addMutableTrack(withMediaType:preferredTrackID:)

**Framework**: AVFoundation  
**Kind**: method

Adds an empty track to a composition.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func addMutableTrack(withMediaType mediaType: AVMediaType, preferredTrackID: CMPersistentTrackID) -> AVMutableCompositionTrack?
```

#### Return Value

A new mutable composition track.

## Parameters

- `mediaType`: The media type of the new track.
- `preferredTrackID`: The preferred track ID for the new track. The system generates a unique ID if the value you specify isn’t available. If you don’t need to specify a preferred track ID, pass  , and the system generates an appropriate identifier.

## See Also

- [func mutableTrack(compatibleWith: AVAssetTrack) -> AVMutableCompositionTrack?](avmutablecomposition/mutabletrack(compatiblewith:).md)
  Returns a composition track into which you can insert any time range of the specified asset track.
- [func removeTrack(AVCompositionTrack)](avmutablecomposition/removetrack(_:).md)
  Removes a specified track from the composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/addmutabletrack(withmediatype:preferredtrackid:))*