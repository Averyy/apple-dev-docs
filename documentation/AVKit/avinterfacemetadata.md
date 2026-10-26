# AVInterfaceMetadata

**Framework**: AVKit  
**Kind**: class  
**Role**: Class

Provides metadata information about media content including title, artwork, and content type.

## Declaration

```objc
@interface AVInterfaceMetadata : NSObject
```

## Topics

### Instance Properties
- [albumArtworkRepresentations](./avinterfacemetadata/albumartworkrepresentations.md)
  Array of available album artwork representations in various formats and sizes for this media content. Multiple representations allow the system to choose the most appropriate artwork for different display contexts (thumbnails, full-screen, high-DPI displays). Each representation specifies its dimensions, format, and URL for optimal loading and display performance.
- [audioOnly](./avinterfacemetadata/audioonly.md)
  Indicates whether the content is audio-only (no video component). Used to optimize UI layout and player controls for audio-focused presentations. When YES, video-related controls and layouts should be hidden or adapted for audio-only playback experiences.
- [presentationSize](./avinterfacemetadata/presentationsize.md)
  The natural pixel dimensions of the video content for display purposes. This represents the encoded size of the video stream and can be used to determine aspect ratio and optimal presentation layout. For audio-only content, this value is CGSizeZero.
- [subtitle](./avinterfacemetadata/subtitle.md)
  Secondary descriptive text such as artist name, episode description, or additional context for the content. This provides supplementary information to help users identify and understand the content being played.
- [title](./avinterfacemetadata/title.md)
  Primary title or name of the media content for display in player UI and system interfaces. This should be the main identifying text for the content, such as a song title, episode name, or movie title.
### Instance Methods
- [- initWithAudioOnly:presentationSize:title:subtitle:albumArtworkRepresentations:](./avinterfacemetadata/initwithaudioonly_presentationsize_title_subtitle_albumartworkrepresentations_.md)
  Initializes a new metadata object with the specified properties.
- [- initWithTemplate:](./avinterfacemetadata/initwithtemplate_.md)
  Initializes a new metadata object by copying values from a metadata template.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacemetadata)*