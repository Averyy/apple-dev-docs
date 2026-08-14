# AVPlaybackUserInterfaceMetadataProviding

**Framework**: AVKit  
**Kind**: protocol

Provides metadata information about media content including title, artwork, and content type.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
protocol AVPlaybackUserInterfaceMetadataProviding : AnyObject, Observable
```

## Topics

### Instance Properties
- [var metadata: AVPlaybackUserInterfaceContentMetadata](avplaybackuserinterfacemetadataproviding-814y4/metadata.md)
  The metadata object containing information about the media content.

## Relationships

### Inherits From
- [Observable](../observation/observable.md)
### Inherited By
- [AVPlaybackUserInterfaceControllable](avplaybackuserinterfacecontrollable-92fri.md)

## See Also

- [struct AVPlaybackUserInterfaceContentMetadata](avplaybackuserinterfacecontentmetadata-swift.struct.md)
  A Swift-friendly structure representing media metadata.
- [class AVPlaybackUserInterfaceContentArtwork](avplaybackuserinterfacecontentartwork.md)
  Base class representing artwork or cover art for media content.
- [class AVPlaybackUserInterfaceContentURLArtwork](avplaybackuserinterfacecontenturlartwork.md)
  An artwork subclass that references artwork via a URL and content type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacemetadataproviding-814y4)*