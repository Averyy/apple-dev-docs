# init(id:sourceName:contentDescription:type:duration:artwork:)

**Framework**: Now Playing  
**Kind**: init

Creates home media content.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(id: String, sourceName: String, contentDescription: String?, type: MediaType, duration: MediaDuration?, artwork: Artwork?)
```

## Parameters

- `id`: A unique identifier for this content.
- `sourceName`: The display name of the device or source providing the media.
- `contentDescription`: A short description of the content, or `nil` when unavailable.
- `type`: The media type.
- `duration`: The total duration, or `nil` when live or unknown.
- `artwork`: Artwork for the content, or `nil` when unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/homemediacontent/init(id:sourcename:contentdescription:type:duration:artwork:))*