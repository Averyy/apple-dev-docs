# Image.ResizingMode

**Framework**: SwiftUI  
**Kind**: enum  
**Role**: Enumeration

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
- [Image.ResizingMode.stretch](./resizingmode/stretch.md)
  A mode to enlarge or reduce the size of an image so that it fills the available space.
- [Image.ResizingMode.tile](./resizingmode/tile.md)
  A mode to repeat the image at its original size, as many times as necessary to fill the available space.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring an image
- [Fitting images into available space](../fitting-images-into-available-space.md)
  Adjust the size and shape of images in your app’s user interface by applying view modifiers.
- [func imageScale(Image.Scale) -> some View](../view/imagescale%28_%29.md)
  Scales images within the view according to one of the relative sizes available including small, medium, and large images sizes.
- [var imageScale: Image.Scale](../environmentvalues/imagescale.md)
  The image scale for this environment.
- [Image.Scale](./scale.md)
  A scale to apply to vector images relative to text.
- [Image.Orientation](./orientation.md)
  The orientation of an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/image/resizingmode)*