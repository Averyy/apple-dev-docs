# AVPlaybackUserInterfaceContentVideoProperties

**Framework**: AVKit  
**Kind**: class  
**Role**: Class

Properties specific to video content.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
@interface AVPlaybackUserInterfaceContentVideoProperties : NSObject
```

## Topics

### Instance Properties
- [presentationSize](./avplaybackuserinterfacecontentvideoproperties/presentationsize.md)
  The natural pixel dimensions of the video content for layout and aspect ratio calculations.
### Instance Methods
- [- initWithPresentationSize:](./avplaybackuserinterfacecontentvideoproperties/initwithpresentationsize_.md)
  Initializes a new video properties instance.

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
- [AVPlaybackUserInterfaceContentMetadata](./avplaybackuserinterfacecontentmetadata-c.class.md)
  Provides metadata information about media content including title, artwork, and content type.
- [AVPlaybackUserInterfaceContentMetadataTemplate](./avplaybackuserinterfacecontentmetadatatemplate.md)
  A mutable template for configuring media metadata before creating immutable metadata objects.
- [class AVPlaybackUserInterfaceContentArtwork](./avplaybackuserinterfacecontentartwork.md)
  Base class representing artwork or cover art for media content.
- [class AVPlaybackUserInterfaceContentURLArtwork](./avplaybackuserinterfacecontenturlartwork.md)
  An artwork subclass that references artwork via a URL and content type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacecontentvideoproperties)*