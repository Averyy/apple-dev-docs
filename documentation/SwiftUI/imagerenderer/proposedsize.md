# proposedSize

**Framework**: SwiftUI  
**Kind**: property

The size proposed to the root view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@MainActor
final var proposedSize: ProposedViewSize { get set }
```

#### Discussion

The default value of this property, [`unspecified`](proposedviewsize/unspecified.md), produces an image that matches the original view size. You can provide a custom [`ProposedViewSize`](proposedviewsize.md) to override the view’s size in one or both dimensions.

## See Also

- [var scale: CGFloat](imagerenderer/scale.md)
  The scale at which to render the image.
- [var isOpaque: Bool](imagerenderer/isopaque.md)
  A Boolean value that indicates whether the alpha channel of the image is fully opaque.
- [var colorMode: ColorRenderingMode](imagerenderer/colormode.md)
  The working color space and storage format of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/imagerenderer/proposedsize)*