# mutableTrack(compatibleWith:)

**Framework**: AVFoundation  
**Kind**: method

Returns a composition track into which you can insert any time range of the specified asset track.

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
func mutableTrack(compatibleWith track: AVAssetTrack) -> AVMutableCompositionTrack?
```

#### Return Value

A mutable composition track, of `nil` if a compatible track isn’t available.

#### Discussion

To optimize performance, limit the number of tracks to only what you need to present media data in parallel. To present media data of the same type serially, even from multiple assets, use a single track of that media type. You use this method to identify a suitable existing target track for an insertion.

If there’s no compatible track available, you can create a new track of the same media type as `track` using [`addMutableTrack(withMediaType:preferredTrackID:)`](avmutablecomposition/addmutabletrack(withmediatype:preferredtrackid:).md).

This method is the counterpart to [`compatibleTrack(for:)`](avurlasset/compatibletrack(for:).md) on [`AVAsset`](avasset.md).

## Parameters

- `track`: The asset track to find a composition track for.

## See Also

- [func addMutableTrack(withMediaType: AVMediaType, preferredTrackID: CMPersistentTrackID) -> AVMutableCompositionTrack?](avmutablecomposition/addmutabletrack(withmediatype:preferredtrackid:).md)
  Adds an empty track to a composition.
- [func removeTrack(AVCompositionTrack)](avmutablecomposition/removetrack(_:).md)
  Removes a specified track from the composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/mutabletrack(compatiblewith:))*