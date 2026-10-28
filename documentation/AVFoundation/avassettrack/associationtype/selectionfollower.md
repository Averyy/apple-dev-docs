# selectionFollower

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

An association between two tracks that specifies when a user selects the main track, the system should follow that selection by automatically selecting the associated track.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
static let selectionFollower: AVAssetTrack.AssociationType
```

```c
extern AVTrackAssociationType const AVTrackAssociationTypeSelectionFollower;
```

## Discussion

For example, a follower of an audio track could be a subtitle track in the same language. When the user chooses a language for audio, the subtitle language “follows” the audio language selection.

## See Also

### Track association types
- [static let audioFallback: AVAssetTrack.AssociationType](./audiofallback.md)
  The track contains the same content as another track, but in a more widely supported format.
- [static let chapterList: AVAssetTrack.AssociationType](./chapterlist.md)
  The associated track contains chapter information for the base track.
- [static let forcedSubtitlesOnly: AVAssetTrack.AssociationType](./forcedsubtitlesonly.md)
  An association between a subtitle track containing forced and nonforced subtitles and one with a subtitle track containing only forced subtitles.
- [static let metadataReferent: AVAssetTrack.AssociationType](./metadatareferent.md)
  An association between a metadata track and the track that it describes or annotates.
- [static let timecode: AVAssetTrack.AssociationType](./timecode.md)
  An association between a timecode track providing timing information for the main track.
- [static let renderMetadataSource: AVAssetTrack.AssociationType](./rendermetadatasource.md)
  Indicates an association between a metadata track and another track where the metadata provides additional information for rendering of that track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/associationtype/selectionfollower)*