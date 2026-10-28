# ArtworkImage

**Framework**: MusicKit  
**Kind**: struct  
**Role**: Structure

A view that displays the image for a music item’s artwork.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@MainActor
@preconcurrency struct ArtworkImage
```

## Overview

You can create an artwork image with an instance of [`Artwork`](./artwork.md).

While the artwork’s image data is loading, [`ArtworkImage`](./artworkimage.md) automatically displays a placeholder with a solid color that matches the [`backgroundColor`](./artwork/backgroundcolor.md) property of the artwork to render.

## Topics

### Initializers
- [init(Artwork, height: CGFloat)](./artworkimage/init%28_,height%29.md)
  Creates an instance with a specified height.
- [init(Artwork, width: CGFloat)](./artworkimage/init%28_,width%29.md)
  Creates an instance with a specified width.
- [init(Artwork, width: CGFloat, height: CGFloat)](./artworkimage/init%28_,width,height%29.md)
  Creates an instance with a specified width and height.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [View](../SwiftUI/view.md)

## See Also

### Artwork
- [struct Artwork](./artwork.md)
  An object that represents artwork for a music item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage)*