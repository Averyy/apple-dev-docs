# addTrackAssociation(to:type:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Creates a specific type of track association between two tracks.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func addTrackAssociation(to movieTrack: AVMovieTrack, type trackAssociationType: AVAssetTrack.AssociationType)
```

```objc
- (void) addTrackAssociationToTrack:(AVMovieTrack *) movieTrack type:(AVTrackAssociationType) trackAssociationType;
```

## Parameters

- `movieTrack`: The AVMovieTrack object to be associated with the receiver.
- `trackAssociationType`: The type of track association to add between the receiver and the specified movie track.

## See Also

### Managing track associations
- [var availableTrackAssociationTypes: [AVAssetTrack.AssociationType]](./availabletrackassociationtypes.md)
  An array of association types that the track uses to associate with other tracks.
- [func associatedTracks(ofType: AVAssetTrack.AssociationType) -> [AVAssetTrack]](./associatedtracks%28oftype%29.md)
  Returns an array of associated tracks that have the specified association type.
- [func removeTrackAssociation(to: AVMovieTrack, type: AVAssetTrack.AssociationType)](./removetrackassociation%28to,type%29.md)
  Removes a specific type of track association between two tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/addtrackassociation(to:type:))*