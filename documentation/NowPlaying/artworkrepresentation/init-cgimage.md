# init(cgImage:)

**Framework**: Now Playing  
**Kind**: init

Creates an [`ArtworkRepresentation`](artworkrepresentation.md) from a `CGImage` instance.

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
init(cgImage: CGImage) throws
```

#### Discussion

If the provided image uses an unsupported format, this initializer returns `nil`.

## Parameters

- `cgImage`: The `CGImage` that represents the artwork.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/artworkrepresentation/init(cgimage:))*