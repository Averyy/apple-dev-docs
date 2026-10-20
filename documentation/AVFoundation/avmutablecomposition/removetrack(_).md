# removeTrack(_:)

**Framework**: AVFoundation  
**Kind**: method

Removes a specified track from the composition.

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
func removeTrack(_ track: AVCompositionTrack)
```

#### Discussion

When you remove a track, the system sets its composition value to nil.

## Parameters

- `track`: The track to remove.

## See Also

- [func mutableTrack(compatibleWith: AVAssetTrack) -> AVMutableCompositionTrack?](avmutablecomposition/mutabletrack(compatiblewith:).md)
  Returns a composition track into which you can insert any time range of the specified asset track.
- [func addMutableTrack(withMediaType: AVMediaType, preferredTrackID: CMPersistentTrackID) -> AVMutableCompositionTrack?](avmutablecomposition/addmutabletrack(withmediatype:preferredtrackid:).md)
  Adds an empty track to a composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/removetrack(_:))*