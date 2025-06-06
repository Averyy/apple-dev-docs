# antialiased(_:)

**Framework**: SwiftUI  
**Kind**: method

Specifies whether SwiftUI applies antialiasing when rendering the image.

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
func antialiased(_ isAntialiased: Bool) -> Image
```

#### Return Value

An image with the antialiasing behavior set.

## Parameters

- `isAntialiased`: A Boolean value that specifies whether to   allow antialiasing. Pass   to allow antialising,   otherwise.

## See Also

- [func symbolRenderingMode(SymbolRenderingMode?) -> Image](image/symbolrenderingmode(_:).md)
  Sets the rendering mode for symbol images within this view.
- [func renderingMode(Image.TemplateRenderingMode?) -> Image](image/renderingmode(_:).md)
  Indicates whether SwiftUI renders an image as-is, or by using a different mode.
- [func interpolation(Image.Interpolation) -> Image](image/interpolation(_:).md)
  Specifies the current level of quality for rendering an image that requires interpolation.
- [Image.TemplateRenderingMode](image/templaterenderingmode.md)
  A type that indicates how SwiftUI renders images.
- [Image.Interpolation](image/interpolation.md)
  The level of quality for rendering an image that requires interpolation, such as a scaled image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/image/antialiased(_:))*