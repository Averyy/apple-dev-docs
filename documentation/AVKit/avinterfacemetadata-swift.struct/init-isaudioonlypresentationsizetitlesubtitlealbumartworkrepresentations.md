# init(isAudioOnly:presentationSize:title:subtitle:albumArtworkRepresentations:)

**Framework**: AVKit  
**Kind**: init

Creates a new metadata object.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
init(isAudioOnly: Bool = false, presentationSize: CGSize = .zero, title: String? = nil, subtitle: String? = nil, albumArtworkRepresentations: [AVInterfaceAlbumArtwork] = [])
```

## Parameters

- `isAudioOnly`: Whether the content is audio-only (default: false).
- `presentationSize`: The natural pixel dimensions of the video content (default: .zero).
- `title`: Primary title or name of the media content.
- `subtitle`: Secondary descriptive text.
- `albumArtworkRepresentations`: Array of available album artwork representations in various formats and sizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacemetadata-swift.struct/init(isaudioonly:presentationsize:title:subtitle:albumartworkrepresentations:))*