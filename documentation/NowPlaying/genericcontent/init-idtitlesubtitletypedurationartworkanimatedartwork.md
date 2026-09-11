# init(id:title:subtitle:type:duration:artwork:animatedArtwork:)

**Framework**: Now Playing  
**Kind**: init

Creates generic media content with static and animated artwork.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(id: String, title: String, subtitle: String? = nil, type: MediaType, duration: MediaDuration?, artwork: Artwork, animatedArtwork: AnimatedArtwork?)
```

## Parameters

- `id`: A unique identifier for this content.
- `title`: The primary display title.
- `subtitle`: Secondary information to display below the title.
- `type`: The media type.
- `duration`: The total duration, or `nil` when unknown.
- `artwork`: Static artwork for the content.
- `animatedArtwork`: Animated artwork for the content, or `nil` when unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/genericcontent/init(id:title:subtitle:type:duration:artwork:animatedartwork:))*