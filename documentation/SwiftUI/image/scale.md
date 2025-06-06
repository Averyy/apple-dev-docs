# Image.Scale

**Framework**: SwiftUI  
**Kind**: enum

A scale to apply to vector images relative to text.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 11.0+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum Scale
```

#### Overview

Use this type with the [`imageScale(_:)`](view/imagescale(_:).md) modifier, or the [`imageScale`](environmentvalues/imagescale.md) environment key, to set the image scale.

The following example shows the three `Scale` values as applied to a system symbol image, each set against a text view:

```swift
HStack { Image(systemName: "swift").imageScale(.small); Text("Small") }
HStack { Image(systemName: "swift").imageScale(.medium); Text("Medium") }
HStack { Image(systemName: "swift").imageScale(.large); Text("Large") }
```

![Vertically arranged text views that read Small, Medium, and](https://docs-assets.developer.apple.com/published/807d651a857b2a60654ec856ecf79588/SwiftUI-EnvironmentAdditions-Image-scale%402x.png)

## Topics

### Getting image scales
- [Image.Scale.small](image/scale/small.md)
  A scale that produces small images.
- [Image.Scale.medium](image/scale/medium.md)
  A scale that produces medium-sized images.
- [Image.Scale.large](image/scale/large.md)
  A scale that produces large images.

## Relationships

### Conforms To
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
- [Image.Orientation](image/orientation.md)
  The orientation of an image.
- [Image.ResizingMode](image/resizingmode.md)
  The modes that SwiftUI uses to resize an image to fit within its containing view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/image/scale)*