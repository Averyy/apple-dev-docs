# init(id:artworkProvider:)

**Framework**: Now Playing  
**Kind**: init

Creates an artwork whose image data loads on demand at the requested size.

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
init(id: String, artworkProvider: @escaping @Sendable (CGSize) async throws -> ArtworkRepresentation)
```

#### Discussion

The provider returns artwork that matches the requested size when possible. One dimension may differ if the artwork’s aspect ratio differs from the requested size. If the requested size exceeds the artwork’s maximum available size, the provider returns the artwork at its maximum size without enlarging the image.

## Parameters

- `id`: A unique identifier for this artwork.
- `artworkProvider`: A handler the system calls to request an [`ArtworkRepresentation`](artworkrepresentation.md) for a specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/artwork/init(id:artworkprovider:))*