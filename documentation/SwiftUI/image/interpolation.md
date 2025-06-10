# Image.Interpolation

**Framework**: SwiftUI  
**Kind**: enum

The level of quality for rendering an image that requires interpolation, such as a scaled image.

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
enum Interpolation
```

#### Overview

The [`interpolation(_:)`](image/interpolation(_:).md) modifier specifies the interpolation behavior when using the [`resizable(capInsets:resizingMode:)`](image/resizable(capinsets:resizingmode:).md) modifier on an [`Image`](image.md). Use this behavior to prioritize rendering performance or image quality.

## Topics

### Getting interpolation options
- [Image.Interpolation.high](image/interpolation/high.md)
  A value that indicates a high level of interpolation quality, which may slow down image rendering.
- [Image.Interpolation.low](image/interpolation/low.md)
  A value that indicates a low level of interpolation quality, which may speed up image rendering.
- [Image.Interpolation.medium](image/interpolation/medium.md)
  A value that indicates a medium level of interpolation quality, between the low- and high-quality values.
- [Image.Interpolation.none](image/interpolation/none.md)
  A value that indicates SwiftUI doesn’t interpolate image data.

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
- [Image.TemplateRenderingMode](image/templaterenderingmode.md)
  A type that indicates how SwiftUI renders images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/image/interpolation)*