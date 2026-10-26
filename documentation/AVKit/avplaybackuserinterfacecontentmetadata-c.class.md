# AVPlaybackUserInterfaceContentMetadata

**Framework**: AVKit  
**Kind**: class  
**Role**: Class

Provides metadata information about media content including title, artwork, and content type.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
@interface AVPlaybackUserInterfaceContentMetadata : NSObject
```

## Topics

### Instance Properties
- [artworkRepresentations](./avplaybackuserinterfacecontentmetadata-c.class/artworkrepresentations.md)
  Array of available artwork representations in various formats and sizes for this media content. Multiple representations allow the system to choose the most appropriate artwork for different display contexts (thumbnails, full-screen, high-DPI displays). Each representation specifies its dimensions, format, and URL for optimal loading and display performance.
- [subtitle](./avplaybackuserinterfacecontentmetadata-c.class/subtitle.md)
  Secondary descriptive text such as artist name, episode description, or additional context for the content. This provides supplementary information to help users identify and understand the content being played.
- [title](./avplaybackuserinterfacecontentmetadata-c.class/title.md)
  Primary title or name of the media content for display in player UI and system interfaces. This should be the main identifying text for the content, such as a song title, episode name, or movie title.
- [videoProperties](./avplaybackuserinterfacecontentmetadata-c.class/videoproperties.md)
  Properties describing the video content. `nil` if the content contains no video.
### Instance Methods
- [- initWithTemplate:](./avplaybackuserinterfacecontentmetadata-c.class/initwithtemplate_.md)
  Initializes a new metadata object by copying values from a metadata template.
- [- initWithVideoProperties:title:subtitle:artworkRepresentations:](./avplaybackuserinterfacecontentmetadata-c.class/initwithvideoproperties_title_subtitle_artworkrepresentations_.md)
  Initializes a new metadata object with the specified properties.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Content metadata
- [AVPlaybackUserInterfaceMetadataProviding](./avplaybackuserinterfacemetadataproviding-1w04z.md)
  Provides metadata information about media content including title, artwork, and content type.
- [AVPlaybackUserInterfaceContentMetadataTemplate](./avplaybackuserinterfacecontentmetadatatemplate.md)
  A mutable template for configuring media metadata before creating immutable metadata objects.
- [class AVPlaybackUserInterfaceContentArtwork](./avplaybackuserinterfacecontentartwork.md)
  Base class representing artwork or cover art for media content.
- [class AVPlaybackUserInterfaceContentURLArtwork](./avplaybackuserinterfacecontenturlartwork.md)
  An artwork subclass that references artwork via a URL and content type.
- [AVPlaybackUserInterfaceContentVideoProperties](./avplaybackuserinterfacecontentvideoproperties.md)
  Properties specific to video content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacecontentmetadata-c.class)*