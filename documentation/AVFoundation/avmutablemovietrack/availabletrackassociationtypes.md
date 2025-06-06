# availableTrackAssociationTypes

**Framework**: AVFoundation  
**Kind**: property

An array of association types that the track uses to associate with other tracks.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var availableTrackAssociationTypes: [AVAssetTrack.AssociationType] { get }
```

## See Also

- [func associatedTracks(ofType: AVAssetTrack.AssociationType) -> [AVAssetTrack]](avmutablemovietrack/associatedtracks(oftype:).md)
  Returns an array of associated tracks that have the specified association type.
- [func addTrackAssociation(to: AVMovieTrack, type: AVAssetTrack.AssociationType)](avmutablemovietrack/addtrackassociation(to:type:).md)
  Creates a specific type of track association between two tracks.
- [func removeTrackAssociation(to: AVMovieTrack, type: AVAssetTrack.AssociationType)](avmutablemovietrack/removetrackassociation(to:type:).md)
  Removes a specific type of track association between two tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/availabletrackassociationtypes)*