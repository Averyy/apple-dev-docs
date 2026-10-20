# removeTrackAssociation(to:type:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Removes an association from a composition track.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func removeTrackAssociation(to compositionTrack: AVCompositionTrack, type trackAssociationType: AVAssetTrack.AssociationType)
```

```objc
- (void) removeTrackAssociationToTrack:(AVCompositionTrack *) compositionTrack type:(AVTrackAssociationType) trackAssociationType;
```

## Parameters

- `compositionTrack`: A composition track to remove the association from.
- `trackAssociationType`: The type of track association to remove.

## See Also

### Associating tracks
- [func addTrackAssociation(to: AVCompositionTrack, type: AVAssetTrack.AssociationType)](./addtrackassociation%28to,type%29.md)
  Establishes a track association of a specific type between two tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/removetrackassociation(to:type:))*