# AVInterfaceMetadataProviding

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
protocol AVInterfaceMetadataProviding : Observable
```

## Topics

### Providing metadata
- [var metadata: AVInterfaceMetadata](avinterfacemetadataproviding-666nk/metadata.md)
  The metadata object containing information about the media content.

## Relationships

### Inherits From
- [Observable](../Observation/Observable.md)
### Inherited By
- [AVInterfaceControllable](avinterfacecontrollable-3xs3i.md)

## See Also

- [struct AVInterfaceMetadata](avinterfacemetadata-swift.struct.md)
  A Swift-friendly structure representing media metadata.
- [class AVInterfaceAlbumArtwork](avinterfacealbumartwork.md)
  Base class representing album artwork or cover art for media content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacemetadataproviding-666nk)*