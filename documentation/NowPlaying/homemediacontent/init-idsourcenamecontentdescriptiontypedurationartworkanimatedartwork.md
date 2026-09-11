# init(id:sourceName:contentDescription:type:duration:artwork:animatedArtwork:)

**Framework**: Now Playing  
**Kind**: init

Creates home media content with static and animated artwork.

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
init(id: String, sourceName: String, contentDescription: String?, type: MediaType, duration: MediaDuration?, artwork: Artwork, animatedArtwork: AnimatedArtwork?)
```

## Parameters

- `id`: A unique identifier for this content.
- `sourceName`: The display name of the device or source providing the media.
- `contentDescription`: A short description of the content, or `nil` when unavailable.
- `type`: The media type.
- `duration`: The total duration, or `nil` when live or unknown.
- `artwork`: Static artwork for the content.
- `animatedArtwork`: Animated artwork for the content, or `nil` when unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/homemediacontent/init(id:sourcename:contentdescription:type:duration:artwork:animatedartwork:))*