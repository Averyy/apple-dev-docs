# removeTrack(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Removes a specified track from the composition.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func removeTrack(_ track: AVCompositionTrack)
```

```objc
- (void) removeTrack:(AVCompositionTrack *) track;
```

## Discussion

When you remove a track, the system sets its composition value to nil.

## Parameters

- `track`: The track to remove.

## See Also

### Managing composition tracks
- [func mutableTrack(compatibleWith: AVAssetTrack) -> AVMutableCompositionTrack?](./mutabletrack%28compatiblewith%29.md)
  Returns a composition track into which you can insert any time range of the specified asset track.
- [func addMutableTrack(withMediaType: AVMediaType, preferredTrackID: CMPersistentTrackID) -> AVMutableCompositionTrack?](./addmutabletrack%28withmediatype,preferredtrackid%29.md)
  Adds an empty track to a composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/removetrack(_:))*