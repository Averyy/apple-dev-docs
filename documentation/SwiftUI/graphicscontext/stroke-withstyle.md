# stroke(_:with:style:)

**Framework**: SwiftUI  
**Kind**: method

Draws a path into the context with a specified stroke style.

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
func stroke(_ path: Path, with shading: GraphicsContext.Shading, style: StrokeStyle)
```

#### Discussion

If you only need to control the style’s [`lineWidth`](strokestyle/linewidth.md) property, use [`stroke(_:with:lineWidth:)`](graphicscontext/stroke(_:with:linewidth:).md) instead.

## Parameters

- `path`: The path to outline.
- `shading`: The color or pattern to use when outlining the  .
- `style`: A style that indicates how to outline the path.

## See Also

- [func stroke(Path, with: GraphicsContext.Shading, lineWidth: CGFloat)](graphicscontext/stroke(_:with:linewidth:).md)
  Draws a path into the context with a specified line width.
- [func fill(Path, with: GraphicsContext.Shading, style: FillStyle)](graphicscontext/fill(_:with:style:).md)
  Draws a path into the context and fills the outlined region.
- [GraphicsContext.Shading](graphicscontext/shading.md)
  A color or pattern that you can use to outline or fill a path.
- [GraphicsContext.GradientOptions](graphicscontext/gradientoptions.md)
  Options that affect the rendering of color gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/stroke(_:with:style:))*