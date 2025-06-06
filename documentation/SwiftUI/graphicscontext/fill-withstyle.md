# fill(_:with:style:)

**Framework**: SwiftUI  
**Kind**: method

Draws a path into the context and fills the outlined region.

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
func fill(_ path: Path, with shading: GraphicsContext.Shading, style: FillStyle = FillStyle())
```

#### Discussion

The current drawing state of the context defines the full drawing operation. For example, the current transformation and clip shapes, and any styles applied to the result, affect the final result.

## Parameters

- `path`: The outline of the region to fill.
- `shading`: The color or pattern to use when filling the region   bounded by  .
- `style`: A style that indicates how to rasterize the path.

## See Also

- [func stroke(Path, with: GraphicsContext.Shading, lineWidth: CGFloat)](graphicscontext/stroke(_:with:linewidth:).md)
  Draws a path into the context with a specified line width.
- [func stroke(Path, with: GraphicsContext.Shading, style: StrokeStyle)](graphicscontext/stroke(_:with:style:).md)
  Draws a path into the context with a specified stroke style.
- [GraphicsContext.Shading](graphicscontext/shading.md)
  A color or pattern that you can use to outline or fill a path.
- [GraphicsContext.GradientOptions](graphicscontext/gradientoptions.md)
  Options that affect the rendering of color gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/fill(_:with:style:))*