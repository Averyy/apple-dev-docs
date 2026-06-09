# init(data:)

**Framework**: Now Playing  
**Kind**: init

Creates an [`ArtworkRepresentation`](artworkrepresentation.md) from image data.

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
init(data: Data) throws
```

#### Discussion

> **Note**: [`ArtworkRepresentation.ArtworkRepresentationError.noRepresentationAvailable`](artworkrepresentation/artworkrepresentationerror/norepresentationavailable.md) if the data doesn’t represent a valid image or uses an unsupported format.

## Parameters

- `data`: The encoded image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/artworkrepresentation/init(data:))*