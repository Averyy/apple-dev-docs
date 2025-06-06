# Canvas

**Framework**: SwiftUI  
**Kind**: struct

A view type that supports immediate mode drawing.

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
struct Canvas<Symbols> where Symbols : View
```

#### Overview

Use a canvas to draw rich and dynamic 2D graphics inside a SwiftUI view. The canvas passes a [`GraphicsContext`](graphicscontext.md) to the closure that you use to perform immediate mode drawing operations. The canvas also passes a [`CGSize`](https://developer.apple.com/documentation/CoreFoundation/CGSize) value that you can use to customize what you draw. For example, you can use the context’s [`stroke(_:with:lineWidth:)`](graphicscontext/stroke(_:with:linewidth:).md) command to draw a [`Path`](path.md) instance:

```swift
Canvas { context, size in
    context.stroke(
        Path(ellipseIn: CGRect(origin: .zero, size: size)),
        with: .color(.green),
        lineWidth: 4)
}
.frame(width: 300, height: 200)
.border(Color.blue)
```

The example above draws the outline of an ellipse that exactly inscribes a canvas with a blue border:

![A screenshot of a canvas view that shows the green outline of an](https://docs-assets.developer.apple.com/published/da33312de456cfbf0dfa4f0f517083c8/Canvas-1%402x.png)

In addition to outlined and filled paths, you can draw images, text, and complete SwiftUI views. To draw views, use the [`init(opaque:colorMode:rendersAsynchronously:renderer:symbols:)`](canvas/init(opaque:colormode:rendersasynchronously:renderer:symbols:).md) method to supply views that you can reference from inside the renderer. You can also add masks, apply filters, perform transforms, control blending, and more. For information about how to draw, see [`GraphicsContext`](graphicscontext.md).

A canvas doesn’t offer interactivity or accessibility for individual elements, including for views that you pass in as symbols. However, it might provide better performance for a complex drawing that involves dynamic data. Use a canvas to improve performance for a drawing that doesn’t primarily involve text or require interactive elements.

## Topics

### Creating a canvas
- [init(opaque: Bool, colorMode: ColorRenderingMode, rendersAsynchronously: Bool, renderer: (inout GraphicsContext, CGSize) -> Void)](canvas/init(opaque:colormode:rendersasynchronously:renderer:).md)
  Creates and configures a canvas.
- [init(opaque: Bool, colorMode: ColorRenderingMode, rendersAsynchronously: Bool, renderer: (inout GraphicsContext, CGSize) -> Void, symbols: () -> Symbols)](canvas/init(opaque:colormode:rendersasynchronously:renderer:symbols:).md)
  Creates and configures a canvas that you supply with renderable child views.
### Managing opacity and color
- [var isOpaque: Bool](canvas/isopaque.md)
  A Boolean that indicates whether the canvas is fully opaque.
- [var colorMode: ColorRenderingMode](canvas/colormode.md)
  The working color space and storage format of the canvas.
### Referencing symbols
- [var symbols: Symbols](canvas/symbols.md)
  A view that provides child views that you can use in the drawing callback.
### Rendering
- [var rendersAsynchronously: Bool](canvas/rendersasynchronously.md)
  A Boolean that indicates whether the canvas can present its contents to its parent view asynchronously.
- [var renderer: (inout GraphicsContext, CGSize) -> Void](canvas/renderer.md)
  The drawing callback that you use to draw into the canvas.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [View](view.md)

## See Also

- [Add Rich Graphics to Your SwiftUI App](add_rich_graphics_to_your_swiftui_app.md)
  Make your apps stand out by adding background materials, vibrancy, custom graphics, and animations.
- [struct GraphicsContext](graphicscontext.md)
  An immediate mode drawing destination, and its current state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/canvas)*