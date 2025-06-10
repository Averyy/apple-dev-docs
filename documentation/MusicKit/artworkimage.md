# ArtworkImage

**Framework**: MusicKit  
**Kind**: struct

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

#### Overview

You can create an artwork image with an instance of [`Artwork`](Artwork.md).

While the artwork’s image data is loading, [`ArtworkImage`](artworkimage.md) automatically displays a placeholder with a solid color that matches the [`backgroundColor`](Artwork/backgroundColor.md) property of the artwork to render.

## Topics

### Initializers
- [init(Artwork, height: CGFloat)](artworkimage/init(_:height:).md)
  Creates an instance with a specified height.
- [init(Artwork, width: CGFloat)](artworkimage/init(_:width:).md)
  Creates an instance with a specified width.
- [init(Artwork, width: CGFloat, height: CGFloat)](artworkimage/init(_:width:height:).md)
  Creates an instance with a specified width and height.
### Instance Properties
- [var body: some View](artworkimage/body-swift.property.md)
  The content and behavior of the view.
### Type Aliases
- [ArtworkImage.Body](artworkimage/body-swift.typealias.md)
  The type of view representing the body of this view.
### Default Implementations
- [View Implementations](artworkimage/view-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)

## See Also

- [struct Artwork](artwork.md)
  An object that represents artwork for a music item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage)*