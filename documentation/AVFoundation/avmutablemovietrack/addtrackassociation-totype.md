# addTrackAssociation(to:type:)

**Framework**: AVFoundation  
**Kind**: method

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

## Parameters

- `movieTrack`: The AVMovieTrack object to be associated with the receiver.
- `trackAssociationType`: The type of track association to add between the receiver and the specified movie track.

## See Also

- [var availableTrackAssociationTypes: [AVAssetTrack.AssociationType]](avmutablemovietrack/availabletrackassociationtypes.md)
  An array of association types that the track uses to associate with other tracks.
- [func associatedTracks(ofType: AVAssetTrack.AssociationType) -> [AVAssetTrack]](avmutablemovietrack/associatedtracks(oftype:).md)
  Returns an array of associated tracks that have the specified association type.
- [func removeTrackAssociation(to: AVMovieTrack, type: AVAssetTrack.AssociationType)](avmutablemovietrack/removetrackassociation(to:type:).md)
  Removes a specific type of track association between two tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/addtrackassociation(to:type:))*