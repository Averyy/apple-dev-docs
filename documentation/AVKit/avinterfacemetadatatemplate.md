# AVInterfaceMetadataTemplate

**Framework**: AVKit  
**Kind**: class  
**Role**: Class

A mutable template for configuring media metadata before creating immutable metadata objects.

## Declaration

```objc
@interface AVInterfaceMetadataTemplate : NSObject
```

## Overview

Use this class to build and configure metadata for media content with full control over all properties. Once configured, create an immutable `AVInterfaceMetadata` object using `initWithTemplate:` to provide stable metadata for playback interfaces.

This template provides a convenient way to incrementally build metadata information, allowing you to set properties individually before finalizing the metadata. All properties are mutable (readwrite), making it ideal for scenarios where metadata is constructed from multiple sources or updated over time.

Example usage:

AVInterfaceMetadataTemplate *template = [[AVInterfaceMetadataTemplate alloc] init]; template.audioOnly = NO; template.title = @“Episode 5: The Journey Continues”; template.subtitle = @“Season 2”; template.albumArtworkRepresentations = @[artwork1, artwork2];

AVInterfaceMetadata *metadata = [[AVInterfaceMetadata alloc] initWithTemplate:template];

## Topics

### Instance Properties
- [albumArtworkRepresentations](./avinterfacemetadatatemplate/albumartworkrepresentations.md)
  Array of available album artwork representations in various formats and sizes for this media content. Multiple representations allow the system to choose the most appropriate artwork for different display contexts (thumbnails, full-screen, high-DPI displays). Each representation specifies its dimensions, format, and URL for optimal loading and display performance.
- [audioOnly](./avinterfacemetadatatemplate/audioonly.md)
  Indicates whether the content is audio-only (no video component). Used to optimize UI layout and player controls for audio-focused presentations. When YES, video-related controls and layouts should be hidden or adapted for audio-only playback experiences.
- [presentationSize](./avinterfacemetadatatemplate/presentationsize.md)
  The natural pixel dimensions of the video content for display purposes. This represents the encoded size of the video stream and can be used to determine aspect ratio and optimal presentation layout. For audio-only content, this value is CGSizeZero.
- [subtitle](./avinterfacemetadatatemplate/subtitle.md)
  Secondary descriptive text such as artist name, episode description, or additional context for the content. This provides supplementary information to help users identify and understand the content being played.
- [title](./avinterfacemetadatatemplate/title.md)
  Primary title or name of the media content for display in player UI and system interfaces. This should be the main identifying text for the content, such as a song title, episode name, or movie title.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacemetadatatemplate)*