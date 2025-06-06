# init(opaque:colorMode:rendersAsynchronously:renderer:)

**Framework**: SwiftUI  
**Kind**: init

Creates and configures a canvas.

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
init(opaque: Bool = false, colorMode: ColorRenderingMode = .nonLinear, rendersAsynchronously: Bool = false, renderer: @escaping (inout GraphicsContext, CGSize) -> Void)
```

#### Discussion

Use this initializer to create a new canvas that you can draw into. For example, you can draw a path:

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

For information about using a context to draw into a canvas, see [`GraphicsContext`](graphicscontext.md). If you want to provide SwiftUI views for the renderer to use as drawing elements, use [`init(opaque:colorMode:rendersAsynchronously:renderer:symbols:)`](canvas/init(opaque:colormode:rendersasynchronously:renderer:symbols:).md) instead.

## Parameters

- `opaque`: A Boolean that indicates whether the canvas is fully   opaque. You might be able to improve performance by setting this   value to  , but then drawing a non-opaque image into the   context produces undefined results. The default is  .
- `colorMode`: A working color space and storage format of the canvas.   The default is  .
- `rendersAsynchronously`: A Boolean that indicates whether the canvas   can present its contents to its parent view asynchronously. The   default is  .
- `renderer`: A closure in which you conduct immediate mode drawing.   The closure takes two inputs: a context that you use to issue   drawing commands and a size — representing the current   size of the canvas — that you can use to customize the content.   The canvas calls the renderer any time it needs to redraw the   content.

## See Also

- [init(opaque: Bool, colorMode: ColorRenderingMode, rendersAsynchronously: Bool, renderer: (inout GraphicsContext, CGSize) -> Void, symbols: () -> Symbols)](canvas/init(opaque:colormode:rendersasynchronously:renderer:symbols:).md)
  Creates and configures a canvas that you supply with renderable child views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/canvas/init(opaque:colormode:rendersasynchronously:renderer:))*