# symbolRenderingMode(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the rendering mode for symbol images within this view.

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
func symbolRenderingMode(_ mode: SymbolRenderingMode?) -> Image
```

#### Return Value

A view that uses the rendering mode you supply.

## Parameters

- `mode`: The symbol rendering mode to use.

## See Also

- [func antialiased(Bool) -> Image](image/antialiased(_:).md)
  Specifies whether SwiftUI applies antialiasing when rendering the image.
- [func renderingMode(Image.TemplateRenderingMode?) -> Image](image/renderingmode(_:).md)
  Indicates whether SwiftUI renders an image as-is, or by using a different mode.
- [func interpolation(Image.Interpolation) -> Image](image/interpolation(_:).md)
  Specifies the current level of quality for rendering an image that requires interpolation.
- [Image.TemplateRenderingMode](image/templaterenderingmode.md)
  A type that indicates how SwiftUI renders images.
- [Image.Interpolation](image/interpolation.md)
  The level of quality for rendering an image that requires interpolation, such as a scaled image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/image/symbolrenderingmode(_:))*