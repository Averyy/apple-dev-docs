# init(mediaMode:title:subtitle:albumArtworkRepresentations:)

**Framework**: AVKit  
**Kind**: init

Creates a new metadata object.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
init(mediaMode: AVInterfaceMetadata.MediaMode, title: String? = nil, subtitle: String? = nil, albumArtworkRepresentations: [AVInterfaceMetadata.AlbumArtwork] = [])
```

## Parameters

- `mediaMode`: The mode describing whether this content is audio-only or includes video.
- `title`: Primary title or name of the media content.
- `subtitle`: Secondary descriptive text.
- `albumArtworkRepresentations`: Array of available album artwork representations in various formats and sizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacemetadata-swift.struct/init(mediamode:title:subtitle:albumartworkrepresentations:))*