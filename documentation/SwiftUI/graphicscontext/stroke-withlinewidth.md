# stroke(_:with:lineWidth:)

**Framework**: SwiftUI  
**Kind**: method

Draws a path into the context with a specified line width.

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
func stroke(_ path: Path, with shading: GraphicsContext.Shading, lineWidth: CGFloat = 1)
```

#### Discussion

When you call this method, all [`StrokeStyle`](strokestyle.md) properties other than [`lineWidth`](strokestyle/linewidth.md) take their default values. To control other style properties, use [`stroke(_:with:style:)`](graphicscontext/stroke(_:with:style:).md) instead.

## Parameters

- `path`: The path to outline.
- `shading`: The color or pattern to use when outlining the  .
- `lineWidth`: The width of the stroke, which defaults to  .

## See Also

- [func stroke(Path, with: GraphicsContext.Shading, style: StrokeStyle)](graphicscontext/stroke(_:with:style:).md)
  Draws a path into the context with a specified stroke style.
- [func fill(Path, with: GraphicsContext.Shading, style: FillStyle)](graphicscontext/fill(_:with:style:).md)
  Draws a path into the context and fills the outlined region.
- [GraphicsContext.Shading](graphicscontext/shading.md)
  A color or pattern that you can use to outline or fill a path.
- [GraphicsContext.GradientOptions](graphicscontext/gradientoptions.md)
  Options that affect the rendering of color gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/stroke(_:with:linewidth:))*