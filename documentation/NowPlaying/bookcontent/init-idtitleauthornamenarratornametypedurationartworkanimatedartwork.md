# init(id:title:authorName:narratorName:type:duration:artwork:animatedArtwork:)

**Framework**: Now Playing  
**Kind**: init

Creates audiobook content with static and animated artwork.

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
init(id: String, title: String, authorName: String, narratorName: String? = nil, type: MediaType = .audio, duration: MediaDuration?, artwork: Artwork, animatedArtwork: AnimatedArtwork?)
```

## Parameters

- `id`: A unique identifier for this book.
- `title`: The book’s display title.
- `authorName`: The name of the book’s author.
- `narratorName`: The name of the audiobook narrator, if available.
- `type`: The media type. Defaults to `.audio` for spoken-word content.
- `duration`: The total duration of the audiobook, or `nil` when unknown.
- `artwork`: Static cover artwork.
- `animatedArtwork`: Animated artwork for the book, or `nil` when unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/bookcontent/init(id:title:authorname:narratorname:type:duration:artwork:animatedartwork:))*