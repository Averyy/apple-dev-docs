# Image.ResizingMode

**Framework**: SwiftUI  
**Kind**: enum

The modes that SwiftUI uses to resize an image to fit within its containing view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum ResizingMode
```

## Topics

### Getting resizing modes
- [Image.ResizingMode.stretch](image/resizingmode/stretch.md)
  A mode to enlarge or reduce the size of an image so that it fills the available space.
- [Image.ResizingMode.tile](image/resizingmode/tile.md)
  A mode to repeat the image at its original size, as many times as necessary to fill the available space.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Fitting images into available space](fitting-images-into-available-space.md)
  Adjust the size and shape of images in your app’s user interface by applying view modifiers.
- [func imageScale(Image.Scale) -> some View](view/imagescale(_:).md)
  Scales images within the view according to one of the relative sizes available including small, medium, and large images sizes.
- [var imageScale: Image.Scale](environmentvalues/imagescale.md)
  The image scale for this environment.
- [Image.Scale](image/scale.md)
  A scale to apply to vector images relative to text.
- [Image.Orientation](image/orientation.md)
  The orientation of an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/image/resizingmode)*