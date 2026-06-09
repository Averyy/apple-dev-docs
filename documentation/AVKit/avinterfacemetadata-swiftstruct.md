# AVInterfaceMetadata

**Framework**: AVKit  
**Kind**: struct

A Swift-friendly structure representing media metadata.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
struct AVInterfaceMetadata
```

#### Overview

This structure provides metadata information about media content including title, artwork, and content type. Use this to provide rich information for playback interfaces and system integrations.

## Topics

### Creating metadata
- [init(isAudioOnly: Bool, presentationSize: CGSize, title: String?, subtitle: String?, albumArtworkRepresentations: [AVInterfaceAlbumArtwork])](avinterfacemetadata-swift.struct/init(isaudioonly:presentationsize:title:subtitle:albumartworkrepresentations:).md)
  Creates a new metadata object.
### Inspecting the metadata
- [var title: String?](avinterfacemetadata-swift.struct/title.md)
  Primary title or name of the media content.
- [var subtitle: String?](avinterfacemetadata-swift.struct/subtitle.md)
  Secondary descriptive text such as artist name or episode description.
- [var isAudioOnly: Bool](avinterfacemetadata-swift.struct/isaudioonly.md)
  Indicates whether the content is audio-only (no video component).
- [var presentationSize: CGSize](avinterfacemetadata-swift.struct/presentationsize.md)
  The natural pixel dimensions of the video content for display purposes.
- [var albumArtworkRepresentations: [AVInterfaceAlbumArtwork]](avinterfacemetadata-swift.struct/albumartworkrepresentations.md)
  Array of available album artwork representations in various formats and sizes.
### Album artwork
- [AVInterfaceMetadata.AlbumArtwork](avinterfacemetadata-swift.struct/albumartwork.md)
### Initializers
- [init(mediaMode: AVInterfaceMetadata.MediaMode, title: String?, subtitle: String?, albumArtworkRepresentations: [AVInterfaceMetadata.AlbumArtwork])](avinterfacemetadata-swift.struct/init(mediamode:title:subtitle:albumartworkrepresentations:).md)
  Creates a new metadata object.
### Instance Properties
- [var mediaMode: AVInterfaceMetadata.MediaMode](avinterfacemetadata-swift.struct/mediamode-swift.property.md)
  The mode describing whether this content is audio-only or includes video.
### Enumerations
- [AVInterfaceMetadata.MediaMode](avinterfacemetadata-swift.struct/mediamode-swift.enum.md)
  Describes the type of media content and its display characteristics.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol AVInterfaceMetadataProviding](avinterfacemetadataproviding-666nk.md)
  Provides metadata information about media content including title, artwork, and content type.
- [class AVInterfaceAlbumArtwork](avinterfacealbumartwork.md)
  Base class representing album artwork or cover art for media content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacemetadata-swift.struct)*