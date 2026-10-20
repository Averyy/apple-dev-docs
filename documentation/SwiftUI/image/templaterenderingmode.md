# Image.TemplateRenderingMode

**Framework**: SwiftUI  
**Kind**: enum  
**Role**: Enumeration

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
- [Image.TemplateRenderingMode.original](./templaterenderingmode/original.md)
  A mode that renders pixels of bitmap images as-is.
- [Image.TemplateRenderingMode.template](./templaterenderingmode/template.md)
  A mode that renders all non-transparent pixels as the foreground color.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Specifying rendering behavior
- [func antialiased(Bool) -> Image](./antialiased%28_%29.md)
  Specifies whether SwiftUI applies antialiasing when rendering the image.
- [func symbolRenderingMode(SymbolRenderingMode?) -> Image](./symbolrenderingmode%28_%29.md)
  Sets the rendering mode for symbol images within this view.
- [func renderingMode(Image.TemplateRenderingMode?) -> Image](./renderingmode%28_%29.md)
  Indicates whether SwiftUI renders an image as-is, or by using a different mode.
- [func interpolation(Image.Interpolation) -> Image](./interpolation%28_%29.md)
  Specifies the current level of quality for rendering an image that requires interpolation.
- [Image.Interpolation](./interpolation.md)
  The level of quality for rendering an image that requires interpolation, such as a scaled image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/image/templaterenderingmode)*