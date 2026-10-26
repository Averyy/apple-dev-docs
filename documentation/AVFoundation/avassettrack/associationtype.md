# AVAssetTrack.AssociationType

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

Constants that define track association types.

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
struct AssociationType
```

```c
typedef NSString * AVTrackAssociationType;
```

## Topics

### Track association types
- [static let audioFallback: AVAssetTrack.AssociationType](./associationtype/audiofallback.md)
  The track contains the same content as another track, but in a more widely supported format.
- [static let chapterList: AVAssetTrack.AssociationType](./associationtype/chapterlist.md)
  The associated track contains chapter information for the base track.
- [static let forcedSubtitlesOnly: AVAssetTrack.AssociationType](./associationtype/forcedsubtitlesonly.md)
  An association between a subtitle track containing forced and nonforced subtitles and one with a subtitle track containing only forced subtitles.
- [static let metadataReferent: AVAssetTrack.AssociationType](./associationtype/metadatareferent.md)
  An association between a metadata track and the track that it describes or annotates.
- [static let selectionFollower: AVAssetTrack.AssociationType](./associationtype/selectionfollower.md)
  An association between two tracks that specifies when a user selects the main track, the system should follow that selection by automatically selecting the associated track.
- [static let timecode: AVAssetTrack.AssociationType](./associationtype/timecode.md)
  An association between a timecode track providing timing information for the main track.
- [static let renderMetadataSource: AVAssetTrack.AssociationType](./associationtype/rendermetadatasource.md)
  Indicates an association between a metadata track and another track where the metadata provides additional information for rendering of that track.
### Initializers
- [init(rawValue: String)](./associationtype/init%28rawvalue%29.md)
  Creates an association type with a string value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing track associations
- [availableTrackAssociationTypes](./availabletrackassociationtypes.md)
  An array of association types that the track uses to associate with other tracks.
- [- associatedTracksOfType:](./associatedtracks%28oftype%29.md)
  Returns an array of associated tracks that have the specified association type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/associationtype)*