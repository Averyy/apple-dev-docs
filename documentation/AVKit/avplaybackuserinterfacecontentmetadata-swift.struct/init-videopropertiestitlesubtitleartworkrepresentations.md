# init(videoProperties:title:subtitle:artworkRepresentations:)

**Framework**: AVKit  
**Kind**: init

Creates a new metadata object.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
init(videoProperties: AVPlaybackUserInterfaceContentMetadata.VideoProperties? = nil, title: String? = nil, subtitle: String? = nil, artworkRepresentations: [AVPlaybackUserInterfaceContentArtwork] = [])
```

## Parameters

- `videoProperties`: Properties describing the video content, or `nil` for content without video.
- `title`: Primary title or name of the media content.
- `subtitle`: Secondary descriptive text.
- `artworkRepresentations`: Array of available artwork representations in various formats and sizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacecontentmetadata-swift.struct/init(videoproperties:title:subtitle:artworkrepresentations:))*