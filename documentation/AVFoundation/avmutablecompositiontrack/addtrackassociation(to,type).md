# addTrackAssociation(to:type:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Establishes a track association of a specific type between two tracks.

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
func addTrackAssociation(to compositionTrack: AVCompositionTrack, type trackAssociationType: AVAssetTrack.AssociationType)
```

```objc
- (void) addTrackAssociationToTrack:(AVCompositionTrack *) compositionTrack type:(AVTrackAssociationType) trackAssociationType;
```

## Parameters

- `compositionTrack`: A composition track to associate.
- `trackAssociationType`: The type of track association to create between tracks.

## See Also

### Associating tracks
- [func removeTrackAssociation(to: AVCompositionTrack, type: AVAssetTrack.AssociationType)](./removetrackassociation%28to,type%29.md)
  Removes an association from a composition track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/addtrackassociation(to:type:))*