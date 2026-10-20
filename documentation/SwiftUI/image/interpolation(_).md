# interpolation(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Specifies the current level of quality for rendering an image that requires interpolation.

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
func interpolation(_ interpolation: Image.Interpolation) -> Image
```

## Mentions

- [Fitting images into available space](../fitting-images-into-available-space.md)

#### Return Value

An image with the given interpolation value set.

#### Discussion

See the article [Fitting images into available space](../fitting-images-into-available-space.md) for examples of using `interpolation(_:)` when scaling an [`Image`](../image.md).

## Parameters

- `interpolation`: The quality level, expressed as a value of the `Interpolation` type, that SwiftUI applies when interpolating an image.

## See Also

### Specifying rendering behavior
- [func antialiased(Bool) -> Image](./antialiased%28_%29.md)
  Specifies whether SwiftUI applies antialiasing when rendering the image.
- [func symbolRenderingMode(SymbolRenderingMode?) -> Image](./symbolrenderingmode%28_%29.md)
  Sets the rendering mode for symbol images within this view.
- [func renderingMode(Image.TemplateRenderingMode?) -> Image](./renderingmode%28_%29.md)
  Indicates whether SwiftUI renders an image as-is, or by using a different mode.
- [Image.TemplateRenderingMode](./templaterenderingmode.md)
  A type that indicates how SwiftUI renders images.
- [Image.Interpolation](./interpolation.md)
  The level of quality for rendering an image that requires interpolation, such as a scaled image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/image/interpolation(_:))*