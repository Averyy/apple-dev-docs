# init(id:title:subtitle:type:duration:artwork:)

**Framework**: Now Playing  
**Kind**: init

Creates generic media content.

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
init(id: String, title: String, subtitle: String? = nil, type: MediaType, duration: MediaDuration?, artwork: Artwork?)
```

#### Discussion

Use this initializer when your media doesn’t fit other content types.

## Parameters

- `id`: A unique identifier for this content.
- `title`: The primary display title.
- `subtitle`: Secondary information to display below the title.
- `type`: The media type.
- `duration`: The total duration, or `nil` when unknown.
- `artwork`: Artwork for the content, or `nil` when unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/genericcontent/init(id:title:subtitle:type:duration:artwork:))*