# stroke(_:with:style:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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

If you only need to control the style’s [`lineWidth`](../strokestyle/linewidth.md) property, use [`stroke(_:with:lineWidth:)`](./stroke%28_,with,linewidth%29.md) instead.

## Parameters

- `path`: The path to outline.
- `shading`: The color or pattern to use when outlining the `path`.
- `style`: A style that indicates how to outline the path.

## See Also

### Drawing a path
- [func stroke(Path, with: GraphicsContext.Shading, lineWidth: CGFloat)](./stroke%28_,with,linewidth%29.md)
  Draws a path into the context with a specified line width.
- [func fill(Path, with: GraphicsContext.Shading, style: FillStyle)](./fill%28_,with,style%29.md)
  Draws a path into the context and fills the outlined region.
- [GraphicsContext.Shading](./shading.md)
  A color or pattern that you can use to outline or fill a path.
- [GraphicsContext.GradientOptions](./gradientoptions.md)
  Options that affect the rendering of color gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/stroke(_:with:style:))*