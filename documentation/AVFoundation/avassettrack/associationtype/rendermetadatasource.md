# renderMetadataSource

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

Indicates an association between a metadata track and another track where the metadata provides additional information for rendering of that track.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
static let renderMetadataSource: AVAssetTrack.AssociationType
```

```c
extern AVTrackAssociationType const AVTrackAssociationTypeRenderMetadataSource;
```

#### Discussion

This track association is not symmetric; when used with -[AVAssetWriterInput addTrackAssociationWithTrackOfInput:type:], the receiver should be an instance of AVAssetWriterInput with mediaType, AVMediaTypeMetadata, while the input parameter should be an instance of AVAssetWriterInput for the target track that would be rendered (for example, a video track).

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
- [static let selectionFollower: AVAssetTrack.AssociationType](./selectionfollower.md)
  An association between two tracks that specifies when a user selects the main track, the system should follow that selection by automatically selecting the associated track.
- [static let timecode: AVAssetTrack.AssociationType](./timecode.md)
  An association between a timecode track providing timing information for the main track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/associationtype/rendermetadatasource)*