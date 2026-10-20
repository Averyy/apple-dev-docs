# AVPlaybackUserInterfaceContentArtwork

**Framework**: AVKit  
**Kind**: class  
**Role**: Class

Base class representing artwork or cover art for media content.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
class AVPlaybackUserInterfaceContentArtwork
```

```objc
@interface AVPlaybackUserInterfaceContentArtwork : NSObject
```

#### Overview

Use a concrete subclass such as [`AVPlaybackUserInterfaceContentURLArtwork`](./avplaybackuserinterfacecontenturlartwork.md) to create artwork instances.

## Topics

### Initializers
- [init?(coder: NSCoder)](./avplaybackuserinterfacecontentartwork/init%28coder%29.md)
### Instance Properties
- [var size: CGSize](./avplaybackuserinterfacecontentartwork/size.md)
  The pixel dimensions of the artwork image.
### Type Methods
- [class func artwork(url: URL, contentType: UTType, size: CGSize) -> AVPlaybackUserInterfaceContentURLArtwork](./avplaybackuserinterfacecontentartwork/artwork%28url,contenttype,size%29.md)
  Creates an artwork instance that references an image at the given URL.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [AVPlaybackUserInterfaceContentURLArtwork](./avplaybackuserinterfacecontenturlartwork.md)
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
- [class AVPlaybackUserInterfaceContentURLArtwork](./avplaybackuserinterfacecontenturlartwork.md)
  An artwork subclass that references artwork via a URL and content type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacecontentartwork)*