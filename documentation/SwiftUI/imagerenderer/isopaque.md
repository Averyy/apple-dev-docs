# isOpaque

**Framework**: SwiftUI  
**Kind**: property

A Boolean value that indicates whether the alpha channel of the image is fully opaque.

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
final var isOpaque: Bool { get set }
```

#### Discussion

Setting this value to `true`, meaning the alpha channel is opaque, may improve performance. Don’t render non-opaque pixels to a renderer declared as opaque. This property defaults to `false`.

## See Also

- [var proposedSize: ProposedViewSize](imagerenderer/proposedsize.md)
  The size proposed to the root view.
- [var scale: CGFloat](imagerenderer/scale.md)
  The scale at which to render the image.
- [var colorMode: ColorRenderingMode](imagerenderer/colormode.md)
  The working color space and storage format of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/imagerenderer/isopaque)*