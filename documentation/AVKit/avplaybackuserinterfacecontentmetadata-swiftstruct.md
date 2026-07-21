# AVPlaybackUserInterfaceContentMetadata

**Framework**: AVKit  
**Kind**: struct

A Swift-friendly structure representing media metadata.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
struct AVPlaybackUserInterfaceContentMetadata
```

#### Overview

This structure provides metadata information about media content including title, artwork, and content type. Use this to provide rich information for playback interfaces and system integrations.

## Topics

### Structures
- [AVPlaybackUserInterfaceContentMetadata.VideoProperties](avplaybackuserinterfacecontentmetadata-swift.struct/videoproperties-swift.struct.md)
  Properties specific to video content.
### Initializers
- [init(videoProperties: AVPlaybackUserInterfaceContentMetadata.VideoProperties?, title: String?, subtitle: String?, artworkRepresentations: [AVPlaybackUserInterfaceContentArtwork])](avplaybackuserinterfacecontentmetadata-swift.struct/init(videoproperties:title:subtitle:artworkrepresentations:).md)
  Creates a new metadata object.
### Instance Properties
- [var artworkRepresentations: [AVPlaybackUserInterfaceContentArtwork]](avplaybackuserinterfacecontentmetadata-swift.struct/artworkrepresentations.md)
  Array of available artwork representations in various formats and sizes.
- [var subtitle: String?](avplaybackuserinterfacecontentmetadata-swift.struct/subtitle.md)
  Secondary descriptive text such as artist name or episode description.
- [var title: String?](avplaybackuserinterfacecontentmetadata-swift.struct/title.md)
  Primary title or name of the media content.
- [var videoProperties: AVPlaybackUserInterfaceContentMetadata.VideoProperties?](avplaybackuserinterfacecontentmetadata-swift.struct/videoproperties-swift.property.md)
  Properties describing the video content. `nil` if the content contains no video.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol AVPlaybackUserInterfaceMetadataProviding](avplaybackuserinterfacemetadataproviding-814y4.md)
  Provides metadata information about media content including title, artwork, and content type.
- [class AVPlaybackUserInterfaceContentArtwork](avplaybackuserinterfacecontentartwork.md)
  Base class representing artwork or cover art for media content.
- [class AVPlaybackUserInterfaceContentURLArtwork](avplaybackuserinterfacecontenturlartwork.md)
  An artwork subclass that references artwork via a URL and content type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacecontentmetadata-swift.struct)*