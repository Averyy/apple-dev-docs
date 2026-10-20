# AVPlaybackUserInterfaceContentURLArtwork

**Framework**: AVKit  
**Kind**: class  
**Role**: Class

An artwork subclass that references artwork via a URL and content type.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
class AVPlaybackUserInterfaceContentURLArtwork
```

```objc
@interface AVPlaybackUserInterfaceContentURLArtwork : AVPlaybackUserInterfaceContentArtwork
```

## Topics

### Instance Properties
- [var contentType: UTType](./avplaybackuserinterfacecontenturlartwork/contenttype.md)
  The uniform type identifier for the artwork image data.
- [var url: URL](./avplaybackuserinterfacecontenturlartwork/url.md)
  URL pointing to the artwork image resource.

## Relationships

### Inherits From
- [AVPlaybackUserInterfaceContentArtwork](./avplaybackuserinterfacecontentartwork.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Content metadata
- [protocol AVPlaybackUserInterfaceMetadataProviding](./avplaybackuserinterfacemetadataproviding-814y4.md)
  Provides metadata information about media content including title, artwork, and content type.
- [struct AVPlaybackUserInterfaceContentMetadata](./avplaybackuserinterfacecontentmetadata-swift.struct.md)
  A Swift-friendly structure representing media metadata.
- [class AVPlaybackUserInterfaceContentArtwork](./avplaybackuserinterfacecontentartwork.md)
  Base class representing artwork or cover art for media content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacecontenturlartwork)*