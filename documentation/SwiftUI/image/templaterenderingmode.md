# Image.TemplateRenderingMode

**Framework**: SwiftUI  
**Kind**: enum

A type that indicates how SwiftUI renders images.

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
enum TemplateRenderingMode
```

## Topics

### Getting rendering modes
- [Image.TemplateRenderingMode.original](image/templaterenderingmode/original.md)
  A mode that renders pixels of bitmap images as-is.
- [Image.TemplateRenderingMode.template](image/templaterenderingmode/template.md)
  A mode that renders all non-transparent pixels as the foreground color.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func antialiased(Bool) -> Image](image/antialiased(_:).md)
  Specifies whether SwiftUI applies antialiasing when rendering the image.
- [func symbolRenderingMode(SymbolRenderingMode?) -> Image](image/symbolrenderingmode(_:).md)
  Sets the rendering mode for symbol images within this view.
- [func renderingMode(Image.TemplateRenderingMode?) -> Image](image/renderingmode(_:).md)
  Indicates whether SwiftUI renders an image as-is, or by using a different mode.
- [func interpolation(Image.Interpolation) -> Image](image/interpolation(_:).md)
  Specifies the current level of quality for rendering an image that requires interpolation.
- [Image.Interpolation](image/interpolation.md)
  The level of quality for rendering an image that requires interpolation, such as a scaled image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/image/templaterenderingmode)*