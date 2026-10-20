# availableTrackAssociationTypes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

### Managing track associations
- [func associatedTracks(ofType: AVAssetTrack.AssociationType) -> [AVAssetTrack]](./associatedtracks%28oftype%29.md)
  Returns an array of associated tracks that have the specified association type.
- [func addTrackAssociation(to: AVMovieTrack, type: AVAssetTrack.AssociationType)](./addtrackassociation%28to,type%29.md)
  Creates a specific type of track association between two tracks.
- [func removeTrackAssociation(to: AVMovieTrack, type: AVAssetTrack.AssociationType)](./removetrackassociation%28to,type%29.md)
  Removes a specific type of track association between two tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/availabletrackassociationtypes)*