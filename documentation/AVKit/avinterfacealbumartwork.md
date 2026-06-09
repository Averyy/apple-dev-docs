# AVInterfaceAlbumArtwork

**Framework**: AVKit  
**Kind**: class

Base class representing album artwork or cover art for media content.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
class AVInterfaceAlbumArtwork
```

#### Overview

Use a concrete subclass such as @c AVInterfaceURLAlbumArtwork to create artwork instances.

## Topics

### Creating album artwork
- [init(url: URL, contentType: UTType, size: CGSize)](avinterfacealbumartwork/init(url:contenttype:size:)-8s6ku.md)
  Initializes a new album artwork object with the specified image resource information.
### Inspecting the artwork
- [var url: URL?](avinterfacealbumartwork/url.md)
  URL pointing to the album artwork image resource.
- [var contentType: UTType?](avinterfacealbumartwork/contenttype.md)
  The uniform type identifier for the artwork image data.
- [var size: CGSize](avinterfacealbumartwork/size.md)
  The pixel dimensions of the artwork image.
### Initializers
- [init(URL: URL, contentType: UTType, size: CGSize)](avinterfacealbumartwork/init(url:contenttype:size:)-5gq60.md)
- [init?(coder: NSCoder)](avinterfacealbumartwork/init(coder:).md)
### Type Methods
- [class func artwork(url: URL, contentType: UTType, size: CGSize) -> AVInterfaceURLAlbumArtwork](avinterfacealbumartwork/artwork(url:contenttype:size:).md)
  Creates an artwork instance that references an image at the given URL.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AVInterfaceURLAlbumArtwork](avinterfaceurlalbumartwork.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol AVInterfaceMetadataProviding](avinterfacemetadataproviding-666nk.md)
  Provides metadata information about media content including title, artwork, and content type.
- [struct AVInterfaceMetadata](avinterfacemetadata-swift.struct.md)
  A Swift-friendly structure representing media metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacealbumartwork)*