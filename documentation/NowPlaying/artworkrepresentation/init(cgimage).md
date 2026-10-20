# init(cgImage:)

**Framework**: Now Playing  
**Kind**: init

Creates an [`ArtworkRepresentation`](artworkrepresentation.md) from a `CGImage` instance.

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
init(cgImage: CGImage) throws
```

#### Discussion

If the provided image uses an unsupported format, this initializer returns `nil`.

## Parameters

- `cgImage`: The `CGImage` that represents the artwork.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/artworkrepresentation/init(cgimage:))*